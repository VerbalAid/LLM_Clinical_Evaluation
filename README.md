# Clinical text restructuring — LLM evaluation

**Repository:** [github.com/VerbalAid/LLM_Clinical_Evaluation](https://github.com/VerbalAid/LLM_Clinical_Evaluation)

**Branches:** I work on **`main`** and **`master`** — they’re the same commit. If you ever land on an old “neutralisation” README and a flat list of files, that’s the legacy **`old`** branch; switch the branch dropdown to **`main`**. (I’ve set the default branch on GitHub to **`main`** and dropped **`old`**, so you shouldn’t see that anymore.)

This repo is my **HiTZ Center / UPV-EHU internship** project: I evaluated **large language models** on turning **Spanish MIR-style examination justifications** into **unified English clinical narratives** while trying to keep medical specificity intact.

The full write-up — methods, results, error taxonomy — is in [`docs/HITZ_Internship_Report.pdf`](docs/HITZ_Internship_Report.pdf).

---

## What’s in here

| Part | What it is |
|------|------------|
| [`data/CC-MIR.en-es/`](data/CC-MIR.en-es/) | I ship a small **synthetic** demo JSON so anyone can sanity-check Ollama. The real CC-MIR files stayed internal at HiTZ; I never put them on the public repo (see `.gitignore`). |
| [`evaluation/analysis/`](evaluation/analysis/) | The CSV/JSON I used to back the plots, plus scripts to regenerate figures and run the stats. |
| [`evaluation/prompts/Prompt1`–`Prompt6`](evaluation/prompts/) | The six prompt designs (P1–P6) I ran in the study. |
| [`evaluation/outputs/`](evaluation/outputs/) | Where JSONL runs go when you execute the eval scripts locally. |
| [`evaluation/main.py`](evaluation/main.py) | My Ollama runner — tweak `MODEL_NAME` and the prompt path if you replicate. |
| [`evaluation/Medllama_english_test.py`](evaluation/Medllama_english_test.py) | Extra MedLlama runs on **English** inputs (for the cross-language bit in the report). |
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
