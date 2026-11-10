# -*- coding: utf-8 -*-
"""Essay ES.02 — Derived, Not Measured (`tools/folios/essays/e02_derived_not_measured.py`).

Pure-Python stdlib epistemic lattice kernel, three-absence quantitative probes, 8-mutant
falsification harness, and bilingual (EN / es-MX) long-form essay specification.
"""
from __future__ import annotations

import copy
from decimal import Decimal, InvalidOperation
import math
import re

G_NEWTON = 6.67430e-11
HBAR = 1.054571817e-34

EPISTEMIC_LABELS: tuple[str, ...] = (
    "MEASURED",
    "DERIVED (NOT MEASURED)",
    "BOUND",
    "SINGLE RESULT",
    "PROPOSED",
    "OPEN",
)

LABEL_RANK: dict[str, int] = {
    "MEASURED": 5,
    "DERIVED (NOT MEASURED)": 4,
    "BOUND": 4,
    "SINGLE RESULT": 3,
    "PROPOSED": 2,
    "OPEN": 1,
}

REPLICATION_WINDOW_MONTHS = 24
KINDS: tuple[str, ...] = ("peer-reviewed", "preprint", "review", "press")

_SUB_SUP_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻₀₁₂₃₄₅₆₇₈₉", "0123456789-0123456789")
_NUM_RE = re.compile(r"(?<![A-Za-z])[-−]?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-−+]?\d+)?")


def extract_number_tokens(text: str) -> list[str]:
    """Extract normalized numeric tokens from prose or table cells for bilingual parity checks."""
    norm = text.translate(_SUB_SUP_DIGITS).replace("−", "-")
    tokens: list[str] = []
    for match in _NUM_RE.finditer(norm):
        raw = match.group(0).replace(",", "")
        try:
            tokens.append(format(Decimal(raw).normalize(), "f"))
        except InvalidOperation:
            tokens.append(raw)
    return sorted(tokens)


def compute_bmv_derived_witness(
    mass_kg: float = 1.0e-14,
    sep_m: float = 450.0e-6,
    split_m: float = 250.0e-6,
    hold_s: float = 2.5,
) -> dict:
    """Compute the 2017 Bose-Marletto-Vedral four-branch Newtonian phase and Wootters concurrence.

    Demonstrates the distinction between deductive accuracy (closed form vs reduced-state purity
    agreeing within 10^-12 from parent row T05-WESTPHAL2021) and empirical observation (no
    micron-mass spatial superposition interferometer has been built: phenomenon stays PROPOSED).
    """
    d_ll = sep_m
    d_rr = sep_m
    d_lr = sep_m + split_m
    d_rl = sep_m - split_m
    pref = G_NEWTON * (mass_kg ** 2) * hold_s / HBAR
    phi_ll = pref / d_ll
    phi_rr = pref / d_rr
    phi_lr = pref / d_lr
    phi_rl = pref / d_rl
    delta_phi = phi_lr + phi_rl - phi_ll - phi_rr

    concurrence_closed = abs(math.sin(0.5 * delta_phi))

    # Independent calculation from reduced single-qubit state rho_A = Tr_B(|Psi><Psi|)
    # |Psi> = 0.5 * (e^{i phi_LL}|00> + e^{i phi_LR}|01> + e^{i phi_RL}|10> + e^{i phi_RR}|11>)
    psi_00 = complex(math.cos(phi_ll), math.sin(phi_ll)) * 0.5
    psi_01 = complex(math.cos(phi_lr), math.sin(phi_lr)) * 0.5
    psi_10 = complex(math.cos(phi_rl), math.sin(phi_rl)) * 0.5
    psi_11 = complex(math.cos(phi_rr), math.sin(phi_rr)) * 0.5

    rho_00 = (abs(psi_00) ** 2) + (abs(psi_01) ** 2)
    rho_11 = (abs(psi_10) ** 2) + (abs(psi_11) ** 2)
    rho_01 = psi_00 * psi_10.conjugate() + psi_01 * psi_11.conjugate()
    tr_rho_a_sq = (rho_00 ** 2) + (rho_11 ** 2) + 2.0 * (abs(rho_01) ** 2)
    concurrence_purity = math.sqrt(max(0.0, 2.0 * (1.0 - tr_rho_a_sq)))

    return {
        "mass_kg": mass_kg,
        "sep_m": sep_m,
        "split_m": split_m,
        "hold_s": hold_s,
        "delta_phi_rad": delta_phi,
        "concurrence_closed": concurrence_closed,
        "concurrence_purity": concurrence_purity,
        "purity_agreement_abs_diff": abs(concurrence_closed - concurrence_purity),
        "phenomenon_label": "PROPOSED",
        "calculation_label": "DERIVED (NOT MEASURED)",
        "measured_parent_id": "T05-WESTPHAL2021",
    }


def compute_smeared_recast_probe() -> dict:
    """Evaluate the smeared-gravity hybrid pair kernel erf(r / (2 * sigma)) and T.05 recast checkpoints."""
    r_probe_m = 52.0e-6
    ratio_sigma_tiny = math.erf(r_probe_m / (2.0 * 1.0e-12))
    ratio_sigma_33um = math.erf(r_probe_m / (2.0 * 33.0e-6))
    ratio_sigma_75um = math.erf(r_probe_m / (2.0 * 75.0e-6))

    # Checkpoints from the T.05 Fourier-Bessel recast against Lee et al. (2020) Table 11.4:
    at_33um = {
        "sigma_um": 33.0,
        "alpha_eff": -7.3,
        "alpha95_minus_limit": -7.4,
        "excluded_95": -7.3 < -7.4,
    }
    at_35um = {
        "sigma_um": 35.0,
        "alpha_eff": -10.2,
        "alpha95_minus_limit": -7.4,
        "excluded_95": -10.2 < -7.4,
    }
    return {
        "r_probe_m": r_probe_m,
        "newton_limit_ratio": ratio_sigma_tiny,
        "pair_ratio_at_33um": ratio_sigma_33um,
        "pair_ratio_at_75um": ratio_sigma_75um,
        "wedge_120fold_deficit_75um_pct": 17.0,
        "yukawa_edge_38p6um_deficit_pct": 2.5,
        "sigma_95_limit_um": 33.0,
        "at_33um": at_33um,
        "at_35um": at_35um,
        "calculation_label": "DERIVED (NOT MEASURED)",
        "measured_parent_id": "T05-LEE2020",
    }


def audit_cryoem_coordinate_absence() -> dict:
    """Verify the structural-biology coordinate provenance distinction across four human CFTR Cryo-EM maps."""
    structures = [
        {
            "pdb": "5UAK",
            "year": 2017,
            "doi": "10.1016/j.cell.2017.02.024",
            "genotype": "WT",
            "residue_508": "RESOLVED_PHE508",
            "r_domain_unmodeled_residues_approx": 200,
            "r_domain_status": "UNRESOLVED_CONFORMATIONAL_SMEARING",
            "r_domain_epistemic_label": "OPEN",
        },
        {
            "pdb": "5W81",
            "year": 2017,
            "doi": "10.1016/j.cell.2017.06.041",
            "genotype": "WT",
            "residue_508": "RESOLVED_PHE508",
            "r_domain_unmodeled_residues_approx": 200,
            "r_domain_status": "UNRESOLVED_CONFORMATIONAL_SMEARING",
            "r_domain_epistemic_label": "OPEN",
        },
        {
            "pdb": "6MSM",
            "year": 2018,
            "doi": "10.1073/pnas.1815287115",
            "genotype": "WT_E1371Q",
            "residue_508": "RESOLVED_PHE508",
            "r_domain_unmodeled_residues_approx": 200,
            "r_domain_status": "UNRESOLVED_CONFORMATIONAL_SMEARING",
            "r_domain_epistemic_label": "OPEN",
        },
        {
            "pdb": "8EIQ",
            "year": 2022,
            "doi": "10.1126/science.ade2216",
            "genotype": "DELTA_F508",
            "residue_508": "GENETICALLY_DELETED",
            "r_domain_unmodeled_residues_approx": 200,
            "r_domain_status": "UNRESOLVED_CONFORMATIONAL_SMEARING",
            "r_domain_epistemic_label": "OPEN",
        },
    ]
    wt_508_resolved = all(
        s["residue_508"] == "RESOLVED_PHE508" for s in structures if s["pdb"] in ("5UAK", "5W81", "6MSM")
    )
    df508_deleted = next(s for s in structures if s["pdb"] == "8EIQ")["residue_508"] == "GENETICALLY_DELETED"
    all_four_r_domain_open = len(structures) == 4 and all(
        s["r_domain_status"] == "UNRESOLVED_CONFORMATIONAL_SMEARING"
        and s["r_domain_epistemic_label"] == "OPEN"
        for s in structures
    )
    return {
        "structures": structures,
        "wt_508_resolved": wt_508_resolved,
        "df508_genetically_deleted": df508_deleted,
        "all_four_r_domain_open": all_four_r_domain_open,
    }


