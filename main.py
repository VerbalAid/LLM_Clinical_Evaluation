import json
import ollama
import os
import random
import time

MODEL_NAME = "medllama:2:7b"

# Prompt selection
ARG_PROMPT_FILE = "prompts/Prompt1/argument_prompt.txt"


def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
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

    save_dir = os.path.join("Outputs", f"Prompt{prompt_num}")
    os.makedirs(save_dir, exist_ok=True)

    safe_model = MODEL_NAME.replace(":", "-").replace("/", "-")
    filename = f"prompt{prompt_num}_{safe_model}.jsonl"

    return os.path.join(save_dir, filename)


def main():

    # Time tracking
    t0 = time.time()

    # Load and process dataset
    data = load_dataset("CC-MIR.en-es/CC-MIR-2-M.en.json")
    selected = random.sample(data, 2)
    results = []

    for idx, item in enumerate(selected, start=1):
        print(f"[{idx}/{len(selected)}] Processing case...")

        output = run_model(item["options"], item["first_argument"])
        item["neutralized_argumentation"] = output
        results.append(item)

    # Time count
    elapsed_sec = time.time() - t0
    elapsed_min = round(elapsed_sec / 60, 2)

    # Save output
    output_path = get_output_path()
    with open(output_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False, indent=2) + "\n")


    print(f"\nFinished! Saved to: {output_path}")
    print(f"Time elapsed: {elapsed_min} minutes")


if __name__ == "__main__":
    main()

