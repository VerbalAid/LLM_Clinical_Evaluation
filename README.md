# Clinical text restructuring — LLM evaluation

**Repository:** [github.com/VerbalAid/LLM_Clinical_Evaluation](https://github.com/VerbalAid/LLM_Clinical_Evaluation)

**Branches:** Use **`main`** for this project. **`old`** is only an archived early upload (different layout); switch to **`main`** in the branch menu if GitHub ever opens the wrong one.

### What this project is

This is my **HiTZ Center / UPV-EHU** (*MSc Language Analysis and Processing*) internship: **evaluating LLMs on a constrained clinical text restructuring task**—the same framing as in [*Evaluating Large Language Models for Clinical Text Restructuring*](docs/HITZ_Internship_Report.pdf) (systematic error taxonomy + specificity analysis).

**Core task:** Turn **option-based, eliminative exam justifications** (MIR-style reasoning: rule out options A–E with evidence) into a **single, flowing clinical narrative**, under a hard rule of **no new facts, no dropped facts, no vague paraphrase of specific medicine** (numbers, anatomy, time course, and terminology should stay as specific as in the source).

**Languages (what you can verify here):** The **written report** ([`docs/HITZ_Internship_Report.pdf`](docs/HITZ_Internship_Report.pdf)) frames the main study as **Spanish MIR-style justifications → English narrative** for all three models (**216** scored runs: **72 per model**, **six prompts**). The same report’s **§4.5** compares **MedLlama** on **Spanish vs English CC-MIR input** to separate **language** from **task** effects—backed in-repo by [`evaluation/analysis/data/medllama_resources_by_prompt.csv`](evaluation/analysis/data/medllama_resources_by_prompt.csv) and [`published_report_results.json`](evaluation/analysis/data/published_report_results.json) (`table_5_medllama_spanish_vs_english`: `Spanish_input` vs `English_input`). **Prompts** always ask for **English output**; Prompt 1 even references Spanish exam markers (e.g. `(rechaza)`), which fits Spanish source text. **This public repo** ships an **English** demo corpus and wires [`evaluation/main.py`](evaluation/main.py) to it by default; [`Medllama_english_test.py`](evaluation/Medllama_english_test.py) is the English-input helper I kept for replication. I did **not** keep raw JSONL on GitHub, so the README cannot honestly recover “what I ran first” day to day—only the **PDF + analysis tables** do.

**Models:** MedLlama-2-7B (medical specialist), Mistral-7B-Instruct (generalist), Qwen2.5-1.5B (small baseline), via Ollama.

**Evaluation:** Manual **three-dimensional** rubric—**Fidelity**, **Restructuring**, **Clinical clarity** (0–2 each, **6** total)—plus a **specificity-preservation** lens and a **four-type error taxonomy** over **127** coded failures (lexical fabrication, value distortion, temporal shift, anatomical mix-ups).

The full write-up is in [`docs/HITZ_Internship_Report.pdf`](docs/HITZ_Internship_Report.pdf).

---

## What’s in here

| Part | What it is |
|------|------------|
| [`data/CC-MIR.en-es/`](data/CC-MIR.en-es/) | I ship a small **synthetic** demo JSON so anyone can sanity-check Ollama. The real CC-MIR files stayed internal at HiTZ; I never put them on the public repo (see `.gitignore`). |
| [`evaluation/analysis/`](evaluation/analysis/) | The CSV/JSON I used to back the plots, plus scripts to regenerate figures and run the stats. |
| [`evaluation/prompts/Prompt1`–`Prompt6`](evaluation/prompts/) | The six prompt designs (P1–P6) I ran in the study. |
| [`evaluation/outputs/`](evaluation/outputs/) | Where JSONL runs go when you execute the eval scripts locally. |
| [`evaluation/main.py`](evaluation/main.py) | My Ollama runner — tweak `MODEL_NAME` and the prompt path if you replicate. |
| [`evaluation/Medllama_english_test.py`](evaluation/Medllama_english_test.py) | Runner for **English** CC-MIR input with MedLlama (matches the public demo wiring; Spanish-input MedLlama is part of the §4.5 comparison in the report). |
| [`scripts/redact_report_title_date.py`](scripts/redact_report_title_date.py) | I used this once to strip “April 2026” from the title slide of the PDF; needs PyMuPDF if you reuse it. |

---

## What I actually ran (summary)

- **Models:** MedLlama-2-7B, Mistral-7B-Instruct, Qwen2.5-1.5B (through Ollama).
- **Design:** 72 scored runs per model (12 cases × 6 prompts), **216** in total.
- **Scores:** Three dimensions (0–2 each): **Fidelity**, **Restructuring**, **Clinical clarity** → **0–6** overall.
- **What stuck with me:** Models often **blur “change the format” with “water down the medicine”** — specificity loss, hypernym swapping. **Mistral** (generalist, strong on instructions) beat **MedLlama** on this task more than I expected.

**How I ran inference (Appendix A in the PDF):** seed 42, temperature 0.7, max tokens 512, top-p 0.95 — Colab-class GPU setup, described properly in the report.

---

## How to set it up

```bash
cd Clinical
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Pull whatever Ollama models you’re using — I had things like `medllama2:7b`, `mistral:7b-instruct`, `qwen2.5:1.5b`. The names in the scripts need to match your local tags.

---

## How I run things

### Inference (Ollama)

```bash
cd evaluation
# I edit MODEL_NAME and ARG_PROMPT_FILE in main.py when I switch model/prompt
python main.py
python Medllama_english_test.py   # only when I want the English-source MedLlama experiment
```

JSONL lands under `evaluation/outputs/Prompt{N}/`.

### Plots and stats

```bash
cd evaluation/analysis
python plot_main_study.py
python plot_medllama_crosslingual.py
python run_statistics.py
```

PNGs go to `evaluation/analysis/figures/`. There’s a bit more detail on the data files in [`evaluation/analysis/README.md`](evaluation/analysis/README.md).

---

## Folder layout

```
Clinical/
├── README.md
├── requirements.txt
├── docs/
│   └── HITZ_Internship_Report.pdf
├── scripts/
│   └── redact_report_title_date.py
├── data/
│   ├── CC-MIR.en-es/
│   └── original/
└── evaluation/
    ├── main.py
    ├── Medllama_english_test.py
    ├── analysis/
    │   ├── README.md
    │   ├── data/
    │   ├── figures/
    │   ├── plot_main_study.py
    │   ├── plot_medllama_crosslingual.py
    │   └── run_statistics.py
    ├── prompts/
    └── outputs/
```

---

## Licence

I didn’t attach a formal **LICENSE** file when I published this. If you fork or reuse it in public, feel free to add whatever licence fits your situation — I’m not claiming legal advice here.
