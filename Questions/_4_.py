# question4.py
import streamlit as st
import matplotlib.pyplot as plt

def plot_top10_vendor_donut(df):
    # Aggregate and calculate contribution %
    vendor_performance = df.groupby('VendorName')['TotalPurchaseDollars'].sum().sort_values(ascending=False).reset_index()
    vendor_performance['PurchaseContribution%'] = vendor_performance['TotalPurchaseDollars'] / vendor_performance['TotalPurchaseDollars'].sum() * 100

    top_vendors = vendor_performance.head(10)

    vendors = list(top_vendors['VendorName'].values)
    purchase_contributions = list(top_vendors['PurchaseContribution%'].values)
    total_contributions = sum(purchase_contributions)
    remaining_contribution = 100 - total_contributions

    # Append 'Other Vendors'
    vendors.append('Other Vendors')
    purchase_contributions.append(remaining_contribution)

    # Plot Donut Chart
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        purchase_contributions, labels=vendors, autopct='%1.1f%%', startangle=140,
        pctdistance=0.85, colors=plt.cm.Paired.colors
    )

    # Draw center circle for donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)

    # Add total contribution annotation in center
    plt.text(0, 0, f'Top 10 Total:\n{total_contributions:.2f}%', fontsize=14, fontweight='bold', ha='center', va='center')

    plt.title("Top 10 Vendor's Purchase Contribution (%)")
    plt.tight_layout()
    st.pyplot(fig)
