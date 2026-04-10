# Model outputs (JSONL)

Each line is one JSON blob: the fields I fed the model plus whatever it generated.

I **gitignore** these on the public repo because the text can mirror sensitive clinical material from the internal CC-MIR runs. If you clone this and add the real corpus (or just the demo JSON), running `evaluation/main.py` will create `Prompt1` … `Prompt6` and write JSONL there on your machine.

If you’re working inside HiTZ with the full data, I kept the same rule: outputs stay local; a normal `git push` won’t ship them.
