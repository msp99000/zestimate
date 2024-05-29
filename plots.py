import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Assuming zhvi and zori data are loaded as DataFrames
zhvi = pd.read_pickle('data/zhvi.pkl')
zori = pd.read_pickle('data/zori.pkl')

# Streamlit setup
st.title("ZHVI and ZORI Data Visualization")

# Define plot function
def plot_zhvi():
    # Plot 1: ZHVI Distribution by State
    fig1 = px.box(zhvi, x="State", y="ZHVI", title="ZHVI Distribution by State")
    st.plotly_chart(fig1)

    # Plot 2: ZHVI Trend Over Time by State
    fig2 = px.line(zhvi, x="Date", y="ZHVI", color="State", title="ZHVI Trend Over Time by State")
    st.plotly_chart(fig2)

    # Plot 3: ZHVI by Type
    fig3 = px.box(zhvi, x="Type", y="ZHVI", title="ZHVI by Type")
    st.plotly_chart(fig3)

    # Plot 4: ZHVI Average by Year
    zhvi['Year'] = zhvi['Date'].dt.year
    avg_zhvi_year = zhvi.groupby('Year')['ZHVI'].mean().reset_index()
    fig4 = px.bar(avg_zhvi_year, x="Year", y="ZHVI", title="Average ZHVI by Year")
    st.plotly_chart(fig4)

    # Plot 5: ZHVI Monthly Trend
    zhvi['Month'] = zhvi['Date'].dt.to_period('M').astype('str')
    monthly_trend = zhvi.groupby('Month')['ZHVI'].mean().reset_index()
    fig5 = px.line(monthly_trend, x="Month", y="ZHVI", title="Monthly ZHVI Trend")
    st.plotly_chart(fig5)

    # Plot 6: ZHVI by Region
    fig6 = px.scatter(zhvi, x="Region", y="ZHVI", color="State", title="ZHVI by Region")
    st.plotly_chart(fig6)

    # Plot 7: ZHVI Heatmap by State and Type
    heatmap_data = zhvi.pivot_table(values='ZHVI', index='State', columns='Type', aggfunc='mean').reset_index()
    fig7 = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data['State'],
        colorscale='Viridis'
    ))
    fig7.update_layout(title="ZHVI Heatmap by State and Type")
    st.plotly_chart(fig7)

    # Plot 8: ZHVI Weekly Trend
    zhvi['Week'] = zhvi['Date'].dt.to_period('W').astype('str')
    weekly_trend = zhvi.groupby('Week')['ZHVI'].mean().reset_index()
    fig8 = px.line(weekly_trend, x="Week", y="ZHVI", title="Weekly ZHVI Trend")
    st.plotly_chart(fig8)

def plot_zori():
    # Plot 1: ZORI Distribution by State
    fig1 = px.box(zori, x="State", y="ZORI", title="ZORI Distribution by State")
    st.plotly_chart(fig1)

    # Plot 2: ZORI Trend Over Time by State
    fig2 = px.line(zori, x="Date", y="ZORI", color="State", title="ZORI Trend Over Time by State")
    st.plotly_chart(fig2)

    # Plot 3: ZORI by Type
    fig3 = px.box(zori, x="Type", y="ZORI", title="ZORI by Type")
    st.plotly_chart(fig3)

    # Plot 4: ZORI Average by Year
    zori['Year'] = zori['Date'].dt.year
    avg_zori_year = zori.groupby('Year')['ZORI'].mean().reset_index()
    fig4 = px.bar(avg_zori_year, x="Year", y="ZORI", title="Average ZORI by Year")
    st.plotly_chart(fig4)

    # Plot 5: ZORI Monthly Trend
    zori['Month'] = zori['Date'].dt.to_period('M').astype('str')
    monthly_trend = zori.groupby('Month')['ZORI'].mean().reset_index()
    fig5 = px.line(monthly_trend, x="Month", y="ZORI", title="Monthly ZORI Trend")
    st.plotly_chart(fig5)

    # Plot 6: ZORI by Region
    fig6 = px.scatter(zori, x="Region", y="ZORI", color="State", title="ZORI by Region")
    st.plotly_chart(fig6)

    # Plot 7: ZORI Heatmap by State and Type
    heatmap_data = zori.pivot_table(values='ZORI', index='State', columns='Type', aggfunc='mean').reset_index()
    fig7 = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data['State'],
        colorscale='Viridis'
    ))
    fig7.update_layout(title="ZORI Heatmap by State and Type")
    st.plotly_chart(fig7)

    # Plot 8: ZORI Weekly Trend
    zori['Week'] = zori['Date'].dt.to_period('W').astype('str')
    weekly_trend = zori.groupby('Week')['ZORI'].mean().reset_index()
    fig8 = px.line(weekly_trend, x="Week", y="ZORI", title="Weekly ZORI Trend")
    st.plotly_chart(fig8)

# Create tabs for ZHVI and ZORI
# tab1, tab2 = st.tabs(["ZHVI", "ZORI"])

# with tab1:
#     plot_zhvi()

# with tab2:
#     plot_zori()