DEFAULT_EPISTEMIC_BENCHMARK: dict = {
    "rows": [
        {
            "id": "T05-LEE2020",
            "label": "MEASURED",
            "kind": "peer-reviewed",
            "age_months": 78,
            "collaboration": "Eot-Wash (University of Washington)",
            "doi": "10.1103/physrevlett.124.101101",
            "is_positive_detection": True,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 42,
            "scite_contrasting": 1,
            "contrasting_audit": "",
        },
        {
            "id": "T05-TAN2020",
            "label": "MEASURED",
            "kind": "peer-reviewed",
            "age_months": 81,
            "collaboration": "HUST (Wuhan)",
            "doi": "10.1103/physrevlett.124.051301",
            "is_positive_detection": True,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 35,
            "scite_contrasting": 0,
            "contrasting_audit": "",
        },
        {
            "id": "T05-WESTPHAL2021",
            "label": "MEASURED",
            "kind": "peer-reviewed",
            "age_months": 68,
            "collaboration": "Vienna (Aspelmeyer group)",
            "doi": "10.1038/s41586-021-03250-7",
            "is_positive_detection": True,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 58,
            "scite_contrasting": 1,
            "contrasting_audit": "",
        },
        {
            "id": "T05-WOOTTERS1998",
            "label": "DERIVED (NOT MEASURED)",
            "kind": "peer-reviewed",
            "age_months": 340,
            "collaboration": "Wootters (Williams College)",
            "doi": "10.1103/physrevlett.80.2245",
            "is_positive_detection": False,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 210,
            "scite_contrasting": 0,
            "contrasting_audit": "",
        },
        {
            "id": "T05-LEE2021",
            "label": "DERIVED (NOT MEASURED)",
            "kind": "peer-reviewed",
            "age_months": 64,
            "collaboration": "Eot-Wash Fourier-Bessel formalism",
            "doi": "10.1088/1361-6382/abebf2",
            "is_positive_detection": False,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 8,
            "scite_contrasting": 0,
            "contrasting_audit": "",
        },
        {
            "id": "T06-DONADI2021",
            "label": "BOUND",
            "kind": "peer-reviewed",
            "age_months": 70,
            "collaboration": "LNGS Gran Sasso",
            "doi": "10.1038/s41567-020-1008-4",
            "is_positive_detection": False,
            "is_exclusion_bound": True,
            "coordinate_resolved": True,
            "scite_supporting": 31,
            "scite_contrasting": 2,
            "contrasting_audit": "",
        },
        {
            "id": "T06-XENONNT2026",
            "label": "SINGLE RESULT",
            "kind": "peer-reviewed",
            "age_months": 8,
            "collaboration": "XENONnT Collaboration",
            "doi": "10.1103/2jm3-4976",
            "is_positive_detection": False,
            "is_exclusion_bound": True,
            "coordinate_resolved": True,
            "scite_supporting": 3,
            "scite_contrasting": 0,
            "contrasting_audit": "",
        },
        {
            "id": "T05-BOSE2017",
            "label": "PROPOSED",
            "kind": "peer-reviewed",
            "age_months": 107,
            "collaboration": "Bose et al. QGEM proposal",
            "doi": "10.1103/physrevlett.119.240401",
            "is_positive_detection": False,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 94,
            "scite_contrasting": 6,
            "contrasting_audit": "",
        },
        {
            "id": "T05-TILLOY2016",
            "label": "PROPOSED",
            "kind": "peer-reviewed",
            "age_months": 118,
            "collaboration": "Tilloy & Diosi hybrid model",
            "doi": "10.1103/physrevd.93.024026",
            "is_positive_detection": False,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 4,
            "scite_contrasting": 9,
            "contrasting_audit": (
                "Audited (AH-8/AH-12): contrasting citations challenge hybrid classical-channel "
                "heating and short-range bounds; row stays capped at PROPOSED."
            ),
        },
        {
            "id": "T05-DIOSI2025",
            "label": "PROPOSED",
            "kind": "preprint",
            "age_months": 12,
            "collaboration": "Diosi arXiv rebuttal",
            "doi": "10.48550/arXiv.2511.00852",
            "is_positive_detection": False,
            "is_exclusion_bound": False,
            "coordinate_resolved": True,
            "scite_supporting": 0,
            "scite_contrasting": 0,
            "contrasting_audit": "",
        },
        {
            "id": "STR-CRYOEM-RDOM",
            "label": "OPEN",
            "kind": "peer-reviewed",
            "age_months": 48,
            "collaboration": "Cryo-EM CFTR structures (5UAK/5W81/6MSM/8EIQ)",
            "doi": "10.1126/science.ade2216",
            "is_positive_detection": False,
            "is_exclusion_bound": False,
            "coordinate_resolved": False,
            "scite_supporting": 19,
            "scite_contrasting": 0,
            "contrasting_audit": "",
        },
    ],
    "claims": [
        {
            "id": "CLM-01-ISL",
            "label": "MEASURED",
            "row_ids": ["T05-LEE2020", "T05-TAN2020", "T05-WESTPHAL2021"],
            "parent_id": None,
            "en": "Newtonian 1/r^2 attraction holds down to 52 um across 2 torsion-balance collaborations and 90 mg gold spheres at 400 um.",
            "es": "La atracción newtoniana 1/r^2 se cumple hasta 52 um en 2 colaboraciones de balanza de torsión y esferas de oro de 90 mg a 400 um.",
        },
        {
            "id": "CLM-02-BMV-CONCURRENCE",
            "label": "DERIVED (NOT MEASURED)",
            "row_ids": ["T05-WESTPHAL2021", "T05-WOOTTERS1998", "T05-BOSE2017"],
            "parent_id": "T05-WESTPHAL2021",
            "en": "Feeding Newtonian coupling into the 2017 10^-14 kg geometry yields phase 0.31 rad and Wootters concurrence 0.16 to 10^-12.",
            "es": "Al alimentar el acoplamiento newtoniano en la geometría de 2017 de 10^-14 kg se obtiene fase 0.31 rad y concurrencia de Wootters 0.16 a 10^-12.",
        },
        {
            "id": "CLM-03-SMEARED-RECAST",
            "label": "DERIVED (NOT MEASURED)",
            "row_ids": ["T05-LEE2020", "T05-LEE2021"],
            "parent_id": "T05-LEE2020",
            "en": "Projecting erf(r / 2*sigma) / r onto the 2020 52 um wedge limits gives alpha_eff = -7.3 at 33 um vs -7.4 and -10.2 at 35 um, excluding sigma > 33 um at 95 %.",
            "es": "Al proyectar erf(r / 2*sigma) / r sobre los límites de cuñas de 2020 a 52 um resulta alpha_eff = -7.3 a 33 um frente a -7.4 y -10.2 a 35 um, excluyendo sigma > 33 um al 95 %.",
        },
        {
            "id": "CLM-04-DP-BOUND",
            "label": "BOUND",
            "row_ids": ["T06-DONADI2021"],
            "parent_id": None,
            "en": "Underground germanium counting in 2021 observed 0 excess X-ray bursts, setting a lower bound on R0 that rules out parameter-free collapse.",
            "es": "El conteo subterráneo en germanio en 2021 observó 0 ráfagas de rayos X en exceso, fijando una cota inferior sobre R0 que descarta el colapso sin parámetros.",
        },
        {
            "id": "CLM-05-XENONNT-YOUNG",
            "label": "SINGLE RESULT",
            "row_ids": ["T06-XENONNT2026"],
            "parent_id": None,
            "en": "The 2026 XENONnT 1 to 140 keV electronic-recoil run tightens collapse limits by a factor of 5 within 1 collaboration inside the 24-month window.",
            "es": "La corrida de retroceso electrónico de 1 a 140 keV de XENONnT en 2026 estrecha los límites de colapso por un factor de 5 en 1 colaboración dentro de la ventana de 24 meses.",
        },
        {
            "id": "CLM-06-BMV-WITNESS",
            "label": "PROPOSED",
            "row_ids": ["T05-BOSE2017", "T05-TILLOY2016", "T05-DIOSI2025"],
            "parent_id": None,
            "en": "Holding two 10^-14 kg masses in spatial superposition for 2.5 s remains an unbuilt witness proposal, and 2025 preprints stay capped at PROPOSED.",
            "es": "Sostener dos masas de 10^-14 kg en superposición espacial por 2.5 s sigue siendo una propuesta de testigo no construida, y las prepublicaciones de 2025 quedan acotadas en PROPUESTO.",
        },
        {
            "id": "CLM-07-CRYOEM-RDOM",
            "label": "OPEN",
            "row_ids": ["STR-CRYOEM-RDOM"],
            "parent_id": None,
            "en": "Across 4 Cryo-EM maps, roughly 200 disordered R-domain residues remain unresolved by conformational motion while residue 508 is resolved in 5UAK and 6MSM and deleted in 8EIQ.",
            "es": "En 4 mapas Cryo-EM, cerca de 200 residuos desordenados del dominio R permanecen sin resolver por movimiento conformacional mientras el residuo 508 está resuelto en 5UAK y 6MSM y delecionado en 8EIQ.",
        },
    ],
}


def evaluate_epistemic_lattice(benchmark: dict, relax_rule: str | None = None) -> dict:
    """Validate ledger rows and claim spans against the 6-label epistemic lattice contract.

    `relax_rule` is used ONLY by `--planted-defect` to verify that relaxing an epistemic rule
    allows a planted mutant to survive and triggers a deterministic test failure.
    """
    errors: list[str] = []
    rows_by_id: dict[str, dict] = {}

    for row in benchmark.get("rows", []):
        rid = row["id"]
        label = row["label"]
        kind = row["kind"]
        if label not in EPISTEMIC_LABELS:
            errors.append(f"row {rid}: invalid label {label!r}")
            continue
        if kind not in KINDS:
            errors.append(f"row {rid}: invalid kind {kind!r}")
        if kind == "press":
            errors.append(f"row {rid}: press source cannot enter epistemic ledger")
        if kind == "preprint" and relax_rule != "allow_preprint_measured":
            if LABEL_RANK[label] > LABEL_RANK["PROPOSED"]:
                errors.append(f"row {rid}: preprint promoted to {label!r} above PROPOSED cap")
        if row.get("coordinate_resolved") is False and LABEL_RANK[label] > LABEL_RANK["OPEN"]:
            errors.append(f"row {rid}: unresolved coordinate promoted to {label!r} above OPEN")
        if int(row.get("scite_contrasting", 0)) > int(row.get("scite_supporting", 0)):
            audit = str(row.get("contrasting_audit") or "").strip()
            if len(audit) < 20:
                errors.append(
                    f"row {rid}: Scite contrasting ({row['scite_contrasting']}) > supporting "
                    f"({row['scite_supporting']}) without >=20-char contrasting_audit note"
                )
        rows_by_id[rid] = row

    for claim in benchmark.get("claims", []):
        cid = claim["id"]
        clabel = claim["label"]
        if clabel not in EPISTEMIC_LABELS:
            errors.append(f"claim {cid}: invalid label {clabel!r}")
            continue
        cited_ids = claim.get("row_ids") or []
        if not cited_ids:
            errors.append(f"claim {cid}: empty row_ids")
            continue
        cited: list[dict] = []
        for rid in cited_ids:
            if rid not in rows_by_id:
                errors.append(f"claim {cid}: unknown ledger row {rid}")
            else:
                cited.append(rows_by_id[rid])
        if not cited:
            continue

        # Rule: Bilingual numeric parity
        en_nums = extract_number_tokens(claim["en"])
        es_nums = extract_number_tokens(claim["es"])
        if en_nums != es_nums:
            errors.append(f"claim {cid}: EN/es-MX numeric drift {en_nums} != {es_nums}")

        # Rule: Preprints cannot back claims above PROPOSED unless mature peer-reviewed rows carry the rank
        mature_pr = [
            r for r in cited
            if r["kind"] == "peer-reviewed" and int(r["age_months"]) >= REPLICATION_WINDOW_MONTHS
        ]

        if clabel == "MEASURED":
            if any(r.get("coordinate_resolved") is False for r in cited):
                errors.append(f"claim {cid}: unresolved coordinate interpolated as MEASURED")
            if any(r.get("is_exclusion_bound") and not r.get("is_positive_detection") for r in cited):
                if not any(r.get("is_positive_detection") for r in mature_pr):
                    errors.append(f"claim {cid}: exclusion BOUND misread as positive MEASURED detection")
            qualifying = [
                r for r in mature_pr
                if r["label"] == "MEASURED"
                and r.get("is_positive_detection") is True
                and r.get("coordinate_resolved") is not False
            ]
            collabs = {r["collaboration"] for r in qualifying}
            min_collabs = 1 if relax_rule == "allow_single_collab_measured" else 2
            if len(collabs) < min_collabs:
                errors.append(
                    f"claim {cid}: MEASURED requires >= {min_collabs} mature independent collaborations "
                    f"(found {len(collabs)})"
                )

        elif clabel == "DERIVED (NOT MEASURED)":
            parent_id = claim.get("parent_id")
            if not parent_id:
                errors.append(f"claim {cid}: DERIVED (NOT MEASURED) missing required parent_id")
            elif parent_id not in rows_by_id:
                errors.append(f"claim {cid}: parent_id {parent_id} not in ledger")
            else:
                prow = rows_by_id[parent_id]
                if parent_id not in cited_ids:
                    errors.append(f"claim {cid}: parent_id {parent_id} must also appear in row_ids")
                if relax_rule != "allow_proposed_parent":
                    if prow["label"] != "MEASURED":
                        errors.append(
                            f"claim {cid}: parent_id {parent_id} has label {prow['label']!r}, expected 'MEASURED'"
                        )
                    elif prow["kind"] != "peer-reviewed" or int(prow["age_months"]) < REPLICATION_WINDOW_MONTHS:
                        errors.append(f"claim {cid}: parent_id {parent_id} must be mature peer-reviewed MEASURED")
                deriv_rows = [
                    r for r in mature_pr
                    if r["id"] != parent_id and LABEL_RANK[r["label"]] >= LABEL_RANK["DERIVED (NOT MEASURED)"]
                ]
                if not deriv_rows:
                    errors.append(f"claim {cid}: DERIVED (NOT MEASURED) requires a mature derivation row")

        elif clabel == "BOUND":
            if not any(r["label"] == "BOUND" and r.get("is_exclusion_bound") for r in mature_pr):
                errors.append(f"claim {cid}: BOUND requires a mature peer-reviewed exclusion-limit row")

        elif clabel == "SINGLE RESULT":
            if not any(
                r["kind"] == "peer-reviewed"
                and LABEL_RANK[r["label"]] >= LABEL_RANK["SINGLE RESULT"]
                and r.get("coordinate_resolved") is not False
                for r in cited
            ):
                errors.append(f"claim {cid}: SINGLE RESULT requires a peer-reviewed resolved row")

    return {"valid": len(errors) == 0, "error_count": len(errors), "errors": errors}


