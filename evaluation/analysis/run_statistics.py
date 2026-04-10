"""
Stats helper for my internship evaluation.

I’m comparing two different things:

1) What I actually wrote up (full internal run, 72 scores per model)
   — same numbers as in docs/HITZ_Internship_Report.pdf and
     data/published_report_results.json. The raw rows never went on GitHub.

2) The tiny public CSV (12 rows per model)
   — enough to exercise the code and redraw plots; Friedman / Wilcoxon here
     won’t match the χ² in the PDF, and that’s fine.

Run from here:

    cd evaluation/analysis
    python run_statistics.py
"""

import json
import os

import pandas as pd
from scipy.stats import friedmanchisquare, wilcoxon

# --- Paths next to this file ---
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")

SAMPLE_CSV = os.path.join(DATA_DIR, "case_level_scores_public_sample.csv")
REPORT_JSON = os.path.join(DATA_DIR, "published_report_results.json")

# Bonferroni: 3 pairwise tests, family-wise alpha 0.05
N_TESTS = 3
ALPHA = 0.05
BONFERRONI_ALPHA = ALPHA / N_TESTS


def load_report_reference():
    """Load my JSON copy of the report tables (for printing)."""
    with open(REPORT_JSON, encoding="utf-8") as f:
        return json.load(f)


def load_sample_scores():
    """Load the small public CSV everyone can use on GitHub."""
    return pd.read_csv(SAMPLE_CSV)


def build_paired_blocks(df):
    """
    Build three lists of Total scores (one list per model).

    Rows are paired by experimental *slot*: same Prompt order, then same Case
    order inside each model. This matches how the CSV was built (12 aligned rows).
    """
    blocks = []
    for model_name in ["MedLlama", "Qwen", "Mistral"]:
        part = df[df["Model"] == model_name].copy()
        part = part.sort_values(["Prompt", "Case"])
        scores = part["Total"].tolist()
        if len(scores) != 12:
            raise ValueError(f"Expected 12 rows for {model_name}, got {len(scores)}")
        blocks.append(scores)
    return blocks


def run_friedman_three_models(blocks):
    """
    Friedman test: non-parametric alternative to repeated-measures ANOVA.

    scipy.stats.friedmanchisquare takes the three samples as separate arguments.
    Each sample must have the same length (here: 12 paired slots).
    """
    stat, p_value = friedmanchisquare(blocks[0], blocks[1], blocks[2])
    return stat, p_value


def run_pairwise_wilcoxon(blocks):
    """
    Pairwise Wilcoxon signed-rank tests on the same paired slots.

    blocks order: MedLlama, Qwen, Mistral
    """
    med_llama, qwen, mistral = blocks[0], blocks[1], blocks[2]

    pairs = [
        ("Mistral vs MedLlama", mistral, med_llama),
        ("Mistral vs Qwen", mistral, qwen),
        ("MedLlama vs Qwen", med_llama, qwen),
    ]

    results = []
    for label, a, b in pairs:
        res = wilcoxon(a, b, zero_method="wilcox", alternative="two-sided")
        results.append((label, res.statistic, res.pvalue))

    return results


def bonferroni_significant(p_raw):
    """Return True if this raw p-value passes Bonferroni at family-wise 0.05."""
    return p_raw < BONFERRONI_ALPHA


def print_section_title(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def main():
    report = load_report_reference()
    df = load_sample_scores()

    # ----- Part A: what I reported in the PDF (full n=72) -----
    print_section_title("A) What’s in my internship report (full internal evaluation)")
    print(report["important_note"])
    print()
    ft = report["friedman_test_from_report"]
    print("Friedman (from report): χ²({}) = {}, {}".format(
        ft["df"],
        ft["chi2"],
        ft["p_two_sided_description"],
    ))
    print("\nPairwise Wilcoxon + Bonferroni (how I reported them):")
    for row in report["wilcoxon_pairwise_from_report_bonferroni"]:
        r_txt = row["effect_size_r"] if row["effect_size_r"] is not None else "n/a"
        print(
            f"  - {row['comparison']}: {row['p_description']}, r = {r_txt} "
            f"({row['effect_label']})"
        )

    print("\nTable 4–style means (composite, mean ± sd) from my published_report_results.json:")
    for name, stats_block in report["table_4_model_performance"].items():
        m, s = stats_block["composite_mean_sd"]
        print(f"  - {name}: {m} ± {s}")

    # ----- Part B: public sample descriptive stats -----
    print_section_title("B) Public sample CSV (12 rows per model)")
    desc = df.groupby("Model")["Total"].agg(["mean", "std", "count"])
    print(desc)
    print("\n(Smaller n than my real Table 4 — expected for the public sample.)")

    # ----- Part C: run tests on the public sample -----
    print_section_title("C) Tests computed from the public sample only")
    blocks = build_paired_blocks(df)
    chi2_stat, p_fried = run_friedman_three_models(blocks)
    print(f"Friedman chi-square statistic: {chi2_stat:.4f}")
    print(f"Friedman p-value: {p_fried:.6f}")
    if p_fried < 0.05:
        print("Interpretation (sample): p < 0.05 → models differ across paired slots.")
    else:
        print("Interpretation (sample): p >= 0.05 → no strong evidence of differences.")
    print(
        "\n(This p-value won’t match my PDF — different n and different score rows.)"
    )

    print(f"\nPairwise Wilcoxon (raw p-values). Bonferroni cutoff = {BONFERRONI_ALPHA:.4f}")
    for label, w_stat, p_raw in run_pairwise_wilcoxon(blocks):
        ok = bonferroni_significant(p_raw)
        flag = "significant after Bonferroni" if ok else "not significant after Bonferroni"
        print(f"  - {label}: W-like stat = {w_stat:.4f}, p = {p_raw:.6f} → {flag}")

    print_section_title("Done")
    print("If you’re citing results, go from my PDF + published_report_results.json.")
    print("If you’re just learning the workflow, this script + the public CSV is enough.")


if __name__ == "__main__":
    main()
