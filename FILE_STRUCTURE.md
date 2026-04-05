# 📂 Complete Project File Structure & Layout

Comprehensive overview of the entire Clinical Medical NLP project directory structure.

---

## 🎯 Project Root Directories

```
Internship- Medical NLP/
├── README.md                          # Project overview and documentation
├── FILE_STRUCTURE.md                  # This file
│
├── 📁 Irish_model/                    # Primary model evaluation implementation
├── 📁 local/                          # Local testing and analysis
├── 📁 Cloud/                          # Cloud-based implementations
├── 📁 Quantised_Medgemma/             # Quantized model utilities
├── 📁 CC-MIR.en-es/                   # Bilingual clinical corpora (root)
├── 📁 data/                           # Dataset storage
└── 📁 oLLaMa-system-prompts/          # System prompt resources
```

---

## 📦 Detailed Directory Structure

### 1. **Irish_model/** - Main Model Implementation
Primary evaluation framework for clinical models.

```
Irish_model/
├── main.py                            # Entry point for model evaluation
│   └── Purpose: Load models, process prompts, generate outputs
│
├── output.jsonl                       # Model evaluation results
│
├── prompts/                           # Prompt templates directory
│   ├── system_prompt.txt              # System-level prompt configuration
│   └── argument_prompt.txt            # Argument evaluation prompt
│
├── CC-MIR.en-es/                      # Clinical corpora
│   ├── CC-MIR-1-F.en.json            # Case 1: Female, English
│   ├── CC-MIR-1-F.es.json            # Case 1: Female, Spanish
│   ├── CC-MIR-2-M.en.json            # Case 2: Male, English
│   └── CC-MIR-2-M.es.json            # Case 2: Male, Spanish
│
├── __pycache__/                       # Python cache directory
└── .venv/                             # Virtual environment (optional)
```

**Key Functions:**
- Load and initialize medical language models
- Execute prompts against models
- Save results in JSONL format for analysis

---

### 2. **local/** - Local Testing & Analysis
Comprehensive local evaluation with multiple models and prompts.

```
local/
├── main.py                            # Main orchestrator for local tests
│   └── Runs all model evaluations locally
│
├── analysis.py                        # Performance analysis script
│   └── Generates metrics and visualizations
│
├── analysis_medllama.py               # MedLLaMA-specific analysis
│   └── Specialized analysis for MedLLaMA 2-7B
│
├── Medllama_english_test.py          # English evaluation for MedLLaMA
│   └── Tests model on English clinical data
│
├── CC-MIR.en-es/                      # Clinical corpora (local copy)
│   ├── CC-MIR-1-F.en.json            # Female patient case (English)
│   ├── CC-MIR-1-F.es.json            # Female patient case (Spanish)
│   ├── CC-MIR-2-M.en.json            # Male patient case (English)
│   └── CC-MIR-2-M.es.json            # Male patient case (Spanish)
│
├── prompts/                           # 6 Different prompt variations
│   ├── Prompt1/
│   │   └── argument_prompt.txt
│   ├── Prompt2/
│   │   └── argument_prompt.txt
│   ├── Prompt3/
│   │   └── argument_prompt.txt
│   ├── Prompt4/
│   │   └── argument_prompt.txt
│   ├── Prompt5/
│   │   └── argument_prompt.txt
│   └── Prompt6/
│       └── argument_prompt.txt
│
├── Outputs/                           # Model evaluation results
│   ├── Prompt1/
│   │   ├── prompt1_medllama2-7b_english_test.jsonl
│   │   ├── prompt1_medllama2:7b.jsonl
│   │   ├── prompt1_mistral-7b-instruct.jsonl
│   │   └── prompt1_qwen2.5-1.5b.jsonl
│   │
│   ├── Prompt2/
│   │   ├── prompt2_medllama2-7b_english_test.jsonl
│   │   ├── prompt2_medllama2:7b.jsonl
│   │   ├── prompt2_mistral-7b-instruct.jsonl
│   │   └── prompt2_qwen2.5-1.5b.jsonl
│   │
│   ├── Prompt3/
│   │   ├── prompt3_medllama2-7b_english_test.jsonl
│   │   ├── prompt3_medllama2:7b.jsonl
│   │   ├── prompt3_mistral-7b-instruct.jsonl
│   │   └── prompt3_qwen2.5-1.5b.jsonl
│   │
│   ├── Prompt4/
│   │   ├── prompt4_medllama2-7b_english_test.jsonl
│   │   ├── prompt4_medllama2:7b.jsonl
│   │   ├── prompt4_mistral-7b-instruct.jsonl
│   │   └── prompt4_qwen2.5-1.5b.jsonl
│   │
│   ├── Prompt5/
│   │   ├── prompt5_medllama2-7b_english_test.jsonl
│   │   ├── prompt5_medllama2:7b.jsonl
│   │   ├── prompt5_mistral-7b-instruct.jsonl
│   │   └── prompt5_qwen2.5-1.5b.jsonl
│   │
│   └── Prompt6/
│       ├── prompt6_medllama2-7b_english_test.jsonl
│       ├── prompt6_medllama2:7b.jsonl
│       ├── prompt6_mistral-7b-instruct.jsonl
│       └── prompt6_qwen2.5-1.5b.jsonl
│
├── Analysis/                          # Generated visualizations & reports
│   ├── Analysis_of_prompts_medllama2:7b.png
│   ├── case_performance.png
│   ├── dimension_scores.png
│   ├── english_clinical_quality_overview.png
│   ├── english_specialisation_performance.png
│   ├── english_vs_spanish_dimensions.png
│   ├── model_comparison.png
│   ├── performance_scores.png
│   ├── ram_comparison_english_spanish.png
│   ├── resource_usage.png
│   ├── specialisation_performance.png
│   └── time_comparison_english_spanish.png
│
└── .vscode/                           # VS Code workspace settings
    └── settings.json
```

