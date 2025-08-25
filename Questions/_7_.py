# question7_table.py
import streamlit as st
import pandas as pd

def format_dollars(x):
    return f"${x:,.0f}"

def show_unsold_inventory(df):
    # Aggregate unsold inventory per vendor
    inventory_value_per_vendor = df.groupby('VendorName')['UnsoldInventoryValue'].sum().reset_index()

    # Sort descending
    inventory_value_per_vendor = inventory_value_per_vendor.sort_values(by='UnsoldInventoryValue', ascending=False)

    # Format as dollars
    inventory_value_per_vendor['UnsoldInventoryValue'] = inventory_value_per_vendor['UnsoldInventoryValue'].apply(format_dollars)

    # Show top 10
    st.subheader("Top 10 Vendors with Highest Unsold Inventory Value")
    st.dataframe(inventory_value_per_vendor.head(10))
