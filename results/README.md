# Result provenance

The CSV files transcribe rounded aggregate results from the original research notebook and
course report. Returns in `tactical_summary.csv` are cumulative over each separate 24-month
test. Volatilities are annualised. Turnover is total one-way trading, excludes initial
establishment, and accounts for drift. The 10 bp gap charges both strategies their own costs.

Dynamic CE differences are basis points of initial wealth, not annual returns. Their paired
Monte Carlo intervals use 50,000 independent evaluation paths conditional on the December
2015 fitted normal model. They exclude parameter uncertainty and dynamic-programming
approximation error. Small negative estimates do not imply an exact optimal dynamic policy
is theoretically inferior. These are the original experiment results, not a fresh full rerun.