def run_epistemic_mutations(
    benchmark: dict | None = None,
    planted_defect: bool = False,
) -> dict:
    """Execute 8 deterministic epistemic corruption mutants and compute exact mutation-kill recall."""
    base = copy.deepcopy(benchmark if benchmark is not None else DEFAULT_EPISTEMIC_BENCHMARK)
    relax = "allow_proposed_parent" if planted_defect else None
    baseline = evaluate_epistemic_lattice(base, relax_rule=relax)

    def _mutate_m1(b: dict) -> None:
        for r in b["rows"]:
            if r["id"] == "T05-DIOSI2025":
                r["label"] = "MEASURED"

    def _mutate_m2(b: dict) -> None:
        for c in b["claims"]:
            if c["id"] == "CLM-02-BMV-CONCURRENCE":
                c["parent_id"] = None

    def _mutate_m3(b: dict) -> None:
        for c in b["claims"]:
            if c["id"] == "CLM-02-BMV-CONCURRENCE":
                c["parent_id"] = "T05-BOSE2017"

    def _mutate_m4(b: dict) -> None:
        for c in b["claims"]:
            if c["id"] == "CLM-05-XENONNT-YOUNG":
                c["label"] = "MEASURED"

    def _mutate_m5(b: dict) -> None:
        for c in b["claims"]:
            if c["id"] == "CLM-07-CRYOEM-RDOM":
                c["label"] = "MEASURED"

    def _mutate_m6(b: dict) -> None:
        for c in b["claims"]:
            if c["id"] == "CLM-04-DP-BOUND":
                c["label"] = "MEASURED"

    def _mutate_m7(b: dict) -> None:
        for c in b["claims"]:
            if c["id"] == "CLM-02-BMV-CONCURRENCE":
                c["es"] = c["es"].replace("0.31 rad", "0.39 rad")

    def _mutate_m8(b: dict) -> None:
        for r in b["rows"]:
            if r["id"] == "T05-TILLOY2016":
                r["contrasting_audit"] = ""

    specs = [
        ("M1_PREPRINT_TO_MEASURED", "Preprint promoted above PROPOSED cap to MEASURED", _mutate_m1),
        ("M2_DERIVED_MISSING_PARENT", "DERIVED (NOT MEASURED) claim stripped of its parent_id", _mutate_m2),
        ("M3_DERIVED_PROPOSED_PARENT", "DERIVED (NOT MEASURED) claim re-pointed to a PROPOSED parent row", _mutate_m3),
        ("M4_SINGLE_GROUP_TO_MEASURED", "Single-collaboration young result (<24 months) promoted to MEASURED", _mutate_m4),
        ("M5_UNRESOLVED_INTERPOLATED_AS_MEASURED", "Unresolved Cryo-EM R-domain coordinates interpolated as MEASURED", _mutate_m5),
        ("M6_EXCLUSION_BOUND_AS_DETECTION", "Null-excess exclusion BOUND misread as positive MEASURED detection", _mutate_m6),
        ("M7_BILINGUAL_NUMERIC_DRIFT", "Spanish twin drifts from 0.31 rad to 0.39 rad", _mutate_m7),
        ("M8_UNAUDITED_CONTRASTING_DOMINANCE", "Scite contrasting > supporting row missing >=20-char audit note", _mutate_m8),
    ]

    results: list[dict] = []
    killed_count = 0
    for mid, desc, fn in specs:
        mutated = copy.deepcopy(base)
        fn(mutated)
        verdict = evaluate_epistemic_lattice(mutated, relax_rule=relax)
        killed = not verdict["valid"]
        if killed:
            killed_count += 1
        results.append(
            {
                "id": mid,
                "description": desc,
                "killed": killed,
                "errors": verdict["errors"],
            }
        )

    return {
        "baseline_valid": baseline["valid"],
        "baseline_errors": baseline["errors"],
        "mutants_killed": killed_count,
        "mutants_total": len(specs),
        "recall": killed_count / float(len(specs)),
        "planted_defect_active": planted_defect,
        "mutants": results,
    }


