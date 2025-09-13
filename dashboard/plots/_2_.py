# question2.py
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def format_dollars(x):
    return f"${x:,.0f}"

def plot_top_vendors_brands(df):
    # Prepare top vendors and top brands
    top_vendors = df.groupby('VendorName')['TotalSalesDollars'].sum().nlargest(10)
    top_brands = df.groupby('Description')['TotalSalesDollars'].sum().nlargest(10)

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Top Vendors
    ax1 = sns.barplot(y=top_vendors.index, x=top_vendors.values, palette='Blues_r', ax=axes[0])
    axes[0].set_title('Top 10 Vendors By Sales')
    for bar in ax1.patches:
        ax1.text(
            bar.get_width() + (bar.get_width() * 0.02),
            bar.get_y() + bar.get_height() / 2,
            format_dollars(bar.get_width()),
            ha='left',
            va='center',
            fontsize=10,
            color='black'
        )

    # Top Brands
    ax2 = sns.barplot(y=top_brands.index.astype(str), x=top_brands.values, palette='Reds_r', ax=axes[1])
    axes[1].set_title('Top 10 Brands By Sales')
    for bar in ax2.patches:
        ax2.text(
            bar.get_width() + (bar.get_width() * 0.02),
            bar.get_y() + bar.get_height() / 2,
            format_dollars(bar.get_width()),
            ha='left',
            va='center',
            fontsize=10,
            color='black'
        )

    plt.tight_layout()
    st.pyplot(fig)
