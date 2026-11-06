"""Check notebook code syntax without licensed data or executing experiments."""
import ast
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
notebook = json.loads((root / "notebooks/portfolio_research.ipynb").read_text(encoding="utf-8"))
count = 0
for i, cell in enumerate(notebook["cells"]):
    if cell["cell_type"] == "code":
        ast.parse("".join(cell["source"]), filename=f"notebook_cell_{i}")
        count += 1
print(f"PASS: {count} code cells parse. This is not an execution or model-accuracy check.")
