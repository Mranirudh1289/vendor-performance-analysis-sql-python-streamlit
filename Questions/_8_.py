# question8.py
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats

def confidence_interval(data, confidence=0.95):
    mean_val = np.mean(data)
    std_err = np.std(data, ddof=1) / np.sqrt(len(data)) # Standard error !!
    t_critical = stats.t.ppf((1 + confidence) / 2, df=len(data) - 1)
    margin_of_err = t_critical * std_err
    return mean_val, mean_val - margin_of_err, mean_val + margin_of_err

def plot_profit_margin_ci(df):
    # Define top and low vendors
    top_thresold = df['TotalSalesDollars'].quantile(0.75)
    low_thresold = df['TotalSalesDollars'].quantile(0.25)

    top_vendors = df[df['TotalSalesDollars'] >= top_thresold]['ProfitMargin'].dropna()
    low_vendors = df[df['TotalSalesDollars'] >= low_thresold]['ProfitMargin'].dropna()

    # Calculate CI
    top_mean, top_lower, top_upper = confidence_interval(top_vendors)
    low_mean, low_lower, low_upper = confidence_interval(low_vendors)

    st.write(f"**Top Vendors 95% CI:** ({top_lower:.2f}, {top_upper:.2f}), Mean: {top_mean:.2f}")
    st.write(f"**Low Vendors 95% CI:** ({low_lower:.2f}, {low_upper:.2f}), Mean: {low_mean:.2f}")

    # Plot
    fig, ax = plt.subplots(figsize=(12, 6))

    # Top vendors
    sns.histplot(top_vendors, kde=True, color='blue', bins=30, alpha=0.5, label='Top Vendors', ax=ax)
    ax.axvline(top_lower, color='blue', linestyle='--', label=f'Top Lower: {top_lower:.2f}')
    ax.axvline(top_upper, color='blue', linestyle='--', label=f'Top Upper: {top_upper:.2f}')
    ax.axvline(top_mean, color='blue', linestyle='-', label=f'Top Mean: {top_mean:.2f}')

    # Low vendors
    sns.histplot(low_vendors, kde=True, color='red', bins=30, alpha=0.5, label='Low Vendors', ax=ax)
    ax.axvline(low_lower, color='red', linestyle='--', label=f'Low Lower: {low_lower:.2f}')
    ax.axvline(low_upper, color='red', linestyle='--', label=f'Low Upper: {low_upper:.2f}')
    ax.axvline(low_mean, color='red', linestyle='-', label=f'Low Mean: {low_mean:.2f}')

    # Finalize
    ax.set_title('Confidence Interval Comparison: Top vs Low Vendors (Profit Margin)')
    ax.set_xlabel('Profit Margin (%)')
    ax.set_ylabel('Frequency')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
