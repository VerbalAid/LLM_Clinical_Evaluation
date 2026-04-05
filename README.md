# 🏥 Clinical Medical NLP Evaluation

Comprehensive evaluation of clinical language models and medical NLP systems for clinical decision support.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Models](#models-evaluated)
- [Features](#key-features)
- [Getting Started](#getting-started)
- [Usage](#usage)

---

## Overview

This project evaluates the performance of various language models on clinical tasks, including:
- Clinical text analysis
- Medical information retrieval
- Language neutralization
- Multi-lingual evaluation (English/Spanish)

---

## 📁 Project Structure

```
.
├── Irish_model/              # Main model implementation and evaluation
│   ├── main.py              # Primary evaluation script
│   ├── prompts/             # Prompt templates
│   └── CC-MIR.en-es/        # Clinical corpora
├── local/                    # Local analysis and testing
│   ├── main.py              # Local evaluation runner
│   ├── analysis.py          # Performance analysis
│   ├── Outputs/             # Model evaluation outputs (Prompt 1-6)
│   └── Analysis/            # Visualization and reports
├── Cloud/                    # Cloud-based implementations
│   └── Argument_neutraliser.ipynb
├── Quantised_Medgemma/       # Quantized medical models
├── data/
│   ├── original/            # Raw datasets
│   └── neutralized/         # Processed datasets
└── CC-MIR.en-es/            # Bilingual clinical corpora
```

---

## 🤖 Models Evaluated

| Model | Size | Type |
|-------|------|------|
| MedLLaMA 2 | 7B | Fine-tuned Medical LLM |
| Mistral | 7B Instruct | General Purpose |
| Qwen | 1.5B | Lightweight |
| MedGemma | 4B Quantized | Efficient Medical |

---

## ✨ Key Features

- **Multi-lingual Support**: English and Spanish evaluation
- **Multiple Prompt Strategies**: 6 different prompt variations
- **Comprehensive Analysis**: Performance metrics across clinical dimensions
- **Resource Tracking**: Memory and execution time monitoring
- **Reproducible Results**: Structured output formats (JSONL)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Virtual environment set up at `Irish_model/.venv`

### Installation

```bash
# Activate the virtual environment
source Irish_model/.venv/bin/activate

# Install dependencies (varies by component)
pip install -r requirements.txt  # if present
```

### Quick Start

```bash
# Run local evaluation
cd local
python main.py

# Run Irish model evaluation
cd Irish_model
python main.py
```

---

## 📊 Usage

### Local Analysis
```bash
cd local
python analysis.py          # Generate performance analysis
python analysis_medllama.py # MedLLaMA specific analysis
```

### Output Structure
Results are saved in JSONL format:
- `local/Outputs/Prompt{1-6}/` - Model outputs for each prompt variation
- `local/Analysis/` - Generated visualizations and reports

### Datasets
- **Original**: `data/original/` - Raw clinical texts
- **Neutralized**: `data/neutralized/` - Processed texts
- **Corpora**: `CC-MIR.en-es/` - Bilingual clinical datasets

---

## 📝 License

See repository for license information.

---

## 📧 Contact

For questions about this project, refer to the documentation in individual directories.
