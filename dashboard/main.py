import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import scipy.stats as stats
import math
from plots._1_ import plot_brand_performance
from plots._2_ import plot_top_vendors_brands
from plots._3_ import plot_vendor_contribution
from plots._4_ import plot_top10_vendor_donut
from plots._5_ import plot_bulk_purchase_impact
from plots._6_ import show_low_stock_turnover
from plots._7_ import show_unsold_inventory
from plots._8_ import plot_profit_margin_ci
from plots._9_ import ttest_profit_margin

# Load your analyzed data :-
df = pd.read_csv("./data/mydata.csv")

st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;  /* reduce top padding */
        padding-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Vendor Performance Analysis")

# Short Project Description
st.markdown("""
This is a **real-world, company-level** Data Analytics project which simulates how data analysts solve business problems: starting with SQL for data extraction, Python (Pandas, Matplotlib, Seaborn) for cleaning & analysis, and Streamlit for building an interactive dashboard. The goal is to uncover **vendor performance, sales trends, and actionable insights** — just like in an actual business scenario.
""")

st.text("") 

# Show data preview :-
with st.expander("📂 Preview Dataset"):
    st.write("Showing first 5 rows of the dataset:")
    st.dataframe(df.head())  

with st.expander("📊 Dataset Info"):
    st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Show rows & columns as metrics :-
    col1, col2 = st.columns(2)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    # Show column names :-
    st.write("Columns:", list(df.columns))

with st.expander("📈 Summary Statistics"):
    st.write("Basic statistical overview of the dataset:")
    st.dataframe(df.describe().T)

# Big label using markdown above the selectbox
st.markdown("<h2 style='font-size:20px; font-weight:;'>Select to analyse the vendor performance:</h2>", unsafe_allow_html=True)

questions = st.selectbox(
    "",  # Leave empty because we put the label above
    [
        'Brands for promotional or pricing adjustments',
        'Top 10 Vendors and Brands By Sales',
        'Vendor Contribution To Total Purchase',
        "Top 10 Vendor's Purchase Contribution (%)",
        'Impact Of Bulk Purchase On Unit Price',
        'StockTurnover',
        'Unsold inventory per vendor and vendors contribute the most to it',
        'Top vs Low Vendors (Profit Margin)',
        'Profit margins between top-performing and low-performing vendors'
    ],
    key="vendor_analysis"
)

st.text("") 

# Add a button to trigger the analysis
if st.button("🔍 Analyse"):
    if questions == 'Brands for promotional or pricing adjustments': 
        plot_brand_performance(df)

    elif questions == 'Top 10 Vendors and Brands By Sales':
        plot_top_vendors_brands(df)

    elif questions == 'Vendor Contribution To Total Purchase':
        plot_vendor_contribution(df)

    elif questions == "Top 10 Vendor's Purchase Contribution (%)":
        plot_top10_vendor_donut(df)

    elif questions == 'Impact Of Bulk Purchase On Unit Price':
        plot_bulk_purchase_impact(df)

    elif questions == 'StockTurnover':
        show_low_stock_turnover(df)

    elif questions == 'Unsold inventory per vendor and vendors contribute the most to it':
        show_unsold_inventory(df)

    elif questions == 'Top vs Low Vendors (Profit Margin)':
        plot_profit_margin_ci(df)

    elif questions == 'Profit margins between top-performing and low-performing vendors':
        ttest_profit_margin(df)