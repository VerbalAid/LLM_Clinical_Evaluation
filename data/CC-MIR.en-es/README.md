# Corpus folder (CC-MIR)

The **full CC-MIR examination corpus** used for the internship research report is **HiTZ / internal only** and must **not** be pushed to a public GitHub repository.

## What this public repo includes

- **`demo_case_for_public_repo.json`** — two **fully synthetic** items with the same JSON shape the evaluation scripts expect (`options`, `first_argument`, etc.). Use this to check that your Ollama setup runs.

## If you work at HiTZ (internal replication)

1. Copy your approved CC-MIR JSON files into this folder **on your machine only**.
2. Set the environment variable **`CC_MIR_CORPUS_FILE`** to the filename you use (for example `CC-MIR-2-M.es.json`), or edit `evaluation/main.py` / `Medllama_english_test.py` once locally.
3. Never `git add` real corpus files — they are listed in `.gitignore`.

## File name patterns ignored by git

See the repository root `.gitignore` for `data/CC-MIR.en-es/` rules.
