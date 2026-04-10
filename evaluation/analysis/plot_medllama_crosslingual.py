"""MedLlama English vs Spanish comparison (report §4.5). Reads analysis/data/*.csv and *.json."""

import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
FIG = os.path.join(ROOT, "figures")
os.makedirs(FIG, exist_ok=True)


def _fig(name):
    return os.path.join(FIG, name)


def main():
    english_cases = pd.read_csv(
        os.path.join(DATA, "medllama_english_case_scores.csv")
    )

    with open(
        os.path.join(DATA, "medllama_spanish_dimension_means.json"),
        encoding="utf-8",
    ) as f:
        spanish_dim_raw = json.load(f)
    spanish_dim_raw.pop("note", None)
    spanish_dimensions = pd.Series(spanish_dim_raw)

    res = pd.read_csv(os.path.join(DATA, "medllama_resources_by_prompt.csv"))
    english_resources = res[res["Language"] == "English"][
        ["Prompt", "Time_mins", "RAM_GB"]
    ].copy()
    english_resources["Lang"] = "English"
    spanish_resources = res[res["Language"] == "Spanish"][
        ["Prompt", "Time_mins", "RAM_GB", "Mean_total_score_spanish"]
    ].copy()
    spanish_resources["Lang"] = "Spanish"
    resources = pd.concat([english_resources, spanish_resources])

    english_dimensions = english_cases[
        ["Fidelity", "Restructuring", "Clarity"]
    ].mean()

    # PLOT 1: inference time
    plt.figure(figsize=(8, 5))
    for lang, g in resources.groupby("Lang"):
        plt.plot(g["Prompt"], g["Time_mins"], marker="o", label=lang)
    plt.ylabel("Time (minutes)")
    plt.title(
        "Inference Time per Prompt – English vs Spanish", fontweight="bold"
    )
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(_fig("time_comparison_english_spanish.png"), dpi=300)
    plt.close()

    # PLOT 2: RAM
    plt.figure(figsize=(8, 5))
    for lang, g in resources.groupby("Lang"):
        plt.plot(g["Prompt"], g["RAM_GB"], marker="s", label=lang)
    plt.ylabel("RAM (GB)")
    plt.title("RAM Usage per Prompt – English vs Spanish", fontweight="bold")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(_fig("ram_comparison_english_spanish.png"), dpi=300)
    plt.close()

    # PLOT 3: specialisation
    spec_perf = (
        english_cases.groupby("Specialisation")["TotalScore"]
        .mean()
        .sort_values()
    )
    plt.figure(figsize=(9, 5))
    plt.barh(spec_perf.index, spec_perf.values)
    plt.xlim(0, 6)
    plt.xlabel("Mean Composite Score (out of 6)")
    plt.title(
        "English Test – Performance by Clinical Specialisation",
        fontweight="bold",
    )
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig(_fig("english_specialisation_performance.png"), dpi=300)
    plt.close()

    # PLOT 4: three-panel overview
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].bar(english_dimensions.index, english_dimensions.values)
    axes[0].set_ylim(0, 2)
    axes[0].set_title("Average Score by Dimension")
    axes[0].set_ylabel("Mean Score (out of 2)")
    axes[0].grid(axis="y", alpha=0.3)

    axes[1].bar(range(1, len(english_cases) + 1), english_cases["TotalScore"])
    mean_score = english_cases["TotalScore"].mean()
    axes[1].axhline(
        mean_score, linestyle="--", color="red", label=f"Mean: {mean_score:.2f}"
    )
    axes[1].set_title("Total Score by Case")
    axes[1].set_xlabel("Case Number")
    axes[1].set_ylabel("Total Score (out of 6)")
    axes[1].legend()

    heatmap_data = english_cases[
        ["Fidelity", "Restructuring", "Clarity"]
    ].values
    im = axes[2].imshow(heatmap_data, aspect="auto", vmin=0, vmax=2)
    axes[2].set_yticks(range(len(english_cases)))
    axes[2].set_yticklabels(english_cases["Case"])
    axes[2].set_xticks(range(3))
    axes[2].set_xticklabels(["Fidelity", "Restructuring", "Clarity"])
    axes[2].set_title("Heatmap of Case Scores")
    cbar = fig.colorbar(im, ax=axes[2])
    cbar.set_label("Score")
    plt.tight_layout()
    plt.savefig(_fig("english_clinical_quality_overview.png"), dpi=300)
    plt.close(fig)

    # PLOT 5: English vs Spanish dimensions
    labels = ["Fidelity", "Restructuring", "Clarity"]
    x = np.arange(len(labels))
    width = 0.35
    plt.figure(figsize=(8, 5))
    plt.bar(x - width / 2, english_dimensions[labels], width, label="English")
    plt.bar(x + width / 2, spanish_dimensions[labels], width, label="Spanish")
    plt.ylim(0, 2)
    plt.xticks(x, labels)
    plt.ylabel("Mean Score (out of 2)")
    plt.title("Clinical Quality by Dimension – English vs Spanish")
    plt.grid(axis="y", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(_fig("english_vs_spanish_dimensions.png"), dpi=300)
    plt.close()

    print("MedLlama cross-lingual figures written to:", FIG)


if __name__ == "__main__":
    main()
