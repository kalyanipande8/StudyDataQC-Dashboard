# StudyDataQC-Dashboard

A data quality framework with 15 automated checks across 1,260
simulated clinical records spanning 6 data domains, with an
interactive Streamlit dashboard visualizing completeness,
consistency, and anomaly trends for study teams.

> Developed a data quality framework with 15 automated checks across
> 1,260 simulated clinical records and 6 data domains. Built an
> interactive dashboard visualizing data completeness, consistency,
> and anomaly trends for study teams.

**Naming note:** this account already has a different project named
`StudyDataQC` (a 25-rule CDISC/SDTM validation framework from an
earlier resume version). This project implements a distinct resume
bullet (15 checks, 6 domains, interactive dashboards) and is named
`StudyDataQC-Dashboard` to avoid a GitHub name collision with that
existing, different repository.

## What's real vs. synthetic — read this first

**Real:** `src/quality_checks.py` implements exactly 15 genuine
checks (`assert len(DOMAINS) * 2 + 3 == 15`): a completeness check and
a range check for each of the 6 domains, plus 3 cross-domain
consistency checks (record dates within the study period).
`app.py` is a real, runnable Streamlit dashboard with a domain
selector, live completeness/out-of-range metrics, a per-domain value
trend plot, and a cross-domain completeness bar chart — not a static
mockup. Because the simulation injects known missingness and out-of-
range defects independently of the checks, every number reported is
measured directly from running the checks.

**Synthetic:** there is no real multi-domain clinical study dataset
in this environment. `src/simulate_study_domains.py` generates 6
domains (demographics, vitals, labs, adverse events, medications,
visits) x 210 records each, with real injected missingness (~4%) and
out-of-range values (~2%) per domain.

## Results (real, from `run_all.py`)

```
6 domains, 1,260 total records, 15 checks

Each domain: ~96% completeness, ~4 out-of-range values detected
All date-consistency checks: 0 out-of-study-period records
```

`tests/test_pipeline.py` (5 tests, all passing) checks 6 domains are
defined, record count >=1200, exactly 15 checks run, completeness
checks detect real missingness in every domain, and range checks
detect real out-of-range values in every domain.

## Usage

```bash
pip install -r requirements.txt
streamlit run app.py       # interactive dashboard
python3 run_all.py          # headless check results
python3 -m pytest tests/ -v
```

## Project structure

```
src/
  simulate_study_domains.py   # 6-domain, 1,260-record simulation
  quality_checks.py            # 15-check completeness/range/consistency framework
app.py                         # Streamlit interactive dashboard
run_all.py
tests/test_pipeline.py
```

## Tech stack

Python 3.9+, Streamlit, matplotlib, pandas, numpy, pytest. (The
resume names R; this version implements all checks and visualizations
directly in Python.)

## Limitations

- No real multi-domain clinical study dataset is used.
- Anomaly detection uses a simple 3-sigma rule rather than a
  domain-specific anomaly model.
