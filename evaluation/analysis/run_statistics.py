"""
Statistical tests for the internship evaluation.

There are TWO different things in this project:

1) INTERNSHIP REPORT (full internal evaluation, n = 72 scores per model)
   - The numbers in docs/HITZ_Internship_Report.pdf and in
     data/published_report_results.json come from that full evaluation.
   - Those raw score rows are not in the public repo (internal CC-MIR only).

2) PUBLIC SAMPLE (this GitHub-friendly repository)
   - data/case_level_scores_public_sample.csv has 12 rows per model
     (6 prompts × 2 example cases) for plots and learning the code.
   - Friedman / Wilcoxon on this file will NOT match the report's chi-square;
     that is expected.

Run from the analysis folder:

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
    """Load the published table values from the internship report (for printing)."""
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

    # ----- Part A: what the internship report states (full internal n=72) -----
    print_section_title("A) Values from the internship report (full internal evaluation)")
    print(report["important_note"])
    print()
    ft = report["friedman_test_from_report"]
    print("Friedman (from report): χ²({}) = {}, {}".format(
        ft["df"],
        ft["chi2"],
        ft["p_two_sided_description"],
    ))
    print("\nPairwise Wilcoxon + Bonferroni (as stated in the report):")
    for row in report["wilcoxon_pairwise_from_report_bonferroni"]:
        r_txt = row["effect_size_r"] if row["effect_size_r"] is not None else "n/a"
        print(
            f"  - {row['comparison']}: {row['p_description']}, r = {r_txt} "
            f"({row['effect_label']})"
        )

    print("\nTable 4 style means (composite, mean ± sd) from published_report_results.json:")
    for name, stats_block in report["table_4_model_performance"].items():
        m, s = stats_block["composite_mean_sd"]
        print(f"  - {name}: {m} ± {s}")

    # ----- Part B: public sample descriptive stats -----
    print_section_title("B) Public sample CSV (12 rows per model)")
    desc = df.groupby("Model")["Total"].agg(["mean", "std", "count"])
    print(desc)
    print("\n(This is NOT the same n as Table 4 in the internship report.)")

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
        "\nNote: this p-value will NOT match the report, because n and scores differ."
    )

    print(f"\nPairwise Wilcoxon (raw p-values). Bonferroni cutoff = {BONFERRONI_ALPHA:.4f}")
    for label, w_stat, p_raw in run_pairwise_wilcoxon(blocks):
        ok = bonferroni_significant(p_raw)
        flag = "significant after Bonferroni" if ok else "not significant after Bonferroni"
        print(f"  - {label}: W-like stat = {w_stat:.4f}, p = {p_raw:.6f} → {flag}")

    print_section_title("Done")
    print("For formal claims, use the internship report PDF and published_report_results.json.")
    print("For learning Python, use this script + the public sample CSV.")


if __name__ == "__main__":
    main()
