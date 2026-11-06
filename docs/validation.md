# Validation of the public edition

Checked on 6 November 2026 with Python 3.13.7, NumPy 2.3.3, pandas 2.3.3,
SciPy 1.16.2 and Matplotlib 3.10.6.

## Executed checks

- `python scripts/check_notebook.py`: all 65 code cells parse.
- `python scripts/run_selected_checks.py`, with the original workbook supplied locally through
  `BLOOMBERG_DATA_PATH`: PASS for all 31 selected original research cells.
- The executed subset includes workbook loading, common monthly returns, hedge-fund
  desmoothing, covariance validity, constrained efficient-frontier/GMV checks and strategic
  growth classifications.
- It reconstructs the four historical SAA and TAA experiments, executes the notebook's
  feasibility/optimality checks and computes realised performance comparisons.
- It solves the baseline three-period dynamic problem and independently evaluates it, then
  runs the four historical dynamic comparisons, the growth-band controls and the independent
  50,000-path matched-static CE comparison.

The source-cell positions are recorded explicitly in the runner. The public notebook adds
one introduction cell, so its visible positions are shifted by one.

## What was not rerun

The large Q4 repeated Monte Carlo and bootstrap experiments, every parameter sensitivity
experiment and the full wealth-grid/MC refinement sweep were not rerun during publication.
Their retained figures and reported results are from the original saved research run.
The publication check is a selected execution check, not a proof of accuracy for every wealth
state or every model calibration.

The workbook and all raw data remained local and are not tracked by Git. Initial raw-data
preview outputs and the coursework download URL were removed. Selected original PNG chart
outputs remain embedded so the notebook can be read without the data. The report and optional
slides are original team artifacts; the README supplies the qualified portfolio interpretation.