**Key Features:**
- **4 Models Tested**: MedLLaMA 2-7B, MedLLaMA 2-7B (English), Mistral 7B, Qwen 2.5-1.5B
- **6 Prompt Variations**: Different approaches to clinical evaluation
- **Performance Metrics**: RAM usage, execution time, accuracy scores
- **Visualizations**: Charts comparing models and prompts

---

### 3. **Cloud/** - Cloud-Based Implementations
Notebook-based implementations for cloud environments.

```
Cloud/
├── Argument_neutraliser.ipynb         # Argument neutralization workflow
│   └── Jupyter notebook for text preprocessing
│
└── argument_neutralizer_2 (1).ipynb   # Alternative neutralization approach
    └── Enhanced version of neutralizer
```

**Purpose:**
- Interactive development and testing
- Text neutralization and preprocessing
- Cloud execution capability

---

### 4. **Quantised_Medgemma/** - Model Quantization Utilities
Tools for working with quantized medical models.

```
Quantised_Medgemma/
├── download_model.py                  # Model download utility
│   └── Purpose: Fetch medgemma-4b-it from Hugging Face
│
└── llama.cpp/                         # Complete llama.cpp submodule
    ├── README.md                      # llama.cpp documentation
    ├── CMakeLists.txt                 # Build configuration
    ├── Makefile                       # Build instructions
    ├── convert_hf_to_gguf.py         # HuggingFace to GGUF conversion
    ├── convert_hf_to_gguf_update.py  # Updated converter
    ├── convert_llama_ggml_to_gguf.py # Legacy format conversion
    ├── convert_lora_to_gguf.py       # LoRA weight conversion
    │
    ├── 📁 src/                        # C++ source code
    ├── 📁 examples/                   # Example programs
    ├── 📁 tools/                      # Utility tools
    │   ├── quantize/                  # Quantization tools
    │   ├── server/                    # API server implementation
    │   └── llama-bench/               # Benchmarking tools
    │
    ├── 📁 gguf-py/                    # Python GGUF utilities
    │   ├── gguf.py                    # Main GGUF interface
    │   ├── gguf_reader.py             # Read GGUF files
    │   ├── gguf_writer.py             # Write GGUF files
    │   ├── vocab.py                   # Vocabulary utilities
    │   └── scripts/                   # Utility scripts
    │
    ├── 📁 ggml/                       # GGML backend
    ├── 📁 grammars/                   # Grammar definitions
    ├── 📁 tests/                      # Unit tests
    └── 📁 docs/                       # Documentation
```

**Key Utilities:**
- Model conversion (HF → GGUF format)
- Quantization management
- GGML tensor operations
- Server deployment

