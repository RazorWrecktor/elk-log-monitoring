import os
import json

input_dir = os.path.join(os.getcwd(), "Data_original")
output_dir = os.path.join(os.getcwd(), "Data")
os.makedirs(output_dir, exist_ok=True)

def extract_json_objects(text):
    decoder = json.JSONDecoder()
    idx = 0
    length = len(text)
    objects = []

    while idx < length:
        try:
            obj, next_idx = decoder.raw_decode(text, idx)
            objects.append(obj)
            idx = next_idx
        except json.JSONDecodeError:
            idx += 1  # Skip invalid character and try again

    return objects

def convert_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    json_objects = extract_json_objects(content)
    if not json_objects:
        print(f"No JSON objects found in {input_path}")
        return

    with open(output_path, "w", encoding="utf-8") as out:
        for obj in json_objects:
            json.dump(obj, out, ensure_ascii=False)
            out.write("\n")

for filename in os.listdir(input_dir):
    if filename.endswith(".json"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        convert_file(input_path, output_path)

print("All files converted.")
