# Before you push to **public** GitHub

1. **Corpus** — Only `data/CC-MIR.en-es/demo_case_for_public_repo.json` should be tracked. Run `git status` and ensure no `CC-MIR-*.json` files appear as staged.
2. **Outputs** — No `evaluation/outputs/**/*.jsonl` should be committed.
3. **Secrets** — No API keys in the repo (check `.env` is not added).
4. **Internship report PDF** — `docs/HITZ_Internship_Report.pdf` is your choice to publish; if your university restricts it, remove it from the remote and keep it private.

To **stop tracking** files that were committed before these rules (without removing the public demo file from git):

```bash
git rm --cached data/CC-MIR.en-es/CC-MIR-*.json 2>/dev/null || true
git rm --cached evaluation/outputs/Prompt*/*.jsonl 2>/dev/null || true
git rm --cached data/original/*.json 2>/dev/null || true
```

Keep `demo_case_for_public_repo.json` and `README.md` under `data/CC-MIR.en-es/`. Then commit the `.gitignore` update.
