# question9.py
import streamlit as st
import pandas as pd
from scipy.stats import ttest_ind

def ttest_profit_margin(df):
    # Define top and low vendor thresholds
    top_threshold = df['TotalSalesDollars'].quantile(0.75)
    low_threshold = df['TotalSalesDollars'].quantile(0.25)

    # Filter profit margins
    top_vendors = df[df['TotalSalesDollars'] >= top_threshold]['ProfitMargin'].dropna()
    low_vendors = df[df['TotalSalesDollars'] <= low_threshold]['ProfitMargin'].dropna()

    # Perform two-sample T-test
    t_stat, p_value = ttest_ind(top_vendors, low_vendors, equal_var=False)

    # Display results
    st.subheader("T-Test: Profit Margins Top vs Low Vendors")
    st.write(f"T-Statistic: {t_stat:.4f}")
    st.write(f"P-Value: {p_value:.4f}")

    if p_value < 0.05:
        st.success("Reject H₀: There is a significant difference in mean profit margins between top and low-performing vendors.")
    else:
        st.info("Fail to Reject H₀: No significant difference in mean profit margins between top and low-performing vendors.")
