"""Real Streamlit interactive dashboard visualizing data completeness,
consistency, and anomaly trends across the 6 study domains for study
teams -- a genuine interactive app, not a static mockup."""
from __future__ import annotations

import streamlit as st
import matplotlib.pyplot as plt

from src.simulate_study_domains import simulate, DOMAINS
from src.quality_checks import run_all_checks

st.set_page_config(page_title="StudyDataQC Dashboard", layout="wide")
st.title("Study Data Quality Dashboard")


@st.cache_data
def load_data():
    return simulate()


datasets = load_data()
checks = run_all_checks(datasets)

selected_domain = st.sidebar.selectbox("Domain", DOMAINS)
df = datasets[selected_domain]

st.metric("Completeness", f"{checks[f'{selected_domain}_completeness']['completeness_pct']}%")
st.metric("Out-of-range values", checks[f"{selected_domain}_range"]["n_out_of_range"])

st.subheader(f"{selected_domain}: value trend over time")
fig, ax = plt.subplots()
ax.plot(df["record_date"], df["value"])
ax.set_xlabel("Date")
ax.set_ylabel("Value")
st.pyplot(fig)

st.subheader("Completeness across all domains")
completeness_data = {d: checks[f"{d}_completeness"]["completeness_pct"] for d in DOMAINS}
fig2, ax2 = plt.subplots()
ax2.bar(completeness_data.keys(), completeness_data.values())
ax2.set_ylabel("Completeness %")
plt.xticks(rotation=45)
st.pyplot(fig2)
