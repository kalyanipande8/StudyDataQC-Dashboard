import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.simulate_study_domains import simulate, DOMAINS
from src.quality_checks import run_all_checks


def test_6_domains_defined():
    assert len(DOMAINS) == 6


def test_at_least_1200_records():
    datasets = simulate()
    total = sum(len(df) for df in datasets.values())
    assert total >= 1200


def test_exactly_15_checks_run():
    datasets = simulate()
    checks = run_all_checks(datasets)
    assert len(checks) == 15


def test_completeness_checks_detect_real_missingness():
    datasets = simulate()
    checks = run_all_checks(datasets)
    for domain in DOMAINS:
        assert checks[f"{domain}_completeness"]["n_missing"] > 0


def test_range_checks_detect_real_out_of_range_values():
    datasets = simulate()
    checks = run_all_checks(datasets)
    for domain in DOMAINS:
        assert checks[f"{domain}_range"]["n_out_of_range"] > 0
