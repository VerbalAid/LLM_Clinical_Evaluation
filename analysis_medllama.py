import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =====================================================
# ENGLISH – CASE-LEVEL DATA (2 cases per prompt)
# =====================================================

english_cases = pd.DataFrame({
    "Prompt": ["P1","P1","P2","P2","P3","P3","P4","P4","P5","P5","P6","P6"],
    "Case": [
        "P1 – Neurology","P1 – Pneumology",
        "P2 – Digestive","P2 – Pneumology",
        "P3 – Neurology","P3 – Emergencies",
        "P4 – Cardiology","P4 – Digestive",
        "P5 – Cardiology","P5 – Digestive",
        "P6 – Traumatology","P6 – Nephrology"
    ],
    "Specialisation": [
        "Neurology","Pneumology",
        "Digestive","Pneumology",
        "Neurology","Emergencies",
        "Cardiology","Digestive",
        "Cardiology","Digestive",
        "Traumatology","Nephrology"
    ],
    "Fidelity":        [0.2,0.7,1.1,1.6,0.5,0.2,2.0,2.0,2.0,1.5,2.0,0.0],
    "Neutralisation": [1.1,1.3,1.3,1.7,1.3,0.3,1.0,0.0,2.0,1.5,1.0,1.0],
    "Clarity":        [0.5,1.0,1.3,1.6,0.7,0.2,2.0,1.0,2.0,1.5,2.0,1.0],
})

english_cases["TotalScore"] = (
    english_cases["Fidelity"]
    + english_cases["Neutralisation"]
    + english_cases["Clarity"]
)

# Hallucination flag (retained for analysis, not plotted)
english_cases["Hallucination"] = [
    1,1,  # P1
    1,0,  # P2
    1,1,  # P3
    0,0,  # P4
    0,0,  # P5
    0,1   # P6
]


# =====================================================
# ENGLISH – PROMPT-LEVEL SUMMARY
# =====================================================

english_prompt = (
    english_cases
    .groupby("Prompt")
    .agg(
        MeanScore=("TotalScore","mean"),
        Fidelity=("Fidelity","mean"),
        Neutralisation=("Neutralisation","mean"),
        Clarity=("Clarity","mean")
    )
    .reset_index()
)


# =====================================================
# SPANISH DATA
# =====================================================

spanish_dimensions = pd.Series({
    "Fidelity": 0.45,
    "Neutralisation": 0.90,
    "Clarity": 0.70
})

spanish_resources = pd.DataFrame({
    "Prompt": [f"P{i}" for i in range(1,7)],
    "Score": [1,4.5,2.5,4.25,2.5,1.5],
    "Time":  [20,10,6,5,3,4],
    "RAM":   [7.3,7.1,7.3,7.0,6.9,7.0],
    "Lang": "Spanish"
})


# =====================================================
# ENGLISH RESOURCES
# =====================================================

english_resources = pd.DataFrame({
    "Prompt": [f"P{i}" for i in range(1,7)],
    "Time": [11,7,3,5,2,2],
    "RAM":  [7.3,7.0,7.1,7.0,7.0,7.1],
    "Lang": "English"
})

resources = pd.concat([english_resources, spanish_resources])


# =====================================================
# DIMENSION MEANS
# =====================================================

english_dimensions = english_cases[
    ["Fidelity","Neutralisation","Clarity"]
].mean()


# =====================================================
# PLOT 1: INFERENCE TIME (LINE)
# =====================================================

plt.figure(figsize=(8,5))
for lang, g in resources.groupby("Lang"):
    plt.plot(g["Prompt"], g["Time"], marker="o", label=lang)

plt.ylabel("Time (minutes)")
plt.title("Inference Time per Prompt – English vs Spanish", fontweight="bold")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("time_comparison_english_spanish.png", dpi=300)
plt.show()


# =====================================================
# PLOT 2: RAM USAGE (LINE)
# =====================================================

plt.figure(figsize=(8,5))
for lang, g in resources.groupby("Lang"):
    plt.plot(g["Prompt"], g["RAM"], marker="s", label=lang)

plt.ylabel("RAM (GB)")
plt.title("RAM Usage per Prompt – English vs Spanish", fontweight="bold")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("ram_comparison_english_spanish.png", dpi=300)
plt.show()


# =====================================================
# PLOT 3: PERFORMANCE BY CLINICAL SPECIALISATION
# =====================================================

spec_perf = (
    english_cases
    .groupby("Specialisation")["TotalScore"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(9,5))
plt.barh(spec_perf.index, spec_perf.values)
plt.xlim(0,6)
plt.xlabel("Mean Composite Score (out of 6)")
plt.title(
    "English Test – Performance by Clinical Specialisation",
    fontweight="bold"
)
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig("english_specialisation_performance.png", dpi=300)
plt.show()


# =====================================================
# PLOT 4: ENGLISH CLINICAL QUALITY OVERVIEW (3 PANELS)
# =====================================================

fig, axes = plt.subplots(1, 3, figsize=(15,5))

# A) Average score by dimension
axes[0].bar(
    english_dimensions.index,
    english_dimensions.values
)
axes[0].set_ylim(0,2)
axes[0].set_title("Average Score by Dimension")
axes[0].set_ylabel("Mean Score (out of 2)")
axes[0].grid(axis="y", alpha=0.3)

# B) Total score by case
axes[1].bar(
    range(1, len(english_cases)+1),
    english_cases["TotalScore"]
)
mean_score = english_cases["TotalScore"].mean()
axes[1].axhline(mean_score, linestyle="--", color="red",
                label=f"Mean: {mean_score:.2f}")
axes[1].set_title("Total Score by Case")
axes[1].set_xlabel("Case Number")
axes[1].set_ylabel("Total Score (out of 6)")
axes[1].legend()

# C) Heatmap-style matrix
heatmap_data = english_cases[["Fidelity","Neutralisation","Clarity"]].values
im = axes[2].imshow(heatmap_data, aspect="auto", vmin=0, vmax=2)

axes[2].set_yticks(range(len(english_cases)))
axes[2].set_yticklabels(english_cases["Case"])
axes[2].set_xticks(range(3))
axes[2].set_xticklabels(["Fidelity","Neutralisation","Clarity"])
axes[2].set_title("Heatmap of Case Scores")

cbar = fig.colorbar(im, ax=axes[2])
cbar.set_label("Score")

plt.tight_layout()
plt.savefig("english_clinical_quality_overview.png", dpi=300)
plt.show()


# =====================================================
# PLOT 5: ENGLISH vs SPANISH – DIMENSION COMPARISON
# =====================================================

labels = ["Fidelity","Neutralisation","Clarity"]
x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(8,5))
plt.bar(x - width/2, english_dimensions[labels], width, label="English")
plt.bar(x + width/2, spanish_dimensions[labels], width, label="Spanish")

plt.ylim(0,2)
plt.xticks(x, labels)
plt.ylabel("Mean Score (out of 2)")
plt.title("Clinical Quality by Dimension – English vs Spanish")
plt.grid(axis="y", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("english_vs_spanish_dimensions.png", dpi=300)
plt.show()
