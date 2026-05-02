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


## Scripts

```bash
cd evaluation/analysis
python plot_main_study.py
python plot_medllama_crosslingual.py
python run_statistics.py
```


```bash
# from repo root, with venv active
./.venv/bin/python scripts/redact_report_title_date.py path/to/in.pdf path/to/out.pdf
```
