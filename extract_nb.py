import json
import glob

output = []
for file in sorted(glob.glob('/Users/baltaymarci/Documents/Feel Good AI/Analysis/*.ipynb')):
    output.append(f'--- {file} ---')
    with open(file, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        for i, cell in enumerate(nb.get('cells', [])):
            if cell.get('cell_type') == 'code':
                for out in cell.get('outputs', []):
                    if out.get('output_type') == 'stream':
                        text = ''.join(out.get('text', []))
                        output.append(f'Cell {i} output:\n{text.strip()}')
                    elif out.get('output_type') == 'execute_result' or out.get('output_type') == 'display_data':
                        data = out.get('data', {})
                        text = ''.join(data.get('text/plain', []))
                        if text:
                            output.append(f'Cell {i} result:\n{text.strip()}')
    output.append('\n')

with open('/Users/baltaymarci/Documents/Feel Good AI/Analysis/nb_outputs.txt', 'w') as f:
    f.write('\n'.join(output))
