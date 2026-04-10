# Analysis artefacts (report backing)

This folder holds **tabular data**, **aggregate statistics** transcribed from the internship report, and **scripts** that regenerate the evaluation figures.

## Data (`data/`)

| File | Purpose |
|------|---------|
| `case_level_scores_public_sample.csv` | Case-level scores (Fidelity, Restructuring, Clarity, Total, time, RAM) for MedLlama, Qwen, and Mistral across P1–P6 — small public sample for plots (12 rows per model). |
| `published_report_results.json` | Key tables and test results as stated in the internship report (full internal evaluation, n=72 per model). |
| `specialty_mapping.json` | Maps each case label to a clinical specialisation for the specialisation bar chart. |
| `medllama_english_case_scores.csv` | MedLlama English-input runs: per-case dimension scores and hallucination flags. |
| `medllama_resources_by_prompt.csv` | Inference time and RAM by prompt for English vs Spanish MedLlama runs. |
| `medllama_spanish_dimension_means.json` | Aggregate Spanish-input dimension means for the English vs Spanish comparison plot. |

**Raw model generations** (JSONL) are not duplicated here; they live in `evaluation/outputs/Prompt1` … `Prompt6/` when generated locally.

## Scripts

```bash
cd evaluation/analysis
python plot_main_study.py
python plot_medllama_crosslingual.py
python run_statistics.py
```

PNG outputs go to `figures/`. Plot scripts use a non-interactive backend (`Agg`) so they run without a display.

## PDF title slide

The report PDF in `docs/HITZ_Internship_Report.pdf` had the line “April 2026” redacted on the title slide. To repeat that step on another copy of the file:

```bash
# from repository root
./.venv/bin/python scripts/redact_report_title_date.py path/to/in.pdf path/to/out.pdf
```
