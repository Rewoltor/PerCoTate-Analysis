import json

with open("NB5_figures.ipynb", "r") as f:
    nb = json.load(f)

for i, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if "Accuracy Paradox" in source or "figure 5" in source.lower() or "fig5" in source.lower():
            print(f"--- Cell {i} ---")
            print(source)