---

### 5. **CC-MIR.en-es/** - Bilingual Clinical Corpora (Root Level)
Primary location for clinical datasets.

```
CC-MIR.en-es/
├── CC-MIR-1-F.en.json               # Case 1 - Female Patient (English)
│   └── Contains: Clinical notes, medical history, test results
│
├── CC-MIR-1-F.es.json               # Case 1 - Female Patient (Spanish)
│   └── Spanish translation of case 1
│
├── CC-MIR-2-M.en.json               # Case 2 - Male Patient (English)
│   └── Contains: Clinical case data
│
└── CC-MIR-2-M.es.json               # Case 2 - Male Patient (Spanish)
    └── Spanish translation of case 2
```

**Data Format:**
- JSON structure with clinical case information
- Bilingual pairs (English/Spanish)
- 2 test cases (Female/Male)

---

### 6. **data/** - Raw and Processed Datasets
Data management and transformation.

```
data/
├── original/
│   └── es_example.json              # Spanish clinical example
│       └── Sample dataset for development
│
└── neutralized/                     # Processed datasets
    └── [Neutralized text outputs]
```

**Purpose:**
- Store raw input data
- Store processed/neutralized outputs
- Version control for datasets

---

### 7. **oLLaMa-system-prompts/** - System Prompt Resources
Educational materials and prompt engineering guides.

```
oLLaMa-system-prompts/
├── shortLab1-oLLaMa-zero-one-few-shot.pdf
│   └── Zero-shot, one-shot, few-shot prompting
│
├── shortLab2-oLLaMa-basic-prompting.pdf
│   └── Basic prompting techniques
│
├── shortLab3-oLLaMa-system-prompts.pdf
│   └── System prompt design
│
└── shortLab4-oLLaMa-advance-prompting.pdf
    └── Advanced prompt strategies
```

---

### 8. **Additional Root-Level Files**
Supporting documentation and research materials.

```
├── Descripción Tarea.pdf              # Task description (Spanish)
├── Internship-research.pdf            # Research documentation
├── Linguist_WhatDoesYourDoctorSay     # Linguistics research paper
├── week-by-week-Internship Report.pdf # Progress reports
└── local.zip                          # Backup archive
```

---

## 📊 Data Flow & Relationships

```
Input Data (CC-MIR.en-es/)
    ↓
Prompts (Prompt 1-6)
    ↓
Models (MedLLaMA, Mistral, Qwen)
    ↓
Outputs (local/Outputs/)
    ↓
Analysis Scripts (analysis.py)
    ↓
Visualizations (Analysis/)
```

---

## 🔧 File Type Summary

| Type | Count | Purpose |
|------|-------|---------|
| `.py` | 15+ | Python scripts & implementations |
| `.ipynb` | 2 | Jupyter notebooks |
| `.json` | 10+ | Data files & configurations |
| `.txt` | 18+ | Prompts & text data |
| `.pdf` | 6+ | Documentation & research |
| `.png` | 12+ | Analysis visualizations |
| `.jsonl` | 24+ | Model outputs (line-delimited JSON) |

---

## 📌 Key Entry Points

**For Running Evaluations:**
1. `Irish_model/main.py` - Single model test
2. `local/main.py` - Full local evaluation
3. `Cloud/Argument_neutraliser.ipynb` - Text preprocessing

**For Analysis:**
1. `local/analysis.py` - General performance analysis
2. `local/analysis_medllama.py` - MedLLaMA specific analysis
3. `local/Outputs/` - View raw model outputs

**For Model Management:**
1. `Quantised_Medgemma/download_model.py` - Download models
2. `Quantised_Medgemma/llama.cpp/` - Model tools

---

## 🎓 Project Organization

- **Evaluation Framework**: Local + Irish_model directories
- **Data Management**: CC-MIR.en-es + data directories
- **Model Management**: Quantised_Medgemma
- **Cloud Support**: Cloud directory with notebooks
- **Documentation**: Root-level PDFs and markdown files

---

## 📝 Notes

- Multiple copies of CC-MIR corpora exist in different directories for quick access
- Outputs organized by prompt variation for comparative analysis
- All models tested against same datasets for fair evaluation
- Results stored in JSONL format for easy processing

---

*Last Updated: April 2026*
