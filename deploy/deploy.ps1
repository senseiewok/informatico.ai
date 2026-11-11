#!/usr/bin/env pwsh
<#
.SYNOPSIS
  Upload the standalone informatico.ai website (../src) to its sibling cPanel document root (/informatico.ai)
  over an encrypted FTPS connection using Windows' curl.exe.

.DESCRIPTION
  Run this yourself. The server, username, certificate domain, remoteDir and port come from deploy.local.json
  next to this script (a local file that git ignores; copy deploy.local.example.json and fill it in once), or from
  parameters, or from the DEPLOY_* environment variables, or are asked for. The password is asked for every
  time and never stored. There is no default server in this script. An unencrypted connection is never used,
  and the server certificate is fully checked.

  By default -RemoteDir is "informatico.ai", so when FTPS logs into cPanel home (/), src/* is uploaded into
   the standalone sibling document root /informatico.ai (never into /public_html).

  Use -DryRun first: it logs in and shows everything, but uploads nothing.

.EXAMPLE
  ./deploy.ps1 -DryRun
  ./deploy.ps1
#>
[CmdletBinding()]
param(
    [string] $Server = $env:DEPLOY_SERVER,
    [string] $User = $env:DEPLOY_USER,
    # Sibling folder on the server relative to the FTPS login home folder. Defaults to "informatico.ai".
    [string] $RemoteDir = 'informatico.ai',
    [int] $Port = 21,
    [string] $SiteUrl = 'https://informatico.ai',
    # The domain named by the server's certificate (the part after the first dot of its name). No default; asked for if not given.
    [string] $ServerCertDomain = $env:DEPLOY_CERT_DOMAIN,
    [switch] $DryRun,
    [switch] $Force
)

$ErrorActionPreference = 'Stop'
# Settings that are not secret live in a local, git-ignored file, so only the password has to be typed. Parameters and the environment win over it.
$localFile = Join-Path $PSScriptRoot 'deploy.local.json'
$local = $null
if (Test-Path -LiteralPath $localFile) {
    try { $local = Get-Content -Raw -LiteralPath $localFile | ConvertFrom-Json } catch { throw "deploy.local.json is not valid JSON: $($_.Exception.Message)" }
    if (-not $Server -and $local.server) { $Server = [string]$local.server }
    if (-not $User -and $local.user) { $User = [string]$local.user }
    if (-not $ServerCertDomain -and $local.certDomain) { $ServerCertDomain = [string]$local.certDomain }
    if (-not $PSBoundParameters.ContainsKey('RemoteDir') -and $local.PSObject.Properties['remoteDir'] -and $null -ne $local.remoteDir) {
        $RemoteDir = [string]$local.remoteDir
    }
    if (-not $PSBoundParameters.ContainsKey('Port') -and $local.port) { $Port = [int]$local.port }
}
$curl = (Get-Command curl.exe -ErrorAction SilentlyContinue).Source
if (-not $curl) { throw 'curl.exe not found. It ships with Windows 10/11 in C:\Windows\System32.' }
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$gitExe = (Get-Command git -ErrorAction SilentlyContinue).Source
if ($gitExe) {
    $curBranch = (& $gitExe -C $repoRoot rev-parse --abbrev-ref HEAD 2>$null)
    if ($curBranch -eq 'main') {
        $beforeHash = try { (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash } catch { '' }
        Write-Host 'Syncing local main checkout with GitHub (git pull --ff-only --autostash origin main)...' -ForegroundColor Cyan
        & $gitExe -C $repoRoot pull --ff-only --autostash origin main | Out-Host
        $afterHash = try { (Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash } catch { '' }
        if ($beforeHash -and $afterHash -and ($beforeHash -ne $afterHash)) {
            Write-Host 'deploy.ps1 was updated by git pull -- restarting with the updated script...' -ForegroundColor Cyan
            & $PSCommandPath @PSBoundParameters
            return
        }
    }
}
$src = (Resolve-Path (Join-Path $PSScriptRoot '..\src')).Path

# Only web assets go live; backups, hidden files and anything unexpected stay local. Keep in step with deploy/check_upload.py.
$allowed = '.html', '.css', '.js', '.mjs', '.webp', '.avif', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico',
    '.txt', '.xml', '.json', '.webmanifest', '.woff', '.woff2', '.csv', '.tsv', '.mp3', '.webm', '.md',
    '.glb', '.3mf', '.step', '.stp', '.dxf'
$textExts = '.html', '.css', '.js', '.mjs', '.svg', '.txt', '.xml', '.json', '.webmanifest', '.csv', '.tsv', '.md', '.step', '.stp', '.dxf'
$all = @(Get-ChildItem $src -Recurse -File)
# A settings or login file is never site content, even though .json is allowed (the same names deploy/check_upload.py refuses).
$settingsNames = 'credentials.json', 'auth.json', 'sftp.json', 'deploy.local.json'
$files = @($all | Where-Object {
    $_.Extension.ToLowerInvariant() -in $allowed -and
    $_.FullName.Substring($src.Length) -notmatch '[\\/]\.' -and
    $_.Name.ToLowerInvariant() -notin $settingsNames -and
    $_.Name -notlike 'sftp*.json' -and
    $_.Name -notlike '*.local.json' -and
    -not $_.LinkType
})
$skipped = @($all | Where-Object { $_.FullName -notin $files.FullName })
if (-not $files) { throw "No web files found in $src." }

if (-not $Server) { $Server = Read-Host 'Server' }
if (-not $User) { $User = Read-Host 'Username' }
if (-not $ServerCertDomain) { $ServerCertDomain = Read-Host 'Certificate domain (the part of the server certificate name after its first dot; put it in deploy.local.json to stop being asked)' }
if (-not ($Server -and $User -and $ServerCertDomain)) { throw 'The server, username and certificate domain are all needed.' }
if ($Server -notmatch '^[A-Za-z0-9.\-]+$') { throw "Invalid server hostname '$Server'." }
if ($ServerCertDomain -notmatch '^[A-Za-z0-9.\-]+$') { throw "Invalid certificate domain '$ServerCertDomain'." }
if ($Port -lt 1 -or $Port -gt 65535) { throw "Invalid port '$Port'." }
if ($RemoteDir -and ($RemoteDir -notmatch '^[A-Za-z0-9._/\-]+$' -or $RemoteDir -match '(^|/)\.\.(/|$)')) {
    throw "Invalid RemoteDir '$RemoteDir'."
}
$securePassword = Read-Host 'Password (not shown, not saved)' -AsSecureString

# Connect to the host's IP, but validate the certificate against a name it actually covers.
if ($Server -like "*.$ServerCertDomain") { $certHost = $Server; $resolve = @() }
else {
    try { $ip = (Resolve-DnsName $Server -Type A -ErrorAction Stop | Where-Object Type -eq 'A' | Select-Object -First 1).IPAddress }
    catch { throw "Server not found: '$Server' doesn't exist in DNS." }
    $certHost = "informatico.$ServerCertDomain"
    $resolve = @('--resolve', "$($certHost):$($Port):$ip")
}
$baseUrl = "ftp://$($certHost):$Port"

# The password reaches curl through standard input (a curl config line), never the command line.
# Written as raw UTF-8 bytes: Windows PowerShell 5.1 would otherwise prefix piped text with a
# byte-order mark, which curl rejects as an unknown option.
function ConvertTo-ProcessArgument([string] $a) {
    if ($a -notmatch '[\s"]') { return $a }
    '"' + ($a -replace '(\\*)"', '$1$1\"' -replace '(\\+)$', '$1$1') + '"'
}

function Invoke-Curl([string[]] $curlArgs) {
    $plain = [System.Net.NetworkCredential]::new('', $securePassword).Password
    $escape = { param($s) $s.Replace('\', '\\').Replace('"', '\"') }
    $config = 'user = "' + (& $escape $User) + ':' + (& $escape $plain) + '"' + "`n"
    # Pin FTPS to TLS 1.2 (--tlsv1.2 --tls-max 1.2) so Windows Schannel avoids TLS 1.3 NewSessionTicket /
    # data-channel close_notify races that trigger spurious Pure-FTPd 451 (curl exit 18) after file write.
    $common = @('-K', '-', '-sS', '--ssl-reqd', '--tlsv1.2', '--tls-max', '1.2', '--ssl-revoke-best-effort', '--connect-timeout', '20', '--max-time', '600') + $resolve
    $psi = [System.Diagnostics.ProcessStartInfo]::new($curl)
    $psi.Arguments = (@($common + $curlArgs) | ForEach-Object { ConvertTo-ProcessArgument $_ }) -join ' '
    $psi.UseShellExecute = $false
    $psi.RedirectStandardInput = $true; $psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
    $noBom = [System.Text.UTF8Encoding]::new($false)
    $savedInputEncoding = $null
    if ($psi.PSObject.Properties['StandardInputEncoding']) { $psi.StandardInputEncoding = $noBom }
    else { try { $savedInputEncoding = [Console]::InputEncoding; [Console]::InputEncoding = $noBom } catch { } }
    try { $proc = [System.Diagnostics.Process]::Start($psi) }
    finally { if ($savedInputEncoding) { try { [Console]::InputEncoding = $savedInputEncoding } catch { } } }
    $bytes = [System.Text.UTF8Encoding]::new($false).GetBytes($config)
    $proc.StandardInput.BaseStream.Write($bytes, 0, $bytes.Length)
    $proc.StandardInput.Close()
    $plain = $null; $config = $null; $bytes = $null
    $stdout = $proc.StandardOutput.ReadToEndAsync(); $stderr = $proc.StandardError.ReadToEndAsync()
    $proc.WaitForExit()
    $lines = @(($stdout.Result + "`n" + $stderr.Result) -split "`r?`n" | Where-Object { $_ })
    [pscustomobject]@{ Code = $proc.ExitCode; Output = $lines }
}

function Get-CurlError($result) {
    $detail = ($result.Output -join ' ').Trim()
    switch ($result.Code) {
        67 { "Login refused: the username or password is wrong. Type the password rather than pasting it. After several failures the host may block your address for a while; reset the password in the hosting control panel instead of retrying." }
        6 { "Server not found: $detail" }
        { $_ -in 35, 60 } { "Secure connection failed: $detail`nThe server's certificate didn't match $ServerCertDomain. If the site moved, pass the new domain with -ServerCertDomain." }
        { $_ -in 7, 28 } { "Connection timed out or was refused: $detail`nIf the login worked, the second (data) connection may be blocked by a firewall or VPN." }
        default { "curl failed (exit $($result.Code)): $detail" }
    }
}

function ConvertTo-UrlPath([string] $path) {
    ($path -split '/' | Where-Object { $_ } | ForEach-Object { [Uri]::EscapeDataString($_) }) -join '/'
}

# 1. Log in and look around.
$list = Invoke-Curl @('--list-only', "$baseUrl/")
if ($list.Code -ne 0) { throw (Get-CurlError $list) }
$root = @($list.Output | Where-Object { $_ -and $_ -notmatch '^curl:' } | ForEach-Object { ($_.Trim() -replace '^\./', '') })
if (-not $PSBoundParameters.ContainsKey('RemoteDir') -and $RemoteDir -eq 'informatico.ai') {
    # If an FTPS sub-account is already chrooted directly inside /informatico.ai (no informatico.ai subfolder, informatico.css at login root), upload to login root.
    if (($root -notcontains 'informatico.ai') -and ($root -contains 'informatico.css' -and $root -contains 'index.html')) {
        $RemoteDir = ''
    }
}
$remoteLabel = if ($RemoteDir) { "/$RemoteDir" } else { '/ (your login folder)' }

function Get-LiveFileUrl([string] $baseSiteUrl, [string] $relPath) {
    return "$baseSiteUrl/$($relPath)"
}

# Check live site in bounded batches of 20 to skip files that are already identical (unless -Force is set).
$unchangedCount = 0
if (-not $Force -and $SiteUrl) {
    try {
        Add-Type -AssemblyName System.Net.Http -ErrorAction SilentlyContinue
        [System.Net.ServicePointManager]::DefaultConnectionLimit = 24
        $httpClient = [System.Net.Http.HttpClient]::new()
        $httpClient.Timeout = [TimeSpan]::FromSeconds(20)
        $httpClient.DefaultRequestHeaders.CacheControl = [System.Net.Http.Headers.CacheControlHeaderValue]::Parse('no-cache')
        $baseSiteUrl = $SiteUrl.TrimEnd('/')
        $changedFiles = @()
        Write-Host "Comparing $($files.Count) local files against live site (skipping already-uploaded files)..." -ForegroundColor Cyan
        for ($i = 0; $i -lt $files.Count; $i += 20) {
            $end = [Math]::Min($i + 19, $files.Count - 1)
            $batch = @($files[$i..$end])
            $probes = @($batch | ForEach-Object {
                $rel = $_.FullName.Substring($src.Length + 1) -replace '\\', '/'
                $liveUrl = Get-LiveFileUrl $baseSiteUrl $rel
                [pscustomobject]@{
                    File = $_
                    Rel  = $rel
                    Url  = $liveUrl
                    Task = $httpClient.GetByteArrayAsync($liveUrl)
                }
            })
            foreach ($p in $probes) {
                $localBytes = [System.IO.File]::ReadAllBytes($p.File.FullName)
                $same = $false
                for ($try = 1; $try -le 2 -and -not $same; $try++) {
                    try {
                        $remoteBytes = if ($try -eq 1) { $p.Task.GetAwaiter().GetResult() } else { $httpClient.GetByteArrayAsync($p.Url).GetAwaiter().GetResult() }
                        if ($localBytes.Length -eq $remoteBytes.Length) {
                            $same = [System.Linq.Enumerable]::SequenceEqual([byte[]]$localBytes, [byte[]]$remoteBytes)
                        }
                        if (-not $same -and $p.File.Extension.ToLowerInvariant() -in $textExts) {
                            $locStr = [System.Text.Encoding]::UTF8.GetString($localBytes).Replace("`r`n", "`n")
                            $remStr = [System.Text.Encoding]::UTF8.GetString($remoteBytes).Replace("`r`n", "`n")
                            $same = ($locStr -ceq $remStr)
                        }
                        break
                    } catch {
                        $same = $false
                    }
                }
                if (-not $same -and $p.File.Extension.ToLowerInvariant() -eq '.md') {
                    # Apache .htaccess blocks .md over HTTP (404/403); verify directly over FTPS so .md files are not re-uploaded every run.
                    $mdRemote = ConvertTo-UrlPath ((@($RemoteDir, $p.Rel) | Where-Object { $_ }) -join '/')
                    $tmpMd = [System.IO.Path]::GetTempFileName()
                    try {
                        $ftpsMd = Invoke-Curl @('-o', $tmpMd, "$baseUrl/$mdRemote")
                        if ($ftpsMd.Code -eq 0 -and (Test-Path -LiteralPath $tmpMd)) {
                            $ftpsBytes = [System.IO.File]::ReadAllBytes($tmpMd)
                            $same = ($localBytes.Length -eq $ftpsBytes.Length) -and [System.Linq.Enumerable]::SequenceEqual([byte[]]$localBytes, [byte[]]$ftpsBytes)
                            if (-not $same) {
                                $locStr = [System.Text.Encoding]::UTF8.GetString($localBytes).Replace("`r`n", "`n")
                                $remStr = [System.Text.Encoding]::UTF8.GetString($ftpsBytes).Replace("`r`n", "`n")
                                $same = ($locStr -ceq $remStr)
                            }
                        }
                    } catch {
                    } finally {
                        Remove-Item -LiteralPath $tmpMd -Force -ErrorAction SilentlyContinue
                    }
                }
                if ($same) {
                    $unchangedCount++
                } else {
                    $changedFiles += $p.File
                }
            }
        }
        $httpClient.Dispose()
        $files = $changedFiles
    } catch {
        # If live HTTP probe fails (e.g. before initial cutover), fall back to uploading all files.
    }
}

# Prioritize core styles/scripts, root index/404/SEO files, modules, and HTML pages before heavy media/3D artifacts.
$files = @($files | Sort-Object @{ Expression = {
    $r = $_.FullName.Substring($src.Length + 1) -replace '\\', '/'
    if ($r -in @('styles.css', 'informatico.css', 'timegravity.css', 'informatico.js')) { -1 }
    elseif ($r -notmatch '/') { 0 }
    elseif ($r -match '^modules/') { 1 }
    elseif ($r -match '\.html$') { 2 }
    elseif ($r -match '^(audio|plates)/') { 4 }
    else { 3 }
}}, @{ Expression = { $_.FullName } })

''
"Connected to $Server as $User (encrypted, certificate verified as $certHost)."
"Login folder contains: $(($root | Sort-Object) -join ', ')"
"Upload target: $remoteLabel"
if ($unchangedCount -gt 0) {
    "Already up to date on live site: $unchangedCount file(s) (skipped; pass -Force to re-upload all)."
}
''
if ($files.Count -eq 0) {
    'All web files on the live site already match local src/. Nothing to upload.'
    return
}
"Will publish $($files.Count) changed/new file(s) via FTPS upload to $($remoteLabel):"
$files | ForEach-Object { "  {0,10:N0}  {1}" -f $_.Length, $_.FullName.Substring($src.Length + 1) }
if ($skipped) {
    'Skipped (stay local):'
    $skipped | ForEach-Object { "  $($_.FullName.Substring($src.Length + 1))" }
}
''

if ($DryRun) { 'Dry run: nothing was uploaded.'; return }
if ((Read-Host 'Type DEPLOY to upload to the live site') -cne 'DEPLOY') { 'Cancelled; nothing was uploaded.'; return }

function Test-LiveFileUploaded($fileInfo, [string] $relPath, [string] $remoteUrlPath = '') {
    $localBytes = [System.IO.File]::ReadAllBytes($fileInfo.FullName)
    if ($SiteUrl) {
        try {
            Add-Type -AssemblyName System.Net.Http -ErrorAction SilentlyContinue
            $hc = [System.Net.Http.HttpClient]::new()
            try {
                $hc.Timeout = [TimeSpan]::FromSeconds(12)
                $hc.DefaultRequestHeaders.CacheControl = [System.Net.Http.Headers.CacheControlHeaderValue]::Parse('no-cache, no-store')
                $baseSiteUrl = $SiteUrl.TrimEnd('/')
                for ($checkTry = 1; $checkTry -le 2; $checkTry++) {
                    try {
                        $bust = [Guid]::NewGuid().ToString('N')
                        $liveUrl = Get-LiveFileUrl $baseSiteUrl $relPath
                        # Must wrap $($liveUrl) before '?' because '?' is a valid variable-name character in PowerShell!
                        $remoteBytes = $hc.GetByteArrayAsync("$($liveUrl)?nocache=$bust").GetAwaiter().GetResult()
                        if ($localBytes.Length -eq $remoteBytes.Length -and [System.Linq.Enumerable]::SequenceEqual([byte[]]$localBytes, [byte[]]$remoteBytes)) {
                            return $true
                        }
                        if ($fileInfo.Extension.ToLowerInvariant() -in $textExts) {
                            $locStr = [System.Text.Encoding]::UTF8.GetString($localBytes).Replace("`r`n", "`n")
                            $remStr = [System.Text.Encoding]::UTF8.GetString($remoteBytes).Replace("`r`n", "`n")
                            if ($locStr -ceq $remStr) { return $true }
                        }
                    } catch {
                    }
                    if ($checkTry -lt 2) { Start-Sleep -Milliseconds 1500 }
                }
            } finally {
                $hc.Dispose()
            }
        } catch {
        }
    }
    if ($remoteUrlPath) {
        $tmpVerify = [System.IO.Path]::GetTempFileName()
        try {
            $ftpsCheck = Invoke-Curl @('-o', $tmpVerify, "$baseUrl/$remoteUrlPath")
            if ($ftpsCheck.Code -eq 0 -and (Test-Path -LiteralPath $tmpVerify)) {
                $ftpsBytes = [System.IO.File]::ReadAllBytes($tmpVerify)
                if ($localBytes.Length -eq $ftpsBytes.Length -and [System.Linq.Enumerable]::SequenceEqual([byte[]]$localBytes, [byte[]]$ftpsBytes)) {
                    return $true
                }
            }
        } catch {
        } finally {
            Remove-Item -LiteralPath $tmpVerify -Force -ErrorAction SilentlyContinue
        }
    }
    return $false
}

# 2. Upload files one file per curl invocation (avoids Windows Schannel FTPS multi-transfer truncation)
#    with gentle inter-file pacing, live HTTPS + FTPS byte-for-byte verification when Pure-FTPd emits a
#    spurious post-write 451 (curl exit 18) on data-channel teardown, and PASV/rate-limited retries.
$totalToPublish = $files.Count
$uploaded = 0
foreach ($f in $files) {
    if ($uploaded -gt 0) {
        if (($uploaded % 60) -eq 0) {
            Start-Sleep -Seconds 15
        } elseif (($uploaded % 12) -eq 0) {
            Start-Sleep -Seconds 6
        } else {
            Start-Sleep -Milliseconds 700
        }
    }
    $rel = $f.FullName.Substring($src.Length + 1) -replace '\\', '/'
    $remote = ConvertTo-UrlPath ((@($RemoteDir, $rel) | Where-Object { $_ }) -join '/')
    $ok = $false
    $lastRes = $null
    for ($attempt = 1; $attempt -le 7; $attempt++) {
        $extraFlags = if ($attempt -ge 2) { @('--disable-epsv', '--limit-rate', '256k') } else { @() }
        $lastRes = Invoke-Curl ($extraFlags + @('--ftp-create-dirs', '-T', $f.FullName, "$baseUrl/$remote"))
        if ($lastRes.Code -eq 0) {
            $ok = $true
            break
        }
        Start-Sleep -Milliseconds 1500
        if (Test-LiveFileUploaded $f $rel $remote) {
            Write-Host "  [FTPS teardown 451 on $rel, but live HTTPS byte-for-byte check passed -- continuing]" -ForegroundColor Cyan
            $ok = $true
            break
        }
        $waitSec = [Math]::Min(60, 6 * $attempt * $attempt)
        Write-Host "  [FTPS rate-limit/451 on $rel (attempt $attempt/7) -- cooling down ${waitSec}s before retry...]" -ForegroundColor Yellow
        Start-Sleep -Seconds $waitSec
    }
    if (-not $ok) { throw "Upload of $rel failed after $uploaded file(s): $(Get-CurlError $lastRes). Re-run ./deploy/deploy.ps1 to resume from file $($uploaded + 1) (already-uploaded files are skipped automatically)." }
    $uploaded++
    "  uploaded $rel"
}
"Uploaded $uploaded of $totalToPublish file(s) to $remoteLabel."

# 3. Check the live site actually serves the new page.
$title = [regex]::Match((Get-Content -Raw (Join-Path $src 'index.html')), '<title>(.*?)</title>').Groups[1].Value
try {
    $live = Invoke-WebRequest -Uri $SiteUrl -UseBasicParsing -TimeoutSec 20 -Headers @{ 'Cache-Control' = 'no-cache' }
    if ($title -and $live.Content -match [regex]::Escape($title)) { "Live check: $SiteUrl responds ($($live.StatusCode)) and shows '$title'." }
    else { "Live check: $SiteUrl responds ($($live.StatusCode)) but doesn't show '$title' yet. It may be cached, or the upload folder may be wrong." }
}
catch { "Live check: couldn't load $SiteUrl ($($_.Exception.Message)). The upload finished; check the site in a browser." }
