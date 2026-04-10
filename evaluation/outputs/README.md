# Model outputs (JSONL)

Each line is one JSON object: model input fields plus the generated text.

**Public GitHub:** raw JSONL files are **gitignored** because they can echo text derived from the **internal CC-MIR corpus**. Generate them locally after you place the internal corpus (or use the tiny public demo corpus for smoke tests).

After running `evaluation/main.py`, the script creates `Prompt1` … `Prompt6` as needed and appends JSONL lines there.

If you work **inside HiTZ** with the real corpus, keep those JSONL files **only on your machine**; they are listed in `.gitignore` so a normal `git push` will not upload them.
