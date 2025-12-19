import json
import os

def extract():
    json_path = 'apps.json'
    output_path = 'names_for_ai.txt'
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    names = [item.get('name', 'Unknown') for item in data]
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name + '\n')
            
    print(f"Successfully extracted {len(names)} names to {output_path}")
    print("You can now copy these names to AI and ask for descriptions.")

if __name__ == '__main__':
    extract()
