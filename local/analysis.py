import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data: Model, Prompt, Case, Fidelity, Neutralisation, Clarity, Total, Time(mins), RAM(GB)
data = []

# MedLlama
medllama_cases = [
    ('P1', 'Thoracic trauma', 0, 1, 0, 1, 20, 7.3),
    ('P1', 'Knee injury', 0, 1, 0, 1, 20, 7.3),
    ('P2', 'Endocrino A', 1, 1, 1, 3, 10, 7.1),
    ('P2', 'Paliativos B', 2, 2, 2, 6, 10, 7.1),
    ('P3', 'Gine 1', 0, 1, 1, 2, 6, 7.3),
    ('P3', 'Endocrino 2', 1, 1, 1, 3, 6, 7.3),
    ('P4', 'Infecciosas A', 0, 1, 1, 2, 5, 7.0),
    ('P4', 'Cardio B', 2, 2, 2, 6, 5, 7.0),
    ('P5', 'Gine 1', 1, 2, 1, 4, 3, 6.9),
    ('P5', 'Gine 2', 0, 0, 0, 0, 3, 6.9),
    ('P6', 'Cardio AF', 0, 0, 1, 1, 4, 7.0),
    ('P6', 'Genética Turner', 1, 0, 1, 2, 4, 7.0),
]

for prompt, case, fid, neut, clar, tot, time, ram in medllama_cases:
    data.append(['MedLlama', prompt, case, fid, neut, clar, tot, time, ram])

# Qwen
qwen_cases = [
    ('P1', 'Pediatría', 0, 0, 0, 0, 3, 5.5),
    ('P1', 'Hematología', 0, 0, 1, 1, 3, 5.5),
    ('P2', 'Infecciosas', 2, 1, 2, 5, 3.7, 5.7),
    ('P2', 'Plástica', 2, 2, 1, 5, 3.7, 5.7),
    ('P3', 'Turner Syndrome', 2, 2, 2, 6, 1.31, 5.5),
    ('P3', 'Traumatic Shock', 1, 2, 1, 4, 1.31, 5.5),
    ('P4', 'Ginecología', 0, 2, 0, 2, 1.67, 6.0),
    ('P4', 'Nefrología', 0, 1, 0, 1, 1.67, 6.0),
    ('P5', 'Nefrología AIN', 0, 1, 0, 1, 1.82, 5.6),
    ('P5', 'Digestivo', 0, 0, 1, 1, 1.82, 5.6),
    ('P6', 'Psiquiatría Litio', 0.5, 1, 0, 1.5, 1.38, 5.7),
    ('P6', 'Neumología', 1, 1.5, 1, 3.5, 1.38, 5.7),
]

for prompt, case, fid, neut, clar, tot, time, ram in qwen_cases:
    data.append(['Qwen', prompt, case, fid, neut, clar, tot, time, ram])

# Mistral
mistral_cases = [
    ('P1', 'Cardiology', 0.5, 1, 0.5, 2.0, 13, 6.7),
    ('P1', 'Pediatrics', 1.5, 1, 1.5, 4.0, 13, 6.7),
    ('P2', 'Digestive Surgery', 1.8, 1.8, 1.7, 5.3, 4.75, 6.8),
    ('P2', 'Neurology', 1.5, 1.2, 1.5, 4.2, 4.75, 6.8),
    ('P3', 'Digestive Surgery', 0.6, 1.6, 1.2, 3.4, 5.63, 6.8),
    ('P3', 'Psychiatry', 1.9, 1.7, 1.8, 5.4, 5.63, 6.8),
    ('P4', 'Anatomy', 0.4, 1.2, 0.8, 2.4, 4.17, 6.8),
    ('P4', 'Endocrinology', 1.8, 1.6, 1.7, 5.1, 4.17, 6.8),
    ('P5', 'Urgencias', 1.7, 1.6, 1.8, 5.1, 4.39, 6.8),
    ('P5', 'Infecciosas RSV', 1.0, 1.3, 1.6, 3.9, 4.39, 6.8),
    ('P6', 'Ginecología', 1.6, 1.7, 1.8, 5.1, 6.09, 6.9),
    ('P6', 'Psiquiatría', 0.7, 0.4, 0.5, 1.6, 6.09, 6.9),
]

for prompt, case, fid, neut, clar, tot, time, ram in mistral_cases:
    data.append(['Mistral', prompt, case, fid, neut, clar, tot, time, ram])

# Create DataFrame
df = pd.DataFrame(data, columns=['Model', 'Prompt', 'Case', 'Fidelity', 
                                  'Neutralisation', 'Clarity', 'Total', 
                                  'Time (mins)', 'RAM (GB)'])

# OUTPUT 1: Average scores by dimension for each model (3 graphs)
fig1, axes = plt.subplots(1, 3, figsize=(15, 5))

