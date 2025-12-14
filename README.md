# Clinical Text Neutralisation with Large Language Models

This repository contains the code, prompts, outputs, and analysis used
in a research internship project evaluating **large language models
(LLMs)** for **clinical text neutralisation**. The task consists of
transforming option-based clinical exam justifications into coherent,
option-free clinical narratives while preserving all medical facts and
diagnostic logic.

The project focuses on **model behaviour under constraints**, with
particular attention to **hallucinations, instruction-following
failures, and fidelity--fluency trade-offs** in multilingual and medical
contexts.

------------------------------------------------------------------------

## Task Description

Clinical exam justifications often rely on contrastive, option-based
reasoning (e.g., elimination of incorrect diagnoses). For practical
clinical or downstream NLP use, these texts must be rewritten into
**continuous clinical reasoning narratives** without introducing new
information or omitting evidence.

This project evaluates how well different LLMs perform this
**neutralisation task**, defined by the following requirements:

-   Removal of option references and eliminative reasoning\
-   Preservation of all clinical facts and evidence\
-   Coherent, clinician-style diagnostic explanation\
-   No hallucinated findings, mechanisms, or conclusions

------------------------------------------------------------------------

## Models Evaluated

The following models were evaluated under hardware and memory
constraints:

-   **MedLLaMA-2-7B** (medical domain--specialised)\
-   **Mistral-7B-Instruct** (generalist instruction-following model)\
-   **Qwen2.5-1.5B** (small-model stress test)

Additional experiments evaluated **MedLLaMA on English medical cases**
to isolate language effects from model capability.

------------------------------------------------------------------------

## Prompting Strategy

Six prompt designs were implemented to test different
instruction-following behaviours:

1.  System + one-shot demonstration\
2.  Zero-shot instruction prompt\
3.  Delimiter-based prompt\
4.  Do/Don't constraint prompt\
5.  Anti--Chain-of-Thought (final-answer-only) prompt\
6.  Output-targeted prompt (fixed-length narrative)

Prompt performance was analysed with respect to factual fidelity,
structural neutralisation, and clinical coherence.

------------------------------------------------------------------------

## Evaluation Framework

A manual, three-dimensional scoring framework was developed to capture
distinct failure modes not detectable by fluency-based metrics:

### Fidelity (0--2)

-   Preservation of medical facts and evidence\
-   No hallucinated findings or mechanisms\
-   Correct temporal and diagnostic logic

### Neutralisation Quality (0--2)

-   Complete removal of option-based structure\
-   Unified clinical narrative

### Clinical Clarity & Coherence (0--2)

-   Natural clinical reasoning flow\
-   Logical consistency and appropriate terminology

**Maximum score: 6**

------------------------------------------------------------------------

## Repository Structure

    .
    ├── main/                 # Core scripts for running model inference and prompting
    ├── prompts/              # Prompt templates and prompt-specific outputs
    ├── outputs/              # Raw model outputs across clinical cases
    ├── analysis/             # Analysis scripts and visualisations
    ├── medllama_english.py   # MedLLaMA evaluation on English medical cases
    ├── medllama_analysis.py  # Analysis of English MedLLaMA results
    └── README.md

------------------------------------------------------------------------

## Key Findings

-   **Mistral-7B-Instruct** demonstrated the most stable performance
    across fidelity, neutralisation, and clarity.
-   **MedLLaMA-2-7B** showed frequent hallucinations despite medical
    pretraining, particularly in non-English settings.
-   **Small models (≤1.5B parameters)** exhibited highly unstable
    behaviour.
-   **Zero-shot instruction prompts** consistently outperformed one-shot
    and demonstration-based prompts.
-   Fluent outputs frequently masked factual errors, reinforcing the
    inadequacy of perplexity- or BLEU-based evaluation for clinical
    tasks.

------------------------------------------------------------------------

## Limitations

-   Manual evaluation due to lack of reliable automated medical fidelity
    metrics\
-   Limited model scale (≤7B) due to hardware constraints\
-   Small but diverse set of clinical cases\
-   Focus on Spanish-to-English and English-only medical text

------------------------------------------------------------------------

## Future Directions

-   Automated hallucination detection via entity and logic alignment\
-   Lightweight post-generation verification layers\
-   Expanded multilingual clinical evaluation\
-   Instruction-tuning medical LLMs for controlled rewriting tasks

------------------------------------------------------------------------

## Notes

This repository reflects **exploratory research conducted during a
short-term internship**. The emphasis is on **methodological
transparency, failure analysis, and reproducibility**, rather than on
optimised model performance.
