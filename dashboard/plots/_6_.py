# question6_table.py
import streamlit as st
import pandas as pd

def show_low_stock_turnover(df):
    # Filter and aggregate
    low_turnover = (
        df[df['StockTurnover'] < 1]
        .groupby('VendorName')[['StockTurnover']]
        .mean()
        .sort_values('StockTurnover', ascending=True)
        .head(10)
        .reset_index()
    )

    st.subheader("Top 10 Vendors with Low Stock Turnover")
    st.dataframe(low_turnover)
