# CC-MIR data in this repo

The **full CC-MIR examination corpus** I used for the internship lives under HiTZ’s internal rules — I **can’t** put those files on a public GitHub repo, so you won’t find the real cases here.

## What I actually published

- **`demo_case_for_public_repo.json`** — two completely **made-up** vignettes with the same JSON fields my scripts expect (`options`, `first_argument`, …). I use it to check that Ollama and the prompt plumbing work end-to-end.

## If you’re at HiTZ and re-running my setup

1. Drop your approved CC-MIR JSON into this folder **on your machine**.
2. Point the code at it with **`CC_MIR_CORPUS_FILE`** (e.g. `CC-MIR-2-M.es.json`), or tweak `evaluation/main.py` / `Medllama_english_test.py` once locally.
3. I listed the real filenames in `.gitignore` on purpose — please don’t `git add` the actual corpus.

The exact ignore rules for this directory are in the root `.gitignore`.
