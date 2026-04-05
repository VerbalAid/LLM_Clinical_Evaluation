# Clinical Medical NLP Evaluation

This repository contains work on evaluating clinical language models and medical NLP systems.

## Project Structure

- **Irish_model/**: Main model implementation and evaluation code
- **local/**: Local analysis and testing scripts
- **Cloud/**: Cloud-based implementations and notebooks
- **Quantised_Medgemma/**: Quantized medical model implementations
- **CC-MIR.en-es/**: Clinical corpora in English and Spanish
- **data/**: Original and neutralized datasets
- **local/Outputs/**: Model outputs for different prompts

## Models Evaluated

- MedLLaMA 2-7B
- Mistral 7B Instruct
- Qwen 2.5 1.5B

## Key Features

- Multi-lingual support (English/Spanish)
- Multiple prompt strategies (Prompt 1-6)
- Performance analysis across dimensions
- Resource usage tracking

## Getting Started

1. Activate the virtual environment:
   ```bash
   source Irish_model/.venv/bin/activate
   ```

2. Install dependencies as needed for your chosen model

3. Run evaluation scripts from `local/` or `Irish_model/` directories

## Usage

Refer to the individual scripts for detailed usage instructions.

## License

See repository for license information.
