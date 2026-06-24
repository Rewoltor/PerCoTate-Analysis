import json
import glob

for nb_path in sorted(glob.glob('/Users/baltaymarci/Documents/Feel Good AI/Analysis/NB*.ipynb')):
    print(f"\n{'='*60}\nNOTEBOOK: {nb_path}\n{'='*60}\n")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        for i, cell in enumerate(nb.get('cells', [])):
            if cell['cell_type'] == 'code':
                outputs = cell.get('outputs', [])
                if not outputs:
                    continue
                print(f"--- Cell {i} Outputs ---")
                for out in outputs:
                    if out.get('output_type') == 'stream':
                        text = "".join(out.get('text', []))
                        print(text.strip())
                    elif out.get('output_type') in ['execute_result', 'display_data']:
                        data = out.get('data', {})
                        if 'text/plain' in data:
                            print("".join(data['text/plain']).strip())
