"""Run selected original cells with an authorised workbook, from the repo root.

Checks SAA/TAA and dynamic experiments, but skips the large Q4 repeated simulations.
"""
import contextlib
import io
import json
from pathlib import Path
import matplotlib

matplotlib.use('Agg')
root = Path(__file__).resolve().parents[1]
nb = json.loads((root / 'notebooks/portfolio_research.ipynb').read_text(encoding='utf-8'))
# Original source-cell positions; public notebook adds one introductory cell.
source_cells = [1, 5, 10, 13, 16, 22, 25, 36, 37, 56, 57, 58, 61, 62,
                70, 73, 74, 75, 78, 98, 103, 104, 105, 106, 107,
                114, 115, 117, 123, 124, 127]
namespace = {'__name__': '__research_validation__'}
for source_index in source_cells:
    cell = nb['cells'][source_index + 1]
    assert cell['cell_type'] == 'code'
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(''.join(cell['source']), f'cell_{source_index}', 'exec'), namespace)
    import matplotlib.pyplot as plt
    plt.close('all')
    print(f'PASS source cell {source_index}', flush=True)
print('PASS: selected estimation, constraints, historical SAA/TAA and dynamic checks.')
print('Large repeated Q4 simulation/bootstrap experiments were not rerun.')
