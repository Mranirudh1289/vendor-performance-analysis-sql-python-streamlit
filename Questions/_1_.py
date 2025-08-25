def plot_brand_performance(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import streamlit as st

    # Prepare data inside the function
    brand_performance = df.groupby("Brand").agg({
        "TotalSalesDollars": "sum",
        "ProfitMargin": "mean"
    }).reset_index()

    low_sales_threshold = brand_performance['TotalSalesDollars'].quantile(0.15)
    high_margin_threshold = brand_performance['ProfitMargin'].quantile(0.85)
    target_brands = target_brands = brand_performance[
    (brand_performance['TotalSalesDollars'] <= low_sales_threshold) &
    (brand_performance['ProfitMargin'] >= high_margin_threshold)]

    brand_performance = brand_performance[brand_performance["TotalSalesDollars"] < 10000]

    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(data=brand_performance, x='TotalSalesDollars', y='ProfitMargin',
                    color='blue', label='All Brands', alpha=0.2)
    sns.scatterplot(data=target_brands, x='TotalSalesDollars', y='ProfitMargin',
                    color='red', label='Target Brands')

    ax.axhline(high_margin_threshold, linestyle='--', color='black', label='High Margin Threshold')
    ax.axvline(low_sales_threshold, linestyle='--', color='black', label='Low Sales Threshold')

    ax.set_xlabel('Total Sales ($)')
    ax.set_ylabel('Profit Margin (%)')
    ax.set_title('Brands for promotional or pricing adjustment')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
