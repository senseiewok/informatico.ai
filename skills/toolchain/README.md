# Portable AI Agent Skills — Tech & Tools · The Toolbox (`X.01`–`X.06`)

Each folder (`x01/` through `x06/`) contains:
1. **`SKILL.md`**: Cross-provider AI agent skill (`Claude Code`, `GitHub Copilot`, `Cursor`, `Antigravity`, `Qwen3-Coder`, `Ollama`) with YAML frontmatter and `security-runtime` guardrails.
2. **`make_<slug>.py`**: Deterministic Python 3 stdlib generator (the primary source of truth) that writes the neutral `.glb`, `.step`, `.3mf`, `.dxf`, and `manifest.json` files into `src/toolchain/<slug>/files/`.
3. **`verify_<slug>_*.py`**: Byte-level Python 3 stdlib verifier with `--planted-defect` falsification knockout.

## Quick Verification

```bash
# Run all 6 generators, byte-level verifiers, and claim gates in one command (< 1s):
python toolchain/run_all_toolchain.py

# Or run an individual generator + verifier + planted-defect knockout:
python skills/toolchain/x01/make_x01.py
python skills/toolchain/x01/verify_x01_toolchain_x01_glb_inspector_validator.py
python skills/toolchain/x01/verify_x01_toolchain_x01_glb_inspector_validator.py --planted-defect
```

## Skill Index

| Skill Folder | Skill Name | Folio Title | Primary Formats | Verifier Script |
| :--- | :--- | :--- | :--- | :--- |
| `skills/toolchain/x01/` | `toolchain-x01-glb-inspector-validator` | `X.01` · Zero-Build WebGL2 GLB Inspector & Byte-Level 2-Manifold Geometry Verifier | `.glb`, `.step`, `.3mf` | `verify_x01_toolchain_x01_glb_inspector_validator.py` |
| `skills/toolchain/x02/` | `toolchain-x02-parametric-step-3mf-roundtrip` | `X.02` · Code-First Parametric Solids & Measured STEP AP242, 3MF, and GLB Round-Trip Fidelity | `.step`, `.3mf`, `.glb` | `verify_x02_toolchain_x02_parametric_step_3mf_roundtrip.py` |
| `skills/toolchain/x03/` | `toolchain-x03-small-architect-vault-kit` | `X.03` · The Small Architecture Studio's Vault, Timber & Reciprocal Frame Kit: Equilibrium to Open CAD | `.glb`, `.step`, `.3mf`, `.dxf` | `verify_x03_toolchain_x03_small_architect_vault_kit.py` |
| `skills/toolchain/x04/` | `toolchain-x04-miura-ori-dxf-fabricator` | `X.04` · Miura-Ori Deployable Solar Screens: From 3D Folding Kinematics (GLB) to Flat-Pattern DXF | `.glb`, `.3mf`, `.dxf` | `verify_x04_toolchain_x04_miura_ori_dxf_fabricator.py` |
| `skills/toolchain/x05/` | `toolchain-x05-simp-manifold-3mf` | `X.05` · Topology-Optimized Structural Struts to Watertight 3MF & Build-Plate Overhang Audit | `.3mf`, `.glb`, `.step` | `verify_x05_toolchain_x05_simp_manifold_3mf.py` |
| `skills/toolchain/x06/` | `toolchain-x06-topological-metamaterial-cell` | `X.06` · Sub-Wavelength Acoustic & Topological Metamaterial Unit Cells: Genus $g = 1$ & Betti-Number Verification | `.glb`, `.3mf`, `.step` | `verify_x06_toolchain_x06_topological_metamaterial_cell.py` |