for idx, model in enumerate(['MedLlama', 'Qwen', 'Mistral']):
    model_data = df[df['Model'] == model]
    
    ax = axes[idx]
    dims = ['Fidelity', 'Neutralisation', 'Clarity']
    means = [model_data[dim].mean() for dim in dims]
    
    bars = ax.bar(dims, means, color='steelblue', alpha=0.8)
    ax.set_ylim(0, 2)
    ax.set_ylabel('Mean Score (out of 2)')
    ax.set_title(f'{model} - Average by Dimension', fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    for bar, mean in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                f'{mean:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('dimension_scores.png', dpi=300, bbox_inches='tight')
plt.show()

# OUTPUT 2: Model comparison
fig2, ax = plt.subplots(figsize=(8, 6))

model_means = df.groupby('Model')[['Fidelity', 'Neutralisation', 'Clarity']].mean()

x = np.arange(len(model_means.index))
width = 0.25

for i, dim in enumerate(['Fidelity', 'Neutralisation', 'Clarity']):
    offset = width * (i - 1)
    ax.bar(x + offset, model_means[dim], width, label=dim, alpha=0.8)

ax.set_ylabel('Mean Score (out of 2)')
ax.set_title('Model Comparison', fontweight='bold', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(model_means.index)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

# OUTPUT 3: Score by prompt (3 graphs) and overall performance
fig3 = plt.figure(figsize=(16, 5))

# Score by prompt for each model
for idx, model in enumerate(['MedLlama', 'Qwen', 'Mistral']):
    model_data = df[df['Model'] == model]
    prompt_means = model_data.groupby('Prompt')['Total'].mean()
    
    ax = plt.subplot(1, 4, idx + 1)
    bars = ax.bar(prompt_means.index, prompt_means.values, color='steelblue', alpha=0.8)
    
    mean_score = prompt_means.mean()
    ax.axhline(mean_score, color='red', linestyle='--', linewidth=2, 
               label=f'Mean: {mean_score:.2f}')
    
    ax.set_xlabel('Prompt')
    ax.set_ylabel('Mean Total Score (out of 6)')
    ax.set_title(f'{model} - Score by Prompt', fontweight='bold')
    ax.set_ylim(0, 6.5)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

# Overall performance
ax = plt.subplot(1, 4, 4)
model_totals = df.groupby('Model')['Total'].mean()
bars = ax.bar(model_totals.index, model_totals.values, alpha=0.8, color='steelblue')

ax.set_ylabel('Mean Total Score (out of 6)')
ax.set_title('Overall Performance', fontweight='bold', pad=20)
ax.set_ylim(0, 4.5)  # Increased y-axis limit
ax.grid(axis='y', alpha=0.3)

for bar, val in zip(bars, model_totals.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
            f'{val:.2f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('performance_scores.png', dpi=300, bbox_inches='tight')
plt.show()

# OUTPUT 4: Resource usage graphs
fig4 = plt.figure(figsize=(16, 5))

# Time and RAM by prompt for each model
for idx, model in enumerate(['MedLlama', 'Qwen', 'Mistral']):
    model_data = df[df['Model'] == model]
    prompt_stats = model_data.groupby('Prompt')[['Time (mins)', 'RAM (GB)']].mean()
    
    ax = plt.subplot(1, 4, idx + 1)
    ax2 = ax.twinx()
    
    x = np.arange(len(prompt_stats.index))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, prompt_stats['Time (mins)'], width, 
                   label='Time (mins)', color='steelblue', alpha=0.8)
    bars2 = ax2.bar(x + width/2, prompt_stats['RAM (GB)'], width, 
                    label='RAM (GB)', color='coral', alpha=0.8)
    
    ax.set_xlabel('Prompt')
    ax.set_ylabel('Time (mins)', color='steelblue')
    ax2.set_ylabel('RAM (GB) / 7.6', color='coral')
    ax.set_title(f'{model} - Resource Usage', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(prompt_stats.index)
    ax.tick_params(axis='y', labelcolor='steelblue')
    ax2.tick_params(axis='y', labelcolor='coral')
    ax2.set_ylim(0, 7.6)
    
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8)

# Overall resource comparison plot
# First average per (Model, Prompt) to avoid duplicated cases
resource_prompt = (
    df.groupby(['Model', 'Prompt'])[['Time (mins)', 'RAM (GB)']]
      .mean()
      .reset_index()
)

resource_means = (
    resource_prompt
    .groupby('Model')[['Time (mins)', 'RAM (GB)']]
    .mean()
)

# Time plot
ax = plt.subplot(1, 4, 4)
bars = ax.bar(resource_means.index, resource_means['Time (mins)'],
              color='steelblue', alpha=0.8)
ax.set_ylabel('Time (mins)')
ax.set_title('Avg Time per Model (Prompt-level)', fontweight='bold')
ax.grid(axis='y', alpha=0.3)


plt.tight_layout()
plt.savefig('resource_usage.png', dpi=300, bbox_inches='tight')
plt.show()

# Print summary statistics
print("=" * 70)
print("SUMMARY STATISTICS")
print("=" * 70)

print("\n1. Overall Model Performance:")
summary = df.groupby('Model')[['Fidelity', 'Neutralisation', 'Clarity', 'Total']].agg(['mean', 'std'])
print(summary)

print("\n2. Performance by Prompt (All Models):")
prompt_summary = df.groupby('Prompt')[['Fidelity', 'Neutralisation', 'Clarity', 'Total']].mean()
print(prompt_summary)

print("\n3. Resource Usage by Model:")
resource_summary = df.groupby('Model')[['Time (mins)', 'RAM (GB)']].agg(['mean', 'min', 'max'])
print(resource_summary)

print("\n4. Best and Worst Cases:")
print("\nTop 5 Cases:")
top5 = df.nlargest(5, 'Total')[['Model', 'Prompt', 'Case', 'Total']]
print(top5.to_string(index=False))

print("\nBottom 5 Cases:")
bottom5 = df.nsmallest(5, 'Total')[['Model', 'Prompt', 'Case', 'Total']]
print(bottom5.to_string(index=False))

print("\n5. Efficiency Analysis (Score per Minute):")
efficiency = df.groupby('Model').apply(lambda x: x['Total'].sum() / x['Time (mins)'].sum())
print(efficiency)

# EXTRA ANALYSIS: Case Performance + Specialisation Performance


import matplotlib.pyplot as plt

# 1. CASE PERFORMANCE 
case_scores = df.groupby("Case")["Total"].mean().sort_values()

plt.figure(figsize=(10, 6))
plt.barh(case_scores.index, case_scores.values, alpha=0.8)
plt.title("Average Performance by Case (All Models)", fontweight="bold")
plt.xlabel("Mean Total Score (0–6)")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig("case_performance.png", dpi=300)
plt.show()

# 2. SPECIALISATION MAPPING
specialty_map = {
    # Trauma / MSK
    "Thoracic trauma": "Trauma",
    "Knee injury": "Trauma",
    "Traumatic Shock": "Trauma",

    # Endocrinology
    "Endocrino A": "Endocrinology",
    "Endocrino 2": "Endocrinology",
    "Endocrinology": "Endocrinology",

    # Cardiology
    "Cardio B": "Cardiology",
    "Cardio AF": "Cardiology",
    "Cardiology": "Cardiology",

    # Palliative Care
    "Paliativos B": "Palliative Care",

    # Infectious Disease
    "Infecciosas A": "Infectious Disease",
    "Infecciosas": "Infectious Disease",
    "Infecciosas RSV": "Infectious Disease",
    "RSV": "Infectious Disease",

    # Genetics
    "Genética Turner": "Genetics",
    "Turner Syndrome": "Genetics",

    # Gastro / Digestive Surgery
    "Digestive Surgery": "Digestive",
    "Digestivo": "Digestive",

    # Neurology
    "Neurology": "Neurology",

    # Psychiatry
    "Psychiatry": "Psychiatry",
    "Psiquiatría": "Psychiatry",
    "Psiquiatría Litio": "Psychiatry",

    # Nephrology
    "Nefrología": "Nephrology",
    "Nefrología AIN": "Nephrology",

    # Gynecology / Obstetrics
    "Gine 1": "Gynecology",
    "Gine 2": "Gynecology",
    "Ginecología": "Gynecology",
    "Ginecología": "Gynecology",

    # Pediatrics
    "Pediatría": "Pediatrics",
    "Pediatrics": "Pediatrics",

    # Plastic Surgery
    "Plástica": "Plastic Surgery",

    # Anatomy
    "Anatomy": "Anatomy",

    # Pulmonology
    "Neumología": "Pulmonology",

    # Surgery (general)
    "Urgencias": "Emergency Medicine",
}

# Apply mapping
df["Specialisation"] = df["Case"].map(specialty_map)

# 3. SPECIALISATION PERFORMANCE 
spec_scores = (
    df.groupby("Specialisation")["Total"]
      .mean()
      .sort_values()
)

plt.figure(figsize=(10, 6))
plt.barh(spec_scores.index, spec_scores.values, alpha=0.8, color="steelblue")
plt.title("Performance by Medical Specialisation (All Models)", fontweight="bold")
plt.xlabel("Mean Total Score (0–6)")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()
plt.savefig("specialisation_performance.png", dpi=300)
plt.show()
