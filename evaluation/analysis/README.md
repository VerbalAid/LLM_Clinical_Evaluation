# Analysis folder

This is where I kept the **tables and numbers** behind the internship report, plus the **Python scripts** that redraw the figures and print the statistical checks.

## What’s in `data/`

| File | What I used it for |
|------|---------------------|
| `case_level_scores_public_sample.csv` | A **small** public slice (12 rows per model) so the plots and stats scripts run on GitHub without the internal corpus. Not the full n=72 table from the report. |
| `published_report_results.json` | The key tables and test summaries **as they appear in my PDF** (full internal study). Handy if you want to compare without opening the report. |
| `specialty_mapping.json` | I mapped messy case labels to a speciality for the horizontal bar chart. |
| `medllama_english_case_scores.csv` | Per-case scores for the MedLlama **English-input** experiment. |
| `medllama_resources_by_prompt.csv` | Time and RAM by prompt for English vs Spanish MedLlama. |
| `medllama_spanish_dimension_means.json` | Aggregate Spanish-side dimension means for the comparison plots. |

I didn’t duplicate raw JSONL generations here — those live under `evaluation/outputs/` when you run the eval scripts yourself.

## Scripts

```bash
cd evaluation/analysis
python plot_main_study.py
python plot_medllama_crosslingual.py
python run_statistics.py
```

Figures drop into `figures/`. I forced matplotlib’s **Agg** backend so it runs headless on a server without a GUI.

## PDF title slide

I redacted **“April 2026”** on page 1 of `docs/HITZ_Internship_Report.pdf` for the version in this repo. If you need to do the same on another copy:

```bash
# from repo root, with venv active
./.venv/bin/python scripts/redact_report_title_date.py path/to/in.pdf path/to/out.pdf
```
