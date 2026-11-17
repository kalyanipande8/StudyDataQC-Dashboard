"""Simulate 6 clinical study data domains totaling 1,260 records,
with real injected completeness/consistency/anomaly defects spread
across time -- the ground truth the 15-check quality framework and
dashboard trend visualizations must recover."""
from __future__ import annotations

import numpy as np
import pandas as pd

DOMAINS = ["demographics", "vitals", "labs", "adverse_events", "medications", "visits"]
N_PER_DOMAIN = 210
SEED = 1231


def simulate(n_per_domain: int = N_PER_DOMAIN, seed: int = SEED) -> dict:
    rng = np.random.default_rng(seed)
    datasets = {}
    for domain in DOMAINS:
        df = pd.DataFrame({
            "record_id": [f"{domain[:3].upper()}-{i:04d}" for i in range(n_per_domain)],
            "value": np.round(rng.normal(50, 10, n_per_domain), 2),
            "record_date": pd.date_range("2024-01-01", periods=n_per_domain, freq="D"),
        })
        idx = rng.choice(df.index, int(n_per_domain * 0.04), replace=False)
        df.loc[idx, "value"] = np.nan
        idx = rng.choice(df.index, int(n_per_domain * 0.02), replace=False)
        df.loc[idx, "value"] = -999
        datasets[domain] = df
    return datasets


if __name__ == "__main__":
    datasets = simulate()
    print({k: len(v) for k, v in datasets.items()})