ESSAY: dict = {
    "code": "ES.02",
    "slug": "derived-not-measured",
    "plate_slug": "essay02",
    "date": "2026-11-10",
    "seo": (
        "Derived, Not Measured: Six Evidence Labels",
        "Why machine-precision math deduced from a measured law is still not a measurement: six evidence labels, parent provenance, and eight mutation tests.",
        "Derivado, No Medido: Seis Etiquetas de Evidencia",
        "Por qué un cálculo exacto deducido de una ley medida aún no es una medición: seis etiquetas de evidencia, linaje de origen y ocho pruebas mutantes.",
    ),
    "kicker_en": "Essay ES.02 · Scientific Epistemology, Tabletop Gravity & Formal Provenance",
    "kicker_es": "Ensayo ES.02 · Epistemología Científica, Gravedad de Mesa y Linaje Formal",
    "reading_time_en": "13 min read",
    "reading_time_es": "13 min de lectura",
    "title_en": "Derived, Not Measured: Why Machine-Precision Math Never Substitutes for an Experiment",
    "title_es": "Derivado, No Medido: Por Qué un Cálculo Exacto Nunca Sustituye a un Experimento",
    "standfirst_en": (
        "A Python kernel can integrate two-qubit gravitational phases to 10^-12 and project a 2025 smeared-gravity "
        "potential onto 2020 Eöt-Wash torsion-balance limits down to 33 um without rounding error. None of that "
        "makes an unbuilt interferometer or an unrefitted time series a measurement. Here is how six evidence "
        "labels, a mandatory measured-parent edge, and 8 mutation tests keep deduction honest."
    ),
    "standfirst_es": (
        "Un kernel en Python puede integrar fases gravitatorias de dos qubits a 10^-12 y proyectar un potencial "
        "de gravedad suavizada de 2025 sobre los límites de balanza de torsión de Eöt-Wash de 2020 hasta 33 um sin "
        "error de redondeo. Nada de eso convierte un interferómetro no construido ni una serie temporal no reajustada "
        "en una medición. Así es como seis etiquetas de evidencia, una arista obligatoria hacia una fila madre medida "
        "y 8 pruebas mutantes mantienen honesta la deducción."
    ),
    "card_dek_en": (
        "Three kinds of scientific absence—unbuilt proposals, unresolved coordinates, and quantities derived from "
        "a measured parent—checked by an 8-mutant epistemic lattice."
    ),
    "card_dek_es": (
        "Tres tipos de ausencia científica—propuestas no construidas, coordenadas no resueltas y cantidades derivadas "
        "de una fila madre medida—verificadas por una retícula epistémica de 8 mutantes."
    ),
    "instrument_kind": "epistemic",
    "predict": {
        "question_en": (
            "Suppose a deterministic script combines Newton's gravitational constant measured between 90 mg gold "
            "spheres in 2021 with Wootters's 1998 concurrence theorem, computing concurrence 0.16 to 10^-12 for two "
            "10^-14 kg masses held for 2.5 s in an interferometer that no laboratory has yet built. Which label "
            "does that 0.16 earn?"
        ),
        "question_es": (
            "Supón que un script determinista combina la constante gravitatoria de Newton medida entre esferas de "
            "oro de 90 mg en 2021 con el teorema de concurrencia de Wootters de 1998, calculando una concurrencia de "
            "0.16 a 10^-12 para dos masas de 10^-14 kg sostenidas durante 2.5 s en un interferómetro que ningún "
            "laboratorio ha construido todavía. ¿Qué etiqueta merece ese 0.16?"
        ),
        "choices": [
            {
                "id": "a",
                "en": "DERIVED (NOT MEASURED), tied to its 2021 MEASURED parent row while the unbuilt interferometer stays PROPOSED",
                "es": "DERIVADO (NO MEDIDO), ligado a su fila madre MEDIDA de 2021 mientras el interferómetro no construido permanece en PROPUESTO",
            },
            {
                "id": "b",
                "en": "MEASURED, because both the 2021 gravitational constant and the 10^-12 numerical check are verified",
                "es": "MEDIDO, porque tanto la constante gravitatoria de 2021 como la verificación numérica a 10^-12 están comprobadas",
            },
        ],
        "answer": "a",
        "explain_en": (
            "Numerical precision audits the algebra, never the apparatus. Because the Newtonian pull was measured "
            "in 2021 at 90 mg while spatial superposition at 10^-14 kg for 2.5 s remains unbuilt, the computed 0.16 "
            "concurrence is DERIVED (NOT MEASURED) from its 2021 parent, and the witness experiment itself remains PROPOSED."
        ),
        "explain_es": (
            "La precisión numérica audita el álgebra, jamás el aparato. Como la atracción newtoniana se midió en "
            "2021 a 90 mg mientras la superposición espacial a 10^-14 kg por 2.5 s sigue sin construirse, la concurrencia "
            "calculada de 0.16 es DERIVADO (NO MEDIDO) desde su fila madre de 2021, y el experimento testigo permanece en PROPUESTO."
        ),
    },
    "sections": [
        {
            "id": "twelve-digit-illusion",
            "h2_en": "I · The Twelve-Digit Illusion: Accuracy Is Not Observation",
            "h2_es": "I · La Ilusión de los Doce Dígitos: Exactitud No Es Observación",
            "short_en": "I · Twelve Digits",
            "short_es": "I · Doce Dígitos",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Open the entanglement kernel behind step T.05 of Time & Gravity and feed it the geometry "
                        "published by Sougato Bose and colleagues in 2017 (DOI 10.1103/physrevlett.119.240401): two "
                        "diamagnetic microcrystals of 10^-14 kg each, trap centers separated by 450 um, each mass "
                        "coherently split across 250 um, falling in vacuum at 10^-15 Pa and 0.15 K for 2.5 s. Under "
                        "Newtonian attraction, the four spatial branches—left-left at 450 um, right-right at 450 um, "
                        "left-right at 700 um, and right-left at 200 um—accumulate slightly different quantum phases "
                        "phi = G m^2 t / (hbar d). Subtract the symmetric pair from the asymmetric pair and the "
                        "entanglement phase comes out to Delta_phi = 0.31 rad. Pass that phase into William Wootters's "
                        "1998 two-qubit formula and the concurrence reads C = 0.16, rising to 1.00 if the drop could "
                        "be stretched to 25.0 s."
                    ),
                    "es": (
                        "Abre el kernel de entrelazamiento detrás del paso T.05 de Tiempo y Gravedad y aliméntalo con "
                        "la geometría publicada por Sougato Bose y colegas en 2017 (DOI 10.1103/physrevlett.119.240401): "
                        "dos microcristales diamagnéticos de 10^-14 kg cada uno, centros de trampa separados por 450 um, "
                        "cada masa dividida coherentemente a lo largo de 250 um, cayendo en vacío a 10^-15 Pa y 0.15 K "
                        "durante 2.5 s. Bajo atracción newtoniana, las cuatro ramas espaciales—izquierda-izquierda a "
                        "450 um, derecha-derecha a 450 um, izquierda-derecha a 700 um y derecha-izquierda a 200 um—"
                        "acumulan fases cuánticas ligeramente distintas phi = G m^2 t / (hbar d). Al restar el par "
                        "simétrico del asimétrico, la fase de entrelazamiento resulta en Delta_phi = 0.31 rad. Pasa esa "
                        "fase por la fórmula de dos qubits de William Wootters de 1998 y la concurrencia marca C = 0.16, "
                        "subiendo a 1.00 si la caída pudiera extenderse a 25.0 s."
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Four-Branch Newtonian Phase & Wootters Concurrence",
                    "label_es": "Fase Newtoniana de Cuatro Ramas y Concurrencia de Wootters",
                    "formula": "Delta_phi = phi_LR + phi_RL - phi_LL - phi_RR = 0.31 rad   ==>   C = |sin(Delta_phi / 2)| = 0.16",
                    "note_en": (
                        "Closed form |sin(Delta_phi / 2)| = 0.16 vs reduced-state purity sqrt(2 * (1 - Tr rho_A^2)) "
                        "verified to 10^-12 from MEASURED parent row T05-WESTPHAL2021; the 10^-14 kg interferometer remains unbuilt (PROPOSED)."
                    ),
                    "note_es": (
                        "Forma cerrada |sin(Delta_phi / 2)| = 0.16 frente a pureza reducida sqrt(2 * (1 - Tr rho_A^2)) "
                        "verificada a 10^-12 desde la fila madre MEDIDA T05-WESTPHAL2021; el interferómetro de 10^-14 kg sigue sin construirse (PROPUESTO)."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "To guard against coding mistakes, the verifier computes that same 0.16 a second way: it "
                        "constructs the full 4-branch pure state, traces out crystal B in complex arithmetic, computes "
                        "the purity Tr(rho_A^2) of crystal A's 2x2 reduced density matrix, and checks that the two "
                        "routes agree within 1 part in 10^12. Here is where both hurried technical journalism and "
                        "large language models routinely stumble. Seeing a peer-reviewed 2017 Physical Review Letters "
                        "DOI, a measured 2021 gravitational constant from 90 mg gold spheres at 400 um surface gap "
                        "(Tobias Westphal et al., DOI 10.1038/s41586-021-03250-7), and a deterministic script printing "
                        "PASS at 10^-12, an automated summary will confidently write that gravity entangles micron "
                        "crystals with concurrence 0.16. Every digit in that sentence is algebraically unimpeachable, "
                        "and the sentence as physics is false."
                    ),
                    "es": (
                        "Para blindarse contra errores de código, el verificador calcula ese mismo 0.16 por una segunda "
                        "vía: construye el estado puro completo de 4 ramas, traza el cristal B en aritmética compleja, "
                        "evalúa la pureza Tr(rho_A^2) de la matriz de densidad reducida 2x2 del cristal A y comprueba "
                        "que ambas rutas coinciden dentro de 1 parte en 10^12. Aquí es donde tanto el periodismo "
                        "técnico apresurado como los modelos de lenguaje suelen tropezar. Al ver un DOI arbitrado de "
                        "2017 en Physical Review Letters, una constante gravitatoria medida en 2021 con esferas de oro "
                        "de 90 mg a 400 um entre superficies (Tobias Westphal et al., DOI 10.1038/s41586-021-03250-7) "
                        "y un script determinista que imprime PASS a 10^-12, un resumen automático escribirá con "
                        "aplomo que la gravedad entrelaza cristales micrométricos con concurrencia 0.16. Cada dígito "
                        "en esa oración es algebraicamente impecable, y la oración como física es falsa."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "That distinction matters more each year as scientific papers ship alongside executable "
                        "notebooks, symbolic algebra scripts, and automated synthesis pipelines. A deterministic "
                        "program guarantees reproducibility of inference: anyone who runs the same code on the same "
                        "inputs recovers the identical floating-point value. Yet reproducibility of code is orthogonal "
                        "to empirical realization in hardware, and conflating the two silently erases the laboratory."
                    ),
                    "es": (
                        "Esa distinción importa más cada año conforme los artículos científicos se publican junto con "
                        "cuadernos ejecutables, scripts de álgebra simbólica y flujos de síntesis automatizada. Un "
                        "programa determinista garantiza la reproducibilidad de la inferencia: cualquiera que corra el "
                        "mismo código sobre las mismas entradas recupera idéntico valor en punto flotante. Pero la "
                        "reproducibilidad del código es ortogonal a la realización empírica en hardware, y confundirlas "
                        "borra silenciosamente al laboratorio."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "In Plain Words · Extra-Easy Explanation",
                    "kicker_es": "En Palabras Sencillas · Explicación Extra Fácil",
                    "title_en": "Twelve decimal places audit the calculator, never the vacuum chamber",
                    "title_es": "Doce decimales auditan la calculadora, jamás la cámara de vacío",
                    "paras": [
                        (
                            "Checking a calculation to 12 decimal places proves that your calculator did not slip; it "
                            "never proves that nature obeyed the setup you typed in. In 1960 Robert Pound and Glen Rebka "
                            "measured gravitational time dilation over a 22.5 m tower, and in 2021 Vienna measured "
                            "Newtonian pull between two 90 mg gold spheres. Using those real measurements to predict what "
                            "two 10^-14 kg specks would do in a 2.5 s quantum drop is honest deduction, but until someone "
                            "actually drops the specks in 10^-15 Pa vacuum without a stray gas atom spoiling the fringes, "
                            "nobody has measured the entanglement.",
                            "Comprobar un cálculo hasta 12 decimales demuestra que la calculadora no resbaló; jamás "
                            "demuestra que la naturaleza siguió el montaje que escribiste. En 1960 Robert Pound y Glen Rebka "
                            "midieron la dilatación gravitatoria del tiempo en una torre de 22.5 m, y en 2021 Viena midió "
                            "la atracción newtoniana entre dos esferas de oro de 90 mg. Usar esas mediciones reales para "
                            "predecir qué harían dos motas de 10^-14 kg en una caída cuántica de 2.5 s es deducción honesta, "
                            "pero hasta que alguien deje caer esas motas en un vacío de 10^-15 Pa sin que un átomo residual "
                            "arruine las franjas, nadie ha medido el entrelazamiento.",
                        )
                    ],
                },
            ],
        },
        {
            "id": "three-kinds-of-absence",
            "h2_en": "II · Three Kinds of Absence: Unbuilt, Unresolved, and Derived",
            "h2_es": "II · Tres Tipos de Ausencia: No Construido, No Resuelto y Derivado",
            "short_en": "II · Three Absences",
            "short_es": "II · Tres Ausencias",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Scientific prose goes blurry whenever it uses a single hedge word—'estimated', 'modeled', or "
                        "'predicted'—to cover radically different reasons why a direct detector reading does not exist. "
                        "Across computational physics and structural biology, there are 3 distinct kinds of empirical "
                        "absence, and each carries a different obligation to reality. The first absence is an unbuilt "
                        "or unobserved phenomenon, which our ledger caps at PROPOSED. Neither the 2017 Bose–Marletto–Vedral "
                        "interferometer at 10^-14 kg nor the 2025 theoretical counter-arguments by Joseph Aziz and "
                        "Richard Howl (DOI 10.1038/s41586-025-09595-7) or Sebastián Trillo and Miguel Navascués "
                        "(DOI 10.1103/physrevd.111.l121101) represent laboratory observations; they are competing "
                        "mathematical proposals about what classical or quantum fields would do if the apparatus existed."
                    ),
                    "es": (
                        "La prosa científica se vuelve borrosa cada vez que usa una sola palabra ambigua—'estimado', "
                        "'modelado' o 'predicho'—para cubrir razones radicalmente distintas por las cuales no existe "
                        "una lectura directa del detector. Entre la física computacional y la biología estructural hay "
                        "3 tipos distintos de ausencia empírica, y cada uno impone una obligación diferente ante la "
                        "realidad. La primera ausencia es un fenómeno no construido o no observado, que nuestro registro "
                        "acota en PROPUESTO. Ni el interferómetro de Bose–Marletto–Vedral de 2017 a 10^-14 kg ni los "
                        "contraargumentos teóricos de 2025 de Joseph Aziz y Richard Howl (DOI 10.1038/s41586-025-09595-7) "
                        "o Sebastián Trillo y Miguel Navascués (DOI 10.1103/physrevd.111.l121101) representan "
                        "observaciones de laboratorio; son propuestas matemáticas rivales sobre lo que harían campos "
                        "clásicos o cuánticos si el aparato existiera."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "The second kind of absence is physically present in the specimen yet experimentally unresolved "
                        "(OPEN). This rule entered our engineering practice before Time & Gravity existed, while "
                        "auditing structural coordinate files in Cystic Fibrosis ion-channel research. Examine the 4 "
                        "landmark human CFTR Cryo-EM coordinate maps: dephosphorylated wild-type 5UAK (Fei Liu et al. "
                        "2017, DOI 10.1016/j.cell.2017.02.024), phosphorylated ATP-bound 5W81 (Zhenmei Zhang et al. "
                        "2017) and 6MSM (Zhang et al. 2018, DOI 10.1073/pnas.1815287115), and modulator-bound DeltaF508 "
                        "structure 8EIQ (Karol Fiedorczuk & Jue Chen 2022, DOI 10.1126/science.ade2216). In wild-type "
                        "5UAK, 5W81, and 6MSM, residue Phe508 is clearly resolved inside nucleotide-binding domain 1, "
                        "whereas 8EIQ lacks residue 508 because the DeltaF508 genotype genetically deletes that single "
                        "phenylalanine from the polypeptide chain. By contrast, the roughly 200-residue disordered "
                        "regulatory R-domain is physically tethered inside every intact channel in the vitrified ice, "
                        "yet all 4 Cryo-EM structures leave those 200 residues unmodeled in atomic coordinates because "
                        "conformational flexibility smears out the electron density. Structural biologists refuse to "
                        "invent atomic coordinates where density blurs; teaching AI verifiers never to hallucinate "
                        "smooth splines across those 200 unresolved residues—and never to confuse 8EIQ's genetic "
                        "deletion at position 508 with Cryo-EM motion smearing—forged our strict separation between "
                        "what an instrument resolved and what software inferred."
                    ),
                    "es": (
                        "El segundo tipo de ausencia está físicamente presente en la muestra pero experimentalmente "
                        "sin resolver (ABIERTO). Esta regla entró en nuestra práctica de ingeniería antes de que "
                        "existiera Tiempo y Gravedad, al auditar archivos de coordenadas estructurales en investigación "
                        "del canal iónico de fibrosis quística. Examina los 4 mapas seminales Cryo-EM de CFTR humano: "
                        "el tipo silvestre desfosforilado 5UAK (Fei Liu et al. 2017, DOI 10.1016/j.cell.2017.02.024), "
                        "las estructuras fosforiladas unidas a ATP 5W81 (Zhenmei Zhang et al. 2017) y 6MSM (Zhang et al. "
                        "2018, DOI 10.1073/pnas.1815287115), y la estructura DeltaF508 con moduladores 8EIQ (Karol "
                        "Fiedorczuk y Jue Chen 2022, DOI 10.1126/science.ade2216). En los mapas de tipo silvestre 5UAK, "
                        "5W81 y 6MSM, el residuo Phe508 está claramente resuelto dentro del dominio de unión a "
                        "nucleótidos 1, mientras que 8EIQ carece del residuo 508 porque el genotipo DeltaF508 deleciona "
                        "genéticamente esa fenilalanina de la cadena polipeptídica. En cambio, el dominio regulador R "
                        "desordenado de unos 200 residuos está físicamente unido dentro de cada canal intacto en el "
                        "hielo vitrificado, pero las 4 estructuras Cryo-EM dejan esos 200 residuos sin modelar en "
                        "coordenadas atómicas porque la flexibilidad conformacional difumina la densidad electrónica. "
                        "Los biólogos estructurales se niegan a inventar coordenadas atómicas donde la densidad se "
                        "borra; enseñar a los verificadores de IA a jamás alucinar curvas suaves sobre esos 200 residuos "
                        "no resueltos—y a nunca confundir la deleción genética en la posición 508 de 8EIQ con el "
                        "difuminado por movimiento en Cryo-EM—forjó nuestra separación estricta entre lo resuelto por "
                        "un instrumento y lo inferido por software."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "The third kind of absence is neither an unbuilt dream nor a blurred micrograph: it is a "
                        "quantity deduced with mathematical rigor from a real, peer-reviewed measurement when the "
                        "target configuration itself has not been directly observed. Suppose we take Vienna's 2021 "
                        "measurement of Newtonian gravity between two 90 mg gold spheres at 400 um surface separation "
                        "and combine it with quantum mechanics to compute the 0.31 rad phase of two 10^-14 kg crystals, "
                        "or take Seattle's 2020 torsion-balance Yukawa table down to 52 um and project a 2025 "
                        "error-function potential onto those 66 published wavelength rows. Calling those calculations "
                        "PROPOSED would understate their empirical anchor, because a real pendulum already constrained "
                        "the force law; calling them MEASURED would overstate what occurred in the room, because no "
                        "sensor ever recorded that observable directly. Naming this third category DERIVED (NOT MEASURED) "
                        "and requiring an explicit link to its MEASURED parent row resolves the dilemma cleanly."
                    ),
                    "es": (
                        "El tercer tipo de ausencia no es un sueño sin construir ni una micrografía borrosa: es una "
                        "cantidad deducida con rigor matemático a partir de una medición real arbitrada cuando la "
                        "configuración objetivo aún no se ha observado directamente. Supongamos que tomamos la medición "
                        "vienesa de 2021 de la gravedad newtoniana entre dos esferas de oro de 90 mg a 400 um entre "
                        "superficies y la combinamos con la mecánica cuántica para calcular la fase de 0.31 rad de dos "
                        "cristales de 10^-14 kg, o tomamos la tabla de Yukawa de 2020 en Seattle hasta 52 um y "
                        "proyectamos un potencial de función error de 2025 sobre esas 66 filas publicadas. Llamar "
                        "PROPUESTO a esos cálculos subestimaría su ancla empírica, pues un péndulo real ya acotó la ley "
                        "de fuerza; llamarlos MEDIDO exageraría lo ocurrido en el laboratorio, pues ningún sensor "
                        "registró jamás ese observable de forma directa. Nombrar esta tercera categoría DERIVADO (NO "
                        "MEDIDO) y exigir un vínculo explícito hacia su fila madre MEDIDA resuelve el dilema con limpieza."
                    ),
                },
                {
                    "type": "analogy",
                    "kicker_en": "Everyday Analogy · Three Blank Spots on a Canyon Map",
                    "kicker_es": "Analogía Cotidiana · Tres Espacios en Blanco en el Mapa de un Cañón",
                    "title_en": "A penciled bridge, a fog-hidden gorge floor, and an arch calculated from a granite monument",
                    "title_es": "Un puente a lápiz, un barranco oculto por niebla y un arco calculado desde un banco de granito",
                    "paras": [
                        (
                            "Picture a civil surveyor's topographic sheet of a river gorge. A brass benchmark stamped "
                            "1,420.00 m in solid granite by 2 independent survey crews is MEASURED. A proposed footbridge "
                            "sketched in pencil across the rim has 0 bolts in the rock: that is PROPOSED. A mist-filled "
                            "chasm floor where laser rangefinders scatter off river spray is real rock hidden by fog, left "
                            "honestly blank on the sheet: that is OPEN and unresolved. Finally, the steel arch stress "
                            "computed to 6 significant figures from the 1,420.00 m granite benchmark and Euler-Bernoulli "
                            "beam theory is neither fog nor fantasy—it is DERIVED (NOT MEASURED), trustworthy precisely "
                            "because it points back to the brass monument.",
                            "Imagina el plano topográfico de un cañón fluvial trazado por un ingeniero. Un banco de nivel "
                            "de latón grabado a 1,420.00 m en granito sólido por 2 brigadas independientes es MEDIDO. Un "
                            "puente peatonal dibujado a lápiz de borde a borde tiene 0 pernos en la roca: eso es PROPUESTO. "
                            "El fondo del barranco cubierto de niebla donde el láser se dispersa en la bruma es roca real "
                            "oculta, dejada honestamente en blanco en el plano: eso es ABIERTO y no resuelto. Finalmente, "
                            "el esfuerzo del arco de acero calculado con 6 cifras significativas a partir del banco de "
                            "granito de 1,420.00 m y la teoría de vigas de Euler-Bernoulli no es niebla ni fantasía: es "
                            "DERIVADO (NO MEDIDO), confiable precisamente porque apunta de vuelta al monumento de latón.",
                        )
                    ],
                },
            ],
        },
        {
            "id": "parent-provenance-recast",
            "h2_en": "III · The Recast Discipline: Why Every Derived Claim Needs a Measured Parent",
            "h2_es": "III · La Disciplina del Recast: Por Qué Todo Cálculo Derivado Exige una Fila Madre Medida",
            "short_en": "III · Parent Provenance",
            "short_es": "III · Fila Madre",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "The third kind of absence—a number rigorously deduced from a measured dataset under a new "
                        "kernel that the original experimenters never fitted—came into sharp focus during the 2025 "
                        "tabletop-gravity dispute. In Physical Review D in 2025, Trillo and Navascués integrated the "
                        "Tilloy–Diósi hybrid master equation, in which gravity remains classical at the price of "
                        "smearing Newton's point-mass potential over a regularization length sigma into "
                        "V(r) = -G m_1 m_2 erf(r / (2 * sigma)) / r. In their geometry of 10^-15 kg spheres separated "
                        "by 24 um with a 23 um split, that hybrid dynamics generates entanglement only below "
                        "0.8508 * sigma, requiring sigma above 55 um (and they plotted curves at sigma = 75 um, "
                        "100 um, and 250 um). A natural physicist's question immediately follows: if gravity is "
                        "weakened by erf(r / (2 * sigma)) at tens of micrometres, what would have happened inside the "
                        "2020 Eöt-Wash short-range torsion balance?"
                    ),
                    "es": (
                        "El tercer tipo de ausencia—un número deducido con rigor desde datos medidos bajo un nuevo "
                        "kernel que los experimentadores originales jamás ajustaron—cobró plena nitidez durante la "
                        "disputa de gravedad de mesa de 2025. En Physical Review D en 2025, Trillo y Navascués "
                        "integraron la ecuación maestra híbrida de Tilloy–Diósi, donde la gravedad sigue siendo clásica "
                        "a cambio de suavizar el potencial newtoniano en una longitud de regularización sigma según "
                        "V(r) = -G m_1 m_2 erf(r / (2 * sigma)) / r. En su geometría de esferas de 10^-15 kg separadas "
                        "por 24 um con división de 23 um, esa dinámica híbrida genera entrelazamiento solo por debajo "
                        "de 0.8508 * sigma, exigiendo sigma mayor a 55 um (y graficaron curvas en sigma = 75 um, "
                        "100 um y 250 um). Una pregunta física inmediata surge al instante: si la gravedad se debilita "
                        "por erf(r / (2 * sigma)) a decenas de micrómetros, ¿qué habría ocurrido dentro de la balanza "
                        "de torsión de corto alcance de Eöt-Wash en 2020?"
                    ),
                },
                {
                    "type": "equation",
                    "label_en": "Fourier–Bessel Recast of Smeared Gravity onto Eöt-Wash 2020",
                    "label_es": "Recast de Fourier–Bessel de Gravedad Suavizada sobre Eöt-Wash 2020",
                    "formula": "V_smeared(r) = -G m_1 m_2 erf(r / 2*sigma) / r   ==>   sigma = 33 um: alpha_eff = -7.3 > -7.4  |  sigma = 35 um: alpha_eff = -10.2 < -7.4",
                    "note_en": (
                        "Projected onto T05-LEE2020 across 52 um to 3.0 mm: at 33 um, alpha_eff = -7.3 stays inside the "
                        "signed 95 % limit -7.4; at 35 um, alpha_eff = -10.2 crosses -7.4, excluding sigma > 33 um at 95 %."
                    ),
                    "note_es": (
                        "Proyectado sobre T05-LEE2020 entre 52 um y 3.0 mm: a 33 um, alpha_eff = -7.3 queda dentro del "
                        "límite con signo al 95 % de -7.4; a 35 um, alpha_eff = -10.2 cruza -7.4, excluyendo sigma > 33 um al 95 %."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "In 2020 Junyi Lee, Eric Adelberger, Blayne Heckel, and colleagues at the University of "
                        "Washington measured gravitational torque between 120-fold and 18-fold platinum wedge rings "
                        "from 52 um out to 3.0 mm, limiting any gravitational-strength Yukawa term to ranges below "
                        "38.6 um at 95 % confidence (T05-LEE2020, DOI 10.1103/physrevlett.124.101101). Using the "
                        "collaboration's own 2021 Fourier–Bessel expansion, our wedge kernel evaluates the smeared "
                        "potential across those exact 54 um and 99 um foils: at 52 um, sigma = 75 um removes 17.0 % "
                        "of the 120-fold Newtonian torque, whereas the Yukawa potential at the published 38.6 um edge "
                        "removes only 2.5 %. Projecting the smeared torque deficit across 52 um to 3.0 mm onto the "
                        "66 signed 95 % Yukawa limits tabulated in Lee's 2020 dissertation yields an effective strength "
                        "alpha_eff = -7.3 against the published signed limit -7.4 at sigma = 33 um, and alpha_eff = -10.2 "
                        "against -7.4 at sigma = 35 um—excluding sigma > 33 um at 95 % confidence across 4 separation "
                        "grids and both harmonics."
                    ),
                    "es": (
                        "En 2020 Junyi Lee, Eric Adelberger, Blayne Heckel y colegas en la Universidad de Washington "
                        "midieron el par gravitatorio entre anillos de platino de 120 y 18 cuñas desde 52 um hasta "
                        "3.0 mm, limitando cualquier término de Yukawa de intensidad gravitatoria a alcances menores de "
                        "38.6 um al 95 % de confianza (T05-LEE2020, DOI 10.1103/physrevlett.124.101101). Usando la "
                        "propia expansión de Fourier–Bessel de la colaboración de 2021, nuestro kernel de cuñas evalúa "
                        "el potencial suavizado sobre esas láminas exactas de 54 um y 99 um: a 52 um, sigma = 75 um "
                        "elimina el 17.0 % del par newtoniano de 120 pliegues, mientras que el potencial de Yukawa en "
                        "el borde publicado de 38.6 um quita solo el 2.5 %. Al proyectar el déficit de par suavizado "
                        "entre 52 um y 3.0 mm sobre los 66 límites de Yukawa con signo al 95 % tabulados en la tesis "
                        "de Lee de 2020, se obtiene alpha_eff = -7.3 frente al límite con signo publicado de -7.4 en "
                        "sigma = 33 um, y alpha_eff = -10.2 frente a -7.4 en sigma = 35 um—excluyendo sigma > 33 um al "
                        "95 % de confianza en 4 mallas de separación y ambos armónicos."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Why must that sigma > 33 um exclusion wear the badge DERIVED (NOT MEASURED) with an explicit "
                        "data-tg-parent pointer to T05-LEE2020 rather than MEASURED or a standalone BOUND? Because "
                        "the Eöt-Wash team fitted Yukawa exponentials exp(-r / lambda) to their 95 private torsion "
                        "runs, never the error-function kernel erf(r / (2 * sigma)). By contrast, when Sandro Donadi "
                        "and colleagues operated an underground high-purity germanium detector at Gran Sasso in 2021 "
                        "(DOI 10.1038/s41567-020-1008-4) and recorded 0 excess spontaneous X-ray bursts to rule out "
                        "parameter-free Diósi–Penrose collapse, that collaboration analyzed its own raw pulse shapes "
                        "against that exact kernel, earning BOUND. And when the XENONnT Collaboration published its "
                        "1 to 140 keV electronic-recoil collapse search in 2026 (Elena Aprile et al., "
                        "DOI 10.1103/2jm3-4976), tightening Diósi–Penrose limits by a factor of 5, our 24-month "
                        "replication clock holds that young 1-collaboration run at SINGLE RESULT until independent "
                        "time-projection chambers cross-check it."
                    ),
                    "es": (
                        "¿Por qué esa exclusión de sigma > 33 um debe portar la insignia DERIVADO (NO MEDIDO) con un "
                        "puntero explícito data-tg-parent hacia T05-LEE2020 en lugar de MEDIDO o una COTA autónoma? "
                        "Porque el equipo de Eöt-Wash ajustó exponenciales de Yukawa exp(-r / lambda) a sus 95 corridas "
                        "privadas de torsión, jamás el kernel de función error erf(r / (2 * sigma)). En contraste, "
                        "cuando Sandro Donadi y colegas operaron un detector subterráneo de germanio de alta pureza en "
                        "Gran Sasso en 2021 (DOI 10.1038/s41567-020-1008-4) y registraron 0 ráfagas espontáneas de "
                        "rayos X en exceso para descartar el colapso de Diósi–Penrose sin parámetros, esa colaboración "
                        "analizó sus propios pulsos crudos frente a ese kernel exacto, ganando COTA. Y cuando la "
                        "Colaboración XENONnT publicó su búsqueda de colapso por retroceso electrónico de 1 a 140 keV "
                        "en 2026 (Elena Aprile et al., DOI 10.1103/2jm3-4976), estrechando los límites de Diósi–Penrose "
                        "por un factor de 5, nuestro reloj de replicación de 24 meses mantiene esa corrida joven de 1 "
                        "colaboración en RESULTADO ÚNICO hasta que cámaras independientes la verifiquen."
                    ),
                },
            ],
        },
        {
            "id": "epistemic-partial-order",
            "h2_en": "IV · A Partial Order, Not a Ladder: Formal Types and Citation Polarity",
            "h2_es": "IV · Un Orden Parcial, No una Escalera: Tipos Formales y Polaridad de Citas",
            "short_en": "IV · Epistemic Lattice",
            "short_es": "IV · Retícula Epistémica",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "Treat the 6 labels not as a beauty contest from 1 to 6, but as a typed partial order modeled "
                        "on formal proof assistants. When the mathlib community formalized mathematics in Lean in 2020 "
                        "(DOI 10.1145/3372885.3373824) and Joseph Tooby-Smith digitalized high-energy physics theorems "
                        "in HepLean in 2025 (DOI 10.1016/j.cpc.2024.109457), every proved lemma carried its exact "
                        "hypotheses inside its type signature. If you prove theorem B assuming axiom A, Lean's kernel "
                        "verifies the implication A -> B with zero hand-waving, yet running #print axioms never lets "
                        "you pretend A vanished. In Time & Gravity, data-tg-parent is that exact type-theoretic "
                        "dependency edge: DERIVED (NOT MEASURED) certifies the implication from a mature MEASURED "
                        "parent row while refusing to mint synthetic empirical data."
                    ),
                    "es": (
                        "Trata las 6 etiquetas no como un concurso de prestigio del 1 al 6, sino como un orden parcial "
                        "tipado inspirado en los asistentes formales de demostración. Cuando la comunidad de mathlib "
                        "formalizó matemáticas en Lean en 2020 (DOI 10.1145/3372885.3373824) y Joseph Tooby-Smith "
                        "digitalizó teoremas de física de altas energías en HepLean en 2025 (DOI 10.1016/j.cpc.2024.109457), "
                        "cada lema demostrado conservó sus hipótesis exactas dentro de su firma de tipos. Si demuestras "
                        "el teorema B asumiendo el axioma A, el kernel de Lean verifica la implicación A -> B sin "
                        "ambigüedades, pero ejecutar #print axioms jamás permite fingir que A desapareció. En Tiempo y "
                        "Gravedad, data-tg-parent es exactamente esa arista de dependencia de tipos: DERIVADO (NO MEDIDO) "
                        "certifica la implicación desde una fila madre MEDIDA madura negándose a fabricar datos empíricos."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Type-checking internal deduction must also be paired with auditing external scientific "
                        "disagreement. A paper can hold a valid Crossref DOI and still face sharp technical refutations "
                        "in subsequent letters. Drawing on Josh Nicholson and colleagues' 2021 smart-citation "
                        "classification architecture in Scite (DOI 10.1162/qss_a_00146), our ledger lint inspects "
                        "supporting versus contrasting citation counts for every cached DOI. Whenever contrasting "
                        "citation statements exceed supporting ones—as happens on hybrid classical-gravity channels "
                        "challenged by short-range heating bounds—the build fails unless the ledger row carries a "
                        "human-written contrasting_audit scope note of at least 20 characters explaining what remains "
                        "disputed and capping the claim appropriately."
                    ),
                    "es": (
                        "La verificación de tipos sobre la deducción interna también debe emparejarse con la auditoría "
                        "del desacuerdo científico externo. Un artículo puede tener un DOI válido en Crossref y aun así "
                        "enfrentar refutaciones técnicas directas en cartas posteriores. Siguiendo la arquitectura de "
                        "clasificación inteligente de citas publicada por Josh Nicholson y colegas en 2021 con Scite "
                        "(DOI 10.1162/qss_a_00146), nuestro verificador del registro inspecciona los conteos de citas "
                        "de apoyo frente a citas contrastantes para cada DOI en caché. Siempre que los enunciados "
                        "contrastantes superan a los de apoyo—como ocurre en canales híbridos de gravedad clásica "
                        "cuestionados por cotas de calentamiento—la compilación falla salvo que la fila incluya una "
                        "nota contrasting_audit escrita por humanos de al menos 20 caracteres que acote la disputa."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "Notice why a partial order succeeds where a single numerical confidence score fails. Statistical "
                        "language models are trained to maximize next-token likelihood across millions of abstracts, a "
                        "training objective that naturally smooths away boundary conditions: a 95 % exclusion limit "
                        "(BOUND), a 1-group cryogenic run published 8 months ago (SINGLE RESULT), and a closed-form "
                        "integral evaluated to 10^-12 (DERIVED) get flattened into the same declarative verb tense. "
                        "In a partial order, BOUND and DERIVED (NOT MEASURED) sit side by side at rank 4 without "
                        "collapsing into each other. An exclusion bound rules out regions of parameter space where 0 "
                        "signal appeared above background; a derived quantity propagates equations forward from a "
                        "rank-5 MEASURED parent. Neither can be promoted to rank 5 by rhetorical polish or extra "
                        "decimal places—only a 2nd independent laboratory apparatus operating outside the 24-month "
                        "window can unlock MEASURED."
                    ),
                    "es": (
                        "Observa por qué un orden parcial triunfa donde fracasa un puntaje numérico único de confianza. "
                        "Los modelos estadísticos de lenguaje se entrenan para maximizar la verosimilitud del siguiente "
                        "token sobre millones de resúmenes, un objetivo que suaviza de forma natural las condiciones de "
                        "frontera: un límite de exclusión al 95 % (COTA), una corrida criogénica de 1 grupo publicada "
                        "hace 8 meses (RESULTADO ÚNICO) y una integral cerrada evaluada a 10^-12 (DERIVADO) terminan "
                        "aplanados en el mismo tiempo verbal declarativo. En un orden parcial, COTA y DERIVADO (NO "
                        "MEDIDO) conviven lado a lado en el rango 4 sin confundirse entre sí. Una cota de exclusión "
                        "descarta regiones de parámetros donde apareció 0 señal sobre el fondo; una cantidad derivada "
                        "propaga ecuaciones desde una fila madre MEDIDA de rango 5. Ninguna sube al rango 5 con retórica "
                        "ni con más decimales: solo un 2do aparato independiente fuera de la ventana de 24 meses "
                        "desbloquea MEDIDO."
                    ),
                },
                {
                    "type": "table",
                    "caption_en": "Table ES.02-1 · The 6-label epistemic lattice, replication gates, and provenance rules.",
                    "caption_es": "Tabla ES.02-1 · La retícula epistémica de 6 etiquetas, compuertas de replicación y reglas de linaje.",
                    "headers_en": ["Label", "Rank", "Minimum Gate", "Canonical Exemplar"],
                    "headers_es": ["Etiqueta", "Rango", "Compuerta Mínima", "Ejemplo Canónico"],
                    "rows": [
                        [
                            ("MEASURED", "MEDIDO"),
                            ("5", "5"),
                            (
                                ">= 2 peer-reviewed collaborations, >= 24 months old, positive resolved signal",
                                ">= 2 colaboraciones arbitradas, >= 24 meses de antigüedad, señal positiva resuelta",
                            ),
                            (
                                "Sub-mm 1/r^2 gravity down to 52 um (Lee 2020 + Tan 2020 + Westphal 2021)",
                                "Gravedad 1/r^2 submilimétrica hasta 52 um (Lee 2020 + Tan 2020 + Westphal 2021)",
                            ),
                        ],
                        [
                            ("DERIVED (NOT MEASURED)", "DERIVADO (NO MEDIDO)"),
                            ("4", "4"),
                            (
                                "Mandatory MEASURED parent row (>= 24 months) + peer-reviewed mathematical kernel",
                                "Fila madre MEDIDA obligatoria (>= 24 meses) + kernel matemático arbitrado",
                            ),
                            (
                                "Concurrence 0.16 from 2021 90 mg parent; smeared recast sigma > 33 um at 95 % from 2020 52 um parent",
                                "Concurrencia 0.16 desde fila madre de 90 mg de 2021; recast suavizado sigma > 33 um al 95 % desde fila madre de 52 um de 2020",
                            ),
                        ],
                        [
                            ("BOUND", "COTA"),
                            ("4", "4"),
                            (
                                ">= 1 peer-reviewed exclusion-limit row (>= 24 months); rules out parameter space only",
                                ">= 1 fila arbitrada de límite de exclusión (>= 24 meses); solo descarta espacio de parámetros",
                            ),
                            (
                                "Gran Sasso 2021 underground germanium 0-excess bound on spontaneous X-ray collapse",
                                "Cota subterránea en germanio de Gran Sasso 2021 con 0 exceso sobre colapso espontáneo en rayos X",
                            ),
                        ],
                        [
                            ("SINGLE RESULT", "RESULTADO ÚNICO"),
                            ("3", "3"),
                            (
                                "1 peer-reviewed collaboration or any peer-reviewed result < 24 months old",
                                "1 colaboración arbitrada o cualquier resultado arbitrado con < 24 meses de antigüedad",
                            ),
                            (
                                "XENONnT 2026 1 to 140 keV electronic-recoil collapse search (factor of 5 tightening)",
                                "Búsqueda de colapso por retroceso electrónico de 1 a 140 keV de XENONnT en 2026 (factor de 5)",
                            ),
                        ],
                        [
                            ("PROPOSED", "PROPUESTO"),
                            ("2", "2"),
                            (
                                "Unbuilt experimental witness, disputed young model, or any arXiv preprint (hard ceiling)",
                                "Testigo experimental no construido, modelo joven en disputa o prepublicación arXiv (techo estricto)",
                            ),
                            (
                                "Bose 2017 10^-14 kg 2.5 s interferometer; Aziz & Howl 2025; Trillo & Navascués 2025",
                                "Interferómetro de Bose 2017 de 10^-14 kg y 2.5 s; Aziz y Howl 2025; Trillo y Navascués 2025",
                            ),
                        ],
                        [
                            ("OPEN", "ABIERTO"),
                            ("1", "1"),
                            (
                                "Unsettled field question or physically present coordinate unresolved by the detector",
                                "Pregunta abierta del campo o coordenada físicamente presente no resuelta por el detector",
                            ),
                            (
                                "200 unmodeled flexible R-domain residues across 4 Cryo-EM maps (5UAK, 5W81, 6MSM, 8EIQ); T.05 channel dispute",
                                "200 residuos flexibles sin modelar del dominio R en 4 mapas Cryo-EM (5UAK, 5W81, 6MSM, 8EIQ); disputa de canales en T.05",
                            ),
                        ],
                    ],
                },
            ],
        },
        {
            "id": "eight-epistemic-mutations",
            "h2_en": "V · Testing the Guardrails: Eight Planted Epistemic Corruptions",
            "h2_es": "V · Probando las Barreras: Ocho Corrupciones Epistémicas Plantadas",
            "short_en": "V · Mutation Testing",
            "short_es": "V · Pruebas Mutantes",
            "blocks": [
                {
                    "type": "p",
                    "en": (
                        "A verifier that prints PASS on a curated repository proves very little until you try to fool "
                        "it. Borrowed from safety-critical compiler testing, mutation analysis measures whether a rule "
                        "suite actually kills plausible corruptions injected into the data. In the companion Python "
                        "module for this essay, run_epistemic_mutations() takes a clean 11-row, 7-claim benchmark "
                        "spanning tabletop gravity and structural coordinates and injects 8 targeted epistemic failures "
                        "one at a time: (1) promoting a 2025 arXiv preprint to MEASURED; (2) deleting parent_id from "
                        "the 0.16 concurrence derivation; (3) re-pointing that DERIVED (NOT MEASURED) claim from its "
                        "2021 90 mg MEASURED parent to the unbuilt 2017 PROPOSED witness; and (4) promoting the 2026 "
                        "1-collaboration XENONnT run inside the 24-month window to MEASURED."
                    ),
                    "es": (
                        "Un verificador que imprime PASS sobre un repositorio curado demuestra muy poco hasta que "
                        "intentas engañarlo. Tomado de las pruebas de compiladores críticos, el análisis de mutaciones "
                        "mide si un conjunto de reglas realmente elimina corrupciones plausibles inyectadas en los "
                        "datos. En el módulo compañero en Python de este ensayo, run_epistemic_mutations() toma un "
                        "banco limpio de 11 filas y 7 afirmaciones que abarca gravedad de mesa y coordenadas "
                        "estructurales e inyecta 8 fallas epistémicas dirigidas una por una: (1) promover una "
                        "prepublicación de arXiv de 2025 a MEDIDO; (2) borrar parent_id de la derivación de concurrencia "
                        "0.16; (3) redirigir esa afirmación DERIVADO (NO MEDIDO) desde su fila madre MEDIDA de 90 mg de "
                        "2021 hacia el testigo no construido PROPUESTO de 2017; y (4) promover la corrida de 1 "
                        "colaboración de XENONnT de 2026 dentro de la ventana de 24 meses a MEDIDO."
                    ),
                },
                {
                    "type": "p",
                    "en": (
                        "The remaining 4 mutations target subtler failure modes that routinely slip past human "
                        "copy-editing: (5) interpolating the 200 unresolved flexible R-domain residues from OPEN into "
                        "MEASURED coordinates; (6) misreading Gran Sasso's 2021 0-excess exclusion BOUND as a positive "
                        "MEASURED collapse detection; (7) introducing bilingual numeric drift so the Spanish twin "
                        "quotes 0.39 rad where English states 0.31 rad; and (8) erasing the 20-character "
                        "contrasting_audit scope note on a 2016 hybrid-gravity row where 9 contrasting Scite citations "
                        "outnumber 4 supporting ones. On a normal run, the lattice kills 8 of 8 mutants (recall 1.00); "
                        "invoking --planted-defect deliberately relaxes parent-provenance checking so mutant 3 survives "
                        "(7 of 8 killed) and forces a non-zero exit code."
                    ),
                    "es": (
                        "Las 4 mutaciones restantes apuntan a modos de falla más sutiles que suelen filtrarse en la "
                        "edición humana: (5) interpolar los 200 residuos flexibles sin resolver del dominio R de "
                        "ABIERTO a coordenadas MEDIDAS; (6) malinterpretar la COTA de exclusión de 0 exceso de Gran "
                        "Sasso en 2021 como una detección positiva MEDIDA de colapso; (7) introducir deriva numérica "
                        "bilingüe para que el gemelo en español cite 0.39 rad donde el inglés indica 0.31 rad; y (8) "
                        "borrar la nota de alcance contrasting_audit de 20 caracteres en una fila híbrida de 2016 donde "
                        "9 citas contrastantes en Scite superan a 4 de apoyo. En una corrida normal, la retícula "
                        "elimina 8 de 8 mutantes (exhaustividad 1.00); al invocar --planted-defect se relaja "
                        "deliberadamente la revisión de fila madre para que el mutante 3 sobreviva (7 de 8 eliminados) "
                        "y fuerce un código de salida distinto de cero."
                    ),
                },
                {
                    "type": "bridge",
                    "kicker_en": "In Plain Words · Testing the Smoke Alarm with Smoke",
                    "kicker_es": "En Palabras Sencillas · Probar la Alarma de Humo con Humo",
                    "title_en": "A verifier only earns trust when a planted lie makes it fail",
                    "title_es": "Un verificador solo merece confianza cuando una falla plantada lo detiene",
                    "paras": [
                        (
                            "A green indicator LED on a smoke detector only tells you the battery is connected; blowing "
                            "real test smoke into the chamber proves the sensor actually trips the siren. Passing "
                            "--planted-defect to every verifier on this site is that puff of test smoke. And keeping "
                            "DERIVED (NOT MEASURED) distinct from MEASURED protects a quiet human truth: AI agents and "
                            "Python scripts can check 10^-12 algebra in milliseconds, yet they never machine the platinum "
                            "wedges, shield the germanium crystal under 1,400 m of limestone, or coax 10^-14 kg into "
                            "quantum free fall.",
                            "Un foco verde en un detector de humo solo indica que la batería está conectada; soplar humo "
                            "real de prueba en la cámara demuestra que el sensor realmente activa la sirena. Pasar "
                            "--planted-defect a cada verificador de este sitio es esa bocanada de humo de prueba. Y "
                            "mantener DERIVADO (NO MEDIDO) separado de MEDIDO protege una verdad humana serena: los agentes "
                            "de IA y los scripts en Python pueden comprobar álgebra a 10^-12 en milisegundos, pero jamás "
                            "maquinan las cuñas de platino, ni blindan el cristal de germanio bajo 1,400 m de roca caliza, "
                            "ni sostienen 10^-14 kg en caída libre cuántica.",
                        )
                    ],
                },
            ],
        },
    ],
    "sidenotes": [
        {
            "label_en": "Note 01 · Why 10^-12 Is Easy and 10^-15 Pa Is Hard",
            "label_es": "Nota 01 · Por Qué 10^-12 Es Fácil y 10^-15 Pa Es Difícil",
            "en": (
                "Double-precision IEEE 754 arithmetic carries 53 significand bits (roughly 15 to 17 decimal digits), "
                "so agreeing to 10^-12 between Wootters's formula and reduced-state purity takes 20 lines of stdlib "
                "Python; holding 10^-14 kg at 10^-15 Pa and 0.15 K for 2.5 s has not yet been achieved in any laboratory."
            ),
            "es": (
                "La aritmética IEEE 754 de doble precisión porta 53 bits de mantisa (entre 15 y 17 dígitos decimales), "
                "así que coincidir a 10^-12 entre la fórmula de Wootters y la pureza reducida toma 20 líneas de Python "
                "estándar; sostener 10^-14 kg a 10^-15 Pa y 0.15 K durante 2.5 s aún no se ha logrado en ningún laboratorio."
            ),
        },
        {
            "label_en": "Note 02 · Deletion vs Motion in 5UAK, 6MSM, and 8EIQ",
            "label_es": "Nota 02 · Deleción frente a Movimiento en 5UAK, 6MSM y 8EIQ",
            "en": (
                "Wild-type Phe508 is resolved in 5UAK (2017) and 6MSM (2018) and absent in 8EIQ (2022) by genetic "
                "deletion, whereas roughly 200 flexible R-domain residues are physically present yet unmodeled across "
                "all 4 Cryo-EM structures rather than interpolated."
            ),
            "es": (
                "El residuo silvestre Phe508 está resuelto en 5UAK (2017) y 6MSM (2018) y ausente en 8EIQ (2022) por "
                "deleción genética, mientras que unos 200 residuos flexibles del dominio R están físicamente presentes "
                "pero sin modelar en las 4 estructuras Cryo-EM en vez de interpolarse."
            ),
        },
        {
            "label_en": "Note 03 · Recast vs Refit on Eöt-Wash 2020",
            "label_es": "Nota 03 · Recast frente a Reajuste en Eöt-Wash 2020",
            "en": (
                "A refit re-minimizes chi^2 on raw detector voltages; a recast projects a new kernel onto published "
                "limit tables (66 Yukawa ranges from 5 um to 8.9 mm, excluding sigma > 33 um at 95 % from parent T05-LEE2020)."
            ),
            "es": (
                "Un reajuste vuelve a minimizar chi^2 sobre voltajes crudos del detector; un recast proyecta un nuevo "
                "kernel sobre tablas de límites publicadas (66 alcances de Yukawa de 5 um a 8.9 mm, excluyendo sigma > 33 um al 95 % desde T05-LEE2020)."
            ),
        },
        {
            "label_en": "Note 04 · The 24-Month Replication Clock",
            "label_es": "Nota 04 · El Reloj de Replicación de 24 Meses",
            "en": (
                "Even peer-reviewed experiments published in 2025 or 2026 stay capped at SINGLE RESULT or PROPOSED "
                "until 24 months of independent scrutiny and a 2nd collaboration confirm the signal."
            ),
            "es": (
                "Incluso los experimentos arbitrados publicados en 2025 o 2026 permanecen acotados en RESULTADO ÚNICO o "
                "PROPUESTO hasta que 24 meses de escrutinio independiente y una 2da colaboración confirmen la señal."
            ),
        },
        {
            "label_en": "Note 05 · Lean Axioms and Scite Contrasting Audits",
            "label_es": "Nota 05 · Axiomas en Lean y Auditorías Contrastantes en Scite",
            "en": (
                "Just as Lean's #print axioms exposes every unproven assumption behind a theorem, our ledger requires "
                "a >= 20-character contrasting_audit note whenever Scite contrasting citations exceed supporting ones."
            ),
            "es": (
                "Así como #print axioms en Lean expone cada supuesto no demostrado detrás de un teorema, nuestro "
                "registro exige una nota contrasting_audit de >= 20 caracteres cuando las citas contrastantes en Scite superan a las de apoyo."
            ),
        },
    ],
    "sources": [
        {
            "id": "ES02-BOSE2017",
            "citation": "Bose, S. et al. Spin Entanglement Witness for Quantum Gravity. Phys. Rev. Lett. 119, 240401 (2017).",
            "doi": "10.1103/physrevlett.119.240401",
            "year": 2017,
            "role_en": "Unbuilt 10^-14 kg, 2.5 s spatial-superposition entanglement witness capped at PROPOSED.",
            "role_es": "Testigo de entrelazamiento no construido de 10^-14 kg y 2.5 s acotado en PROPUESTO.",
        },
        {
            "id": "ES02-LEE2020",
            "citation": "Lee, J. G., Adelberger, E. G., Cook, T. S., Fleischer, S. M. & Heckel, B. R. New Test of the Gravitational 1/r^2 Law at Separations down to 52 um. Phys. Rev. Lett. 124, 101101 (2020).",
            "doi": "10.1103/physrevlett.124.101101",
            "year": 2020,
            "role_en": "MEASURED 52 um torsion-balance parent row for the sigma > 33 um at 95 % smeared-gravity recast.",
            "role_es": "Fila madre MEDIDA de balanza de torsión a 52 um para el recast de gravedad suavizada sigma > 33 um al 95 %.",
        },
        {
            "id": "ES02-WESTPHAL2021",
            "citation": "Westphal, T., Hepach, H., Pfaff, J. & Aspelmeyer, M. Measurement of gravitational coupling between millimetre-sized masses. Nature 591, 225–228 (2021).",
            "doi": "10.1038/s41586-021-03250-7",
            "year": 2021,
            "role_en": "MEASURED 90 mg gold-sphere gravitational parent row for DERIVED (NOT MEASURED) concurrence 0.16.",
            "role_es": "Fila madre MEDIDA con esferas de oro de 90 mg para la concurrencia DERIVADO (NO MEDIDO) de 0.16.",
        },
        {
            "id": "ES02-DONADI2021",
            "citation": "Donadi, S. et al. Underground test of gravity-related wave function collapse. Nat. Phys. 17, 74–78 (2021).",
            "doi": "10.1038/s41567-020-1008-4",
            "year": 2021,
            "role_en": "Mature peer-reviewed underground germanium spontaneous-radiation exclusion BOUND.",
            "role_es": "COTA de exclusión subterránea en germanio arbitrada y madura sobre radiación espontánea.",
        },
        {
            "id": "ES02-FIEDORCZUK2022",
            "citation": "Fiedorczuk, K. & Chen, J. Molecular structures reveal synergistic rescue of Delta508 CFTR by Trikafta modulators. Science 378, 284–290 (2022).",
            "doi": "10.1126/science.ade2216",
            "year": 2022,
            "role_en": "Cryo-EM structure 8EIQ illustrating genetic deletion at residue 508 vs ~200 unmodeled flexible R-domain residues.",
            "role_es": "Estructura Cryo-EM 8EIQ que ilustra la deleción genética en el residuo 508 frente a ~200 residuos flexibles del dominio R sin modelar.",
        },
        {
            "id": "ES02-TRILLO2025",
            "citation": "Trillo, S. & Navascués, M. Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement. Phys. Rev. D 111, L121101 (2025).",
            "doi": "10.1103/physrevd.111.l121101",
            "year": 2025,
            "role_en": "Young 2025 smeared-gravity hybrid entanglement model (erf(r / 2*sigma) / r), capped at PROPOSED.",
            "role_es": "Modelo híbrido joven de 2025 con gravedad suavizada (erf(r / 2*sigma) / r), acotado en PROPUESTO.",
        },
        {
            "id": "ES02-AZIZ2025",
            "citation": "Aziz, J. & Howl, R. Classical theories of gravity produce entanglement. Nature (2025).",
            "doi": "10.1038/s41586-025-09595-7",
            "year": 2025,
            "role_en": "Disputed 2025 classical-gravity quantum-matter entanglement proposal inside the 24-month window (PROPOSED).",
            "role_es": "Propuesta en disputa de 2025 sobre entrelazamiento con gravedad clásica dentro de la ventana de 24 meses (PROPUESTO).",
        },
        {
            "id": "ES02-APRILE2026",
            "citation": "Aprile, E. et al. (XENONnT Collaboration). Challenging Spontaneous Quantum Collapse with the XENONnT Dark Matter Detector. Phys. Rev. Lett. (2026).",
            "doi": "10.1103/2jm3-4976",
            "year": 2026,
            "role_en": "Young 2026 1 to 140 keV electronic-recoil collapse search held at SINGLE RESULT by the 24-month rule.",
            "role_es": "Búsqueda joven de 2026 de colapso por retroceso electrónico de 1 a 140 keV mantenida en RESULTADO ÚNICO por la regla de 24 meses.",
        },
        {
            "id": "ES02-HEPLEAN2025",
            "citation": "Tooby-Smith, J. HepLean: Digitalising high energy physics. Comput. Phys. Commun. 308, 109457 (2025).",
            "doi": "10.1016/j.cpc.2024.109457",
            "year": 2025,
            "role_en": "Formal Lean 4 type-checking of physics definitions and explicit axiom-provenance signatures.",
            "role_es": "Verificación formal de tipos en Lean 4 para definiciones físicas y firmas explícitas de axiomas.",
        },
        {
            "id": "ES02-SCITE2021",
            "citation": "Nicholson, J. M. et al. scite: A smart citation index that displays the context of citations and classifies their intent using deep learning. Quant. Sci. Stud. 2, 882–898 (2021).",
            "doi": "10.1162/qss_a_00146",
            "year": 2021,
            "role_en": "Citation-polarity classification motivating >= 20-character contrasting_audit scope notes.",
            "role_es": "Clasificación de polaridad de citas que motiva las notas de alcance contrasting_audit de >= 20 caracteres.",
        },
    ],
    "skill_path": "skills/essays/derived-not-measured/SKILL.md",
    "verifier_path": "skills/essays/derived-not-measured/verify_essay_derived_not_measured.py",
    "ai_line_en": (
        "AI contribution to the cited results: none. No AI system contributed to any measurement, exclusion bound, "
        "Cryo-EM coordinate map, or theoretical proposal cited in this essay. The essay text, epistemic mutation "
        "simulator, and verifier were drafted with AI assistance and audited deterministically against primary sources."
    ),
    "ai_line_es": (
        "Contribución de IA a los resultados citados: ninguna. Ningún sistema de IA contribuyó a alguna medición, "
        "cota de exclusión, mapa de coordenadas Cryo-EM o propuesta teórica citada en este ensayo. El texto del "
        "ensayo, el simulador de mutaciones epistémicas y el verificador se redactaron con asistencia de IA y se "
        "auditaron de forma determinista contra las fuentes primarias."
    ),
}
