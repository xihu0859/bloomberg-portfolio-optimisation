# Data access and layout

The study uses a Bloomberg workbook supplied for FMAT3888. Its redistribution permission
has not been established, so the workbook, historical index levels, return series and original
download URL are deliberately excluded from this public repository.

Place your own authorised copy at `data/bloomberg.xlsx`, or set the environment variable
`BLOOMBERG_DATA_PATH` to an absolute path. Run Jupyter from the repository root.

Expected sheets: `Monthly`, `Weekly`, `Daily`. Each sheet contains a `Dates` marker in its
first column, ticker labels two rows above that marker, and dated index observations below it.
Missing Bloomberg values are coerced to NaN. The research notebook locates the header marker.

| Ticker | Asset class |
|---|---|
| ASA52 | Australian equities |
| NDDLWI | International equities |
| NDLEEGF | Emerging-market equities |
| RDAU | Australian listed property |
| FDCIISAH | Listed infrastructure |
| HEDGNAV | Hedge funds |
| BACM0 | Australian bonds |
| H03432AU | Global bonds |
| BAUBIL | Cash |

The common research sample contains 248 complete monthly simple returns from January 2006
to August 2026. Raw monthly returns are used for realised backtests; hedge-fund desmoothing
is applied to estimation inputs and re-estimated inside historical training windows.

`results/` contains only aggregate research results, not a substitute data feed. No account,
personal holdings or individual pension-member data are used.
