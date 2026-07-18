import streamlit as st
import datetime
import pandas as pd
from engines.data_engine import get_stock_data, calculate_relative_metrics
from engines.chart_engine import plot_performance_and_ratio

# Global UI configuration
st.set_page_config(layout="wide", page_title="Relative Strength Engine")

st.title("📈 Relative Strength Breakout & Base Analyzer")
st.caption("Identify exactly where and when target asset price action shifts velocity relative to key indices or asset baselines.")

# --- Sidebar Inputs Control Layer ---
st.sidebar.header("Configuration Panel")

# Timeframe window selection
today = datetime.date.today()
five_years_ago = today - datetime.timedelta(days=5*365)
start_date = st.sidebar.date_input("Start Boundary Window", value=five_years_ago)
end_date = st.sidebar.date_input("End Boundary Window", value=today)

# Asset configuration arrays
base_input = st.sidebar.text_input("Reference/Base Ticker (e.g., SPY, BTC-USD)", value="SPY").strip().upper()
targets_input = st.sidebar.text_input("Target Tickers to Evaluate (Comma Separated)", value="NVDA, CEG, ASML").strip().upper()

# Array clean-up
target_tickers = [t.strip() for t in targets_input.split(",") if t.strip()]
all_tickers = list(set([base_input] + target_tickers))

if st.sidebar.button("Run Analytics Engine", type="primary"):
    if not base_input or not target_tickers:
        st.sidebar.error("Please supply valid Reference and Target tickers.")
    else:
        with st.spinner("Processing historical pricing data rails..."):
            price_df = get_stock_data(all_tickers, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
            
            if price_df.empty or base_input not in price_df.columns:
                st.error("Failed to compile pricing matrix. Verify ticker inputs or structural dates.")
            else:
                # Calculations
                metrics = calculate_relative_metrics(price_df, base_input, target_tickers)
                
                # Main View layout distribution
                col1, col2 = st.columns([0.75, 0.25])
                
                with col1:
                    st.subheader("Interactive Convergence/Divergence Plot")
                    fig = plot_performance_and_ratio(metrics['indexed'], metrics['ratios'], base_input)
                    st.plotly_chart(fig, use_container_width=True)
                    
                with col2:
                    st.subheader("Relative Matrix Diagnostics")
                    # Calculate net window change metrics
                    last_row = metrics['indexed'].iloc[-1]
                    perf_series = last_row - 100
                    
                    perf_df = pd.DataFrame({
                        "Ticker": perf_series.index,
                        "Window Return (%)": perf_series.values
                    }).sort_values(by="Window Return (%)", ascending=False)
                    
                    st.dataframe(perf_df.style.format({"Window Return (%)": "{:,.2f}%"}), hide_index=True)
                    
                    st.info(
                        "💡 **How to spot the pivot:** In the bottom chart, look for a flattening valley followed by an upward slope. "
                        f"That marks the specific day the target asset began outperforming {base_input}, regardless of market direction."
                    )
else:
    st.info("Adjust ticker assets or window boundaries in the sidebar panel and click 'Run Analytics Engine'.")