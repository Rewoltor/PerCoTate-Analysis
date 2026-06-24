import json

with open("NB5_figures.ipynb", "r") as f:
    nb = json.load(f)

script = ""
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        script += "".join(cell["source"]) + "\n"

with open("run_nb5_temp.py", "w") as f:
    f.write(script)
