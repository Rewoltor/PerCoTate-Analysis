import json
import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
import plotly.graph_objects as go
import builtins
import glob

# 1. Config
NOTEBOOKS = sorted(glob.glob("NB*.ipynb"))
REPORT_FILE = "ORIGINAL_ANALYSIS_SUMMARY.md"
ASSET_DIR = "report_assets"

if not os.path.exists(ASSET_DIR):
    os.makedirs(ASSET_DIR)

# 2. State
md_content = []
img_counter = 0

def add_md(text):
    md_content.append(text)

def add_text_block(text):
    if text.strip():
        md_content.append("\n```text\n" + text + "\n```\n")

# 3. Capture Wrappers
text_buffer = []

def custom_print(*args, **kwargs):
    text_buffer.append(" ".join(map(str, args)))

def custom_display(*args, **kwargs):
    for arg in args:
        if isinstance(arg, pd.DataFrame):
            text_buffer.append(arg.to_markdown())
        else:
            text_buffer.append(str(arg))

def flush_text():
    global text_buffer
    if text_buffer:
        add_text_block("\n".join(text_buffer))
        text_buffer = []

def custom_plt_show(*args, **kwargs):
    global img_counter
    flush_text()
    img_name = f"orig_plot_{img_counter}.png"
    img_path = os.path.join(ASSET_DIR, img_name)
    plt.savefig(img_path, bbox_inches='tight', dpi=150)
    plt.close()
    md_content.append(f"\n![Original Analysis Plot]({img_path})\n")
    img_counter += 1

def custom_plotly_show(self, *args, **kwargs):
    global img_counter
    flush_text()
    img_name = f"orig_plotly_{img_counter}.png"
    img_path = os.path.join(ASSET_DIR, img_name)
    try:
        self.write_image(img_path, engine="kaleido", scale=2)
        md_content.append(f"\n![Original Interactive Plot]({img_path})\n")
        img_counter += 1
    except:
        pass

# Monkeypatch
builtins.print = custom_print
builtins.display = custom_display
plt.show = custom_plt_show
go.Figure.show = custom_plotly_show

# 4. Main Loop
add_md("# Original Analysis Summary\n")
add_md("This report summarizes the results from the initial analysis workflow.\n")

for nb_file in NOTEBOOKS:
    add_md(f"\n---\n## Notebook: {nb_file}\n")
    
    with open(nb_file, 'r') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            add_md("".join(cell['source']) + "\n")
        
        elif cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            if not source.strip(): continue
            
            try:
                plt.figure() 
                exec(source, globals())
                flush_text()
            except Exception as e:
                custom_print(f"Error in {nb_file}: {e}")
                flush_text()

# 5. Save
with open(REPORT_FILE, 'w') as f:
    f.write("\n".join(md_content))

builtins.print = print
print(f"Success! {REPORT_FILE} generated.")
