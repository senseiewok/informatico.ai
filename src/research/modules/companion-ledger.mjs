/**
 * @module companion-ledger
 * Portable AI-agnostic SKILL.md Blob download & clipboard copy + Living Edition revision switcher.
 * Strictly zero .innerHTML.
 */
export function initCompanionAndLedger(scope = document) {
  // 1. Living Edition & Frontier Council Revision Switcher
  scope.querySelectorAll(".tp-rev-btn[data-rev-summary]").forEach((btn) => {
    if (btn.dataset.bound === "true") return;
    btn.dataset.bound = "true";
    btn.addEventListener("click", () => {
      const ledger = btn.closest(".tp-rev-ledger");
      if (!ledger) return;
      ledger.querySelectorAll(".tp-rev-btn").forEach((b) => {
        b.setAttribute("aria-pressed", "false");
      });
      btn.setAttribute("aria-pressed", "true");
      const sumEl = ledger.querySelector("[data-rev-summary-out]");
      const opusEl = ledger.querySelector("[data-rev-opus-out]");
      if (sumEl) sumEl.textContent = btn.getAttribute("data-rev-summary") || "";
      if (opusEl) opusEl.textContent = btn.getAttribute("data-rev-opus") || "";
    });
  });

  // 2. Portable AI-Agnostic SKILL.md Download
  scope.querySelectorAll("[data-skill-download]").forEach((btn) => {
    if (btn.dataset.bound === "true") return;
    btn.dataset.bound = "true";
    btn.addEventListener("click", () => {
      const box = btn.closest(".tp-skill-box");
      if (!box) return;
      const srcEl = box.querySelector("[data-skill-source]");
      if (!srcEl) return;
      const fname = btn.getAttribute("data-skill-download") || "SKILL.md";
      const blob = new Blob([srcEl.textContent.trim() + "\n"], {
        type: "text/markdown;charset=utf-8",
      });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = fname;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  });

  // 3. Portable AI-Agnostic SKILL.md Clipboard Copy
  scope.querySelectorAll("[data-skill-copy]").forEach((btn) => {
    if (btn.dataset.bound === "true") return;
    btn.dataset.bound = "true";
    btn.addEventListener("click", () => {
      const box = btn.closest(".tp-skill-box");
      if (!box) return;
      const srcEl = box.querySelector("[data-skill-source]");
      if (!srcEl) return;
      const orig = btn.textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(srcEl.textContent.trim() + "\n").then(() => {
          btn.textContent = "Copied SKILL.md";
          setTimeout(() => {
            btn.textContent = orig;
          }, 1800);
        });
      }
    });
  });

  // 4. Standalone Zero-Dependency Python Verifier Tool (.py) Download
  scope.querySelectorAll("[data-py-download]").forEach((btn) => {
    if (btn.dataset.bound === "true") return;
    btn.dataset.bound = "true";
    btn.addEventListener("click", () => {
      const box = btn.closest(".tp-skill-box");
      if (!box) return;
      const pyEl = box.querySelector("[data-py-source]");
      if (!pyEl) return;
      const fname = btn.getAttribute("data-py-download") || "verify_folio.py";
      const blob = new Blob([pyEl.textContent.trim() + "\n"], {
        type: "text/x-python;charset=utf-8",
      });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = fname;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  });

  // 5. Live Telemetry & Scite Grounding JSON Packet Copy (for AI Agents & Engineering Pipelines)
  scope.querySelectorAll("[data-telemetry-copy]").forEach((btn) => {
    if (btn.dataset.bound === "true") return;
    btn.dataset.bound = "true";
    btn.addEventListener("click", () => {
      const mount = btn.closest("#tp-folio-mount") || document;
      const folioId = btn.getAttribute("data-telemetry-copy") || "FOLIO";
      const sliders = {};
      mount.querySelectorAll('.tp-plate input[type="range"]').forEach((inp) => {
        sliders[inp.id || "param"] = parseFloat(inp.value);
      });
      const readouts = {};
      mount.querySelectorAll(".tp-readout-box").forEach((ro) => {
        const k = ro.querySelector(".tp-readout-k");
        const v = ro.querySelector(".tp-readout-v");
        if (k && v) readouts[k.textContent.trim()] = v.textContent.trim();
      });
      const activeLensBtn = mount.querySelector('.tp-lens-btn[aria-pressed="true"]');
      const packet = {
        folio_id: folioId,
        active_lens: activeLensBtn ? activeLensBtn.textContent.trim() : "1 · 3D Surface",
        parameters: sliders,
        readouts,
        exported_at: new Date().toISOString(),
      };
      const orig = btn.textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(JSON.stringify(packet, null, 2) + "\n").then(() => {
          btn.textContent = "Copied Telemetry JSON";
          setTimeout(() => {
            btn.textContent = orig;
          }, 1800);
        });
      }
    });
  });
}
