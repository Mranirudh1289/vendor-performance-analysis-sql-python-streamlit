# question5.py
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bulk_purchase_impact(df):
   
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='OrderSize', y='UnitPurchasePrice', palette='Set2', ax=ax)
    
    ax.set_title('Impact Of Bulk Purchase On Unit Price')
    ax.set_xlabel('Order Size')
    ax.set_ylabel('Average Unit Purchase Price')
    
    plt.tight_layout()
    st.pyplot(fig)
