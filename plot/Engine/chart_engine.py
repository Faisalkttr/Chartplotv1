import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def plot_performance_and_ratio(df_indexed: pd.DataFrame, df_ratios: pd.DataFrame, base_ticker: str):
    """Generates an interactive multi-chart to track outperformance inflection points."""
    
    # Subplot structure: Top handles normalized returns; Bottom handles structural ratio trends
    fig = make_subplots(
        rows=2, cols=1, 
        shared_xaxes=True, 
        vertical_spacing=0.08,
        row_heights=[0.6, 0.4]
    )
    
    # 1. Top Plot: Normalized Cumulative Growth (Base 100)
    for col in df_indexed.columns:
        width = 3 if col == base_ticker else 1.5
        dash = 'dash' if col == base_ticker else 'solid'
        
        fig.add_trace(
            go.Scatter(
                x=df_indexed.index, y=df_indexed[col],
                mode='lines', name=f"{col} (Indexed)",
                line=dict(width=width, dash=dash)
            ),
            row=1, col=1
        )
        
    # 2. Bottom Plot: Direct Ratio Chart (Target / Base Reference)
    for col in df_ratios.columns:
        fig.add_trace(
            go.Scatter(
                x=df_ratios.index, y=df_ratios[col],
                mode='lines', name=f"{col} Ratio"
            ),
            row=2, col=1
        )
        
    # Formatting layout rules
    fig.update_layout(
        height=700,
        title_text="Relative Strength Pivot Analyzer",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=80, b=20)
    )
    
    fig.update_yaxes(title_text="Performance (Base 100)", row=1, col=1)
    fig.update_yaxes(title_text="Ratio Strength Value", row=2, col=1)
    fig.update_xaxes(title_text="Timeline Axis", row=2, col=1)
    
    return fig