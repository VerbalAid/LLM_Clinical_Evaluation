import json
import requests

MODEL_NAME = "medllama2:7b"
HF_TOKEN = "YOUR_HF_TOKEN"  


def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def build_prompt(options, first_argument):
    system_prompt = load_file("prompts/system_prompt.txt")
    argument_prompt = load_file("prompts/argument_prompt.txt")
    
    # Fill in the variables
    argument_prompt = argument_prompt.format(
        option_text="\n".join(options),
        argumentation=first_argument
    )
    
    return system_prompt + "\n\n" + argument_prompt

def run_model(prompt):
    url = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}
    
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    
    if isinstance(result, list):
        return result[0].get("generated_text", "")
    return result.get("generated_text", "")


# Load data
with open("CC-MIR.en-es/CC-MIR-1-F.es.json", "r", encoding="utf-8") as f:
    data = json.load(f)

results = []

for item in data[:5]:  # Change 10 to process more cases
    prompt = build_prompt(item["options"], item["first_argument"])
    output = run_model(prompt)
    item["neutralized_argumentation"] = output
    results.append(item)
    print(f"Processed case {len(results)}")

# Save results
with open("output.jsonl", "w", encoding="utf-8") as f:
    for r in results:
        f.write(json.dumps(r, ensure_ascii=False, indent=2) + "\n")

print("output.jsonl saved!")