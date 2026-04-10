"""Figures for the main three-model study (report §4). Reads tabular data from analysis/data/."""

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


def load_main_df():
    # Small public sample (12 rows per model). Report Table 4 uses full n=72 internally.
    path = os.path.join(DATA, "case_level_scores_public_sample.csv")
    df = pd.read_csv(path)
    return df.rename(
        columns={"Time_mins": "Time (mins)", "RAM_GB": "RAM (GB)"}
    )


def load_specialty_map():
    path = os.path.join(DATA, "specialty_mapping.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    df = load_main_df()
    specialty_map = load_specialty_map()

    # OUTPUT 1: Average scores by dimension for each model (3 graphs)
    fig1, axes = plt.subplots(1, 3, figsize=(15, 5))

    for idx, model in enumerate(["MedLlama", "Qwen", "Mistral"]):
        model_data = df[df["Model"] == model]
        ax = axes[idx]
        dims = ["Fidelity", "Restructuring", "Clarity"]
        means = [model_data[dim].mean() for dim in dims]
        bars = ax.bar(dims, means, color="steelblue", alpha=0.8)
        ax.set_ylim(0, 2)
        ax.set_ylabel("Mean Score (out of 2)")
        ax.set_title(f"{model} - Average by Dimension", fontweight="bold")
        ax.grid(axis="y", alpha=0.3)
        for bar, mean in zip(bars, means):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.05,
                f"{mean:.2f}",
                ha="center",
                va="bottom",
            )

    plt.tight_layout()
    plt.savefig(_fig("dimension_scores.png"), dpi=300, bbox_inches="tight")
    plt.close(fig1)

    # OUTPUT 2: Model comparison
    fig2, ax = plt.subplots(figsize=(8, 6))
    model_means = df.groupby("Model")[["Fidelity", "Restructuring", "Clarity"]].mean()
    x = np.arange(len(model_means.index))
    width = 0.25
    for i, dim in enumerate(["Fidelity", "Restructuring", "Clarity"]):
        offset = width * (i - 1)
        ax.bar(x + offset, model_means[dim], width, label=dim, alpha=0.8)
    ax.set_ylabel("Mean Score (out of 2)")
    ax.set_title("Model Comparison", fontweight="bold", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(model_means.index)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(_fig("model_comparison.png"), dpi=300, bbox_inches="tight")
    plt.close(fig2)

    # OUTPUT 3: Score by prompt + overall
    fig3 = plt.figure(figsize=(16, 5))
    for idx, model in enumerate(["MedLlama", "Qwen", "Mistral"]):
        model_data = df[df["Model"] == model]
        prompt_means = model_data.groupby("Prompt")["Total"].mean()
        ax = plt.subplot(1, 4, idx + 1)
        ax.bar(prompt_means.index, prompt_means.values, color="steelblue", alpha=0.8)
        mean_score = prompt_means.mean()
        ax.axhline(
            mean_score,
            color="red",
            linestyle="--",
            linewidth=2,
            label=f"Mean: {mean_score:.2f}",
        )
        ax.set_xlabel("Prompt")
        ax.set_ylabel("Mean Total Score (out of 6)")
        ax.set_title(f"{model} - Score by Prompt", fontweight="bold")
        ax.set_ylim(0, 6.5)
        ax.legend()
        ax.grid(axis="y", alpha=0.3)

    ax = plt.subplot(1, 4, 4)
    model_totals = df.groupby("Model")["Total"].mean()
    bars = ax.bar(model_totals.index, model_totals.values, alpha=0.8, color="steelblue")
    ax.set_ylabel("Mean Total Score (out of 6)")
    ax.set_title("Overall Performance", fontweight="bold", pad=20)
    ax.set_ylim(0, 4.5)
    ax.grid(axis="y", alpha=0.3)
    for bar, val in zip(bars, model_totals.values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.15,
            f"{val:.2f}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )
    plt.tight_layout()
    plt.savefig(_fig("performance_scores.png"), dpi=300, bbox_inches="tight")
    plt.close(fig3)

    # OUTPUT 4: Resource usage
    fig4 = plt.figure(figsize=(16, 5))
    for idx, model in enumerate(["MedLlama", "Qwen", "Mistral"]):
        model_data = df[df["Model"] == model]
        prompt_stats = model_data.groupby("Prompt")[["Time (mins)", "RAM (GB)"]].mean()
        ax = plt.subplot(1, 4, idx + 1)
        ax2 = ax.twinx()
        xpos = np.arange(len(prompt_stats.index))
        w = 0.35
        ax.bar(
            xpos - w / 2,
            prompt_stats["Time (mins)"],
            w,
            label="Time (mins)",
            color="steelblue",
            alpha=0.8,
        )
        ax2.bar(
            xpos + w / 2,
            prompt_stats["RAM (GB)"],
            w,
            label="RAM (GB)",
            color="coral",
            alpha=0.8,
        )
        ax.set_xlabel("Prompt")
        ax.set_ylabel("Time (mins)", color="steelblue")
        ax2.set_ylabel("RAM (GB) / 7.6", color="coral")
        ax.set_title(f"{model} - Resource Usage", fontweight="bold")
        ax.set_xticks(xpos)
        ax.set_xticklabels(prompt_stats.index)
        ax.tick_params(axis="y", labelcolor="steelblue")
        ax2.tick_params(axis="y", labelcolor="coral")
        ax2.set_ylim(0, 7.6)
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=8)

    resource_prompt = (
        df.groupby(["Model", "Prompt"])[["Time (mins)", "RAM (GB)"]]
        .mean()
        .reset_index()
    )
    resource_means = resource_prompt.groupby("Model")[["Time (mins)", "RAM (GB)"]].mean()
    ax = plt.subplot(1, 4, 4)
    ax.bar(
        resource_means.index,
        resource_means["Time (mins)"],
        color="steelblue",
        alpha=0.8,
    )
    ax.set_ylabel("Time (mins)")
    ax.set_title("Avg Time per Model (Prompt-level)", fontweight="bold")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(_fig("resource_usage.png"), dpi=300, bbox_inches="tight")
    plt.close(fig4)

    # Console summary
    print("=" * 70)
    print("SUMMARY STATISTICS")
    print("=" * 70)
    print("\n1. Overall Model Performance:")
    print(
        df.groupby("Model")[["Fidelity", "Restructuring", "Clarity", "Total"]].agg(
            ["mean", "std"]
        )
    )
    print("\n2. Performance by Prompt (All Models):")
    print(
        df.groupby("Prompt")[["Fidelity", "Restructuring", "Clarity", "Total"]].mean()
    )
    print("\n3. Resource Usage by Model:")
    print(df.groupby("Model")[["Time (mins)", "RAM (GB)"]].agg(["mean", "min", "max"]))
    print("\n4. Best and Worst Cases:")
    print("\nTop 5 Cases:")
    print(df.nlargest(5, "Total")[["Model", "Prompt", "Case", "Total"]].to_string(index=False))
    print("\nBottom 5 Cases:")
    print(df.nsmallest(5, "Total")[["Model", "Prompt", "Case", "Total"]].to_string(index=False))
    efficiency = df.groupby("Model").apply(
        lambda x: x["Total"].sum() / x["Time (mins)"].sum()
    )
    print("\n5. Efficiency Analysis (Score per Minute):")
    print(efficiency)

    # Case performance
    case_scores = df.groupby("Case")["Total"].mean().sort_values()
    plt.figure(figsize=(10, 6))
    plt.barh(case_scores.index, case_scores.values, alpha=0.8)
    plt.title("Average Performance by Case (All Models)", fontweight="bold")
    plt.xlabel("Mean Total Score (0–6)")
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig(_fig("case_performance.png"), dpi=300)
    plt.close()

    df["Specialisation"] = df["Case"].map(specialty_map)
    spec_scores = df.groupby("Specialisation")["Total"].mean().sort_values()
    plt.figure(figsize=(10, 6))
    plt.barh(spec_scores.index, spec_scores.values, alpha=0.8, color="steelblue")
    plt.title(
        "Performance by Medical Specialisation (All Models)", fontweight="bold"
    )
    plt.xlabel("Mean Total Score (0–6)")
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig(_fig("specialisation_performance.png"), dpi=300)
    plt.close()

    print("\nFigures written to:", FIG)


if __name__ == "__main__":
    main()
