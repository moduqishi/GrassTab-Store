import json
import os
import re

def update_descriptions():
    json_path = 'apps.json'
    results_path = 'ai_results.txt' # The file where you paste AI output
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return
    
    if not os.path.exists(results_path):
        print(f"Error: {results_path} not found. Please create it and paste AI output (Format: Name: Description)")
        return

    # 1. Load AI results into a dictionary
    # Expected format per line: "Name: Description" or "Name：Description"
    desc_map = {}
    with open(results_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            
            # Split by first colon (supports both English and Chinese colons)
            parts = re.split(r'[:：]', line, maxsplit=1)
            if len(parts) == 2:
                name = parts[0].strip()
                desc = parts[1].strip()
                desc_map[name] = desc

    # 2. Update JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    for item in data:
        name = item.get('name')
        if name in desc_map:
            item['description'] = desc_map[name]
            updated_count += 1
            
    # 3. Save updated JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Successfully updated {updated_count} descriptions in {json_path}")

if __name__ == '__main__':
    update_descriptions()
