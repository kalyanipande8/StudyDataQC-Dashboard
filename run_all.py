import json
import os

from src.simulate_study_domains import simulate, DOMAINS
from src.quality_checks import run_all_checks


def main():
    datasets = simulate()
    checks = run_all_checks(datasets)

    n_total_records = sum(len(df) for df in datasets.values())
    summary = {"n_domains": len(DOMAINS), "n_total_records": n_total_records,
               "n_checks": len(checks), "checks": checks}

    os.makedirs("results", exist_ok=True)
    with open("results/summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
