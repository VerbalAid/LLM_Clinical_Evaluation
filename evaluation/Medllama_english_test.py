import json
import ollama
import os
import random
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(ROOT, "..", "data", "CC-MIR.en-es"))

# Same demo corpus as main.py unless you override with CC_MIR_CORPUS_FILE.
CORPUS_FILE = os.environ.get("CC_MIR_CORPUS_FILE", "demo_case_for_public_repo.json")

MODEL_NAME = "medllama2:7b"

ARG_PROMPT_FILE = os.path.join("prompts", "Prompt6", "argument_prompt.txt")


def load_file(path):
    p = path if os.path.isabs(path) else os.path.join(ROOT, path)
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


BASE_PROMPT = load_file(ARG_PROMPT_FILE)


def build_user_prompt(options, argumentation):
    return BASE_PROMPT.format(
        option_text="\n".join(options),
        argumentation=argumentation
    )


def run_model(options, argumentation):
    user_prompt = build_user_prompt(options, argumentation)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response["message"]["content"]


def load_dataset(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_output_path():
    prompt_folder = os.path.basename(os.path.dirname(ARG_PROMPT_FILE))
    prompt_num = ''.join(filter(str.isdigit, prompt_folder))

    save_dir = os.path.join(ROOT, "outputs", f"Prompt{prompt_num}")
    os.makedirs(save_dir, exist_ok=True)

    safe_model = MODEL_NAME.replace(":", "-").replace("/", "-")
    filename = f"prompt{prompt_num}_{safe_model}_english_test.jsonl"

    return os.path.join(save_dir, filename)


def main():
    print("\nRunning: medllama_english_test")
    start_time = time.time()

    data = load_dataset(os.path.join(DATA_DIR, CORPUS_FILE))
    selected = random.sample(data, 2)
    results = []

    for idx, item in enumerate(selected, start=1):
        print(f"[{idx}/{len(selected)}] Processing case...")

        output = run_model(item["options"], item["first_argument"])
        item["neutralized_argumentation"] = output
        results.append(item)

    elapsed_sec = time.time() - start_time
    minutes = int(elapsed_sec//60)
    seconds = int(elapsed_sec % 60)

    output_path = get_output_path()
    with open(output_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False, indent=2) + "\n")

    print(f"\nFinished! Saved to: {output_path}")
    print(f"Time elapsed: {minutes} minutes and {seconds} seconds")


if __name__ == "__main__":
    main()
