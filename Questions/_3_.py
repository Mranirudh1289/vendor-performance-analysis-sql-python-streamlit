# question3.py
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_vendor_contribution(df):
    # Aggregate data
    vendor_performance = df.groupby('VendorName').agg({
        'TotalPurchaseDollars': 'sum',
        'GrossProfit': 'sum',
        'TotalSalesDollars': 'sum'
    }).reset_index()

    # Calculate contribution %
    vendor_performance['PurchaseContribution%'] = vendor_performance['TotalPurchaseDollars'] / vendor_performance['TotalPurchaseDollars'].sum() * 100

    # Select top 10 vendors
    top_vendors = vendor_performance.sort_values('PurchaseContribution%', ascending=False).head(10)
    top_vendors['CumulativeContribution%'] = top_vendors['PurchaseContribution%'].cumsum()

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar plot for Purchase Contribution %
    sns.barplot(
        x=top_vendors['VendorName'], y=top_vendors['PurchaseContribution%'], palette='mako', ax=ax1
    )

    # Annotate bars
    for i, value in enumerate(top_vendors['PurchaseContribution%']):
        ax1.text(i, value - 1, f"{value:.1f}%", ha='center', fontsize=10, color='white')

    # Line plot for Cumulative Contribution %
    ax2 = ax1.twinx()
    ax2.plot(
        top_vendors['VendorName'], top_vendors['CumulativeContribution%'],
        color='red', marker='o', linestyle='dashed', label='Cumulative Contribution %'
    )

    # Labels and title
    ax1.set_xticklabels(top_vendors['VendorName'], rotation=90)
    ax1.set_ylabel('Purchase Contribution %', color='blue')
    ax2.set_ylabel('Cumulative Contribution %', color='red')
    ax1.set_xlabel('Vendors')
    ax1.set_title('Pareto Chart: Vendor Contribution To Total Purchase')

    # Add horizontal line at 100%
    ax2.axhline(y=100, color='gray', linestyle='dashed', alpha=0.7)
    ax2.legend(loc='upper right')

    plt.tight_layout()
    st.pyplot(fig)
