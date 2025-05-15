# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:48:37 2025

@author: USER
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data_mobile = pd.read_csv('mobile.csv')
data_dekstop = pd.read_csv('dekstop.csv')

x = data_mobile['Date']
y1 = data_mobile['Origins']
y2 = data_dekstop['Origins']
y3 = data_mobile['Percent good CWV']
y4 = data_dekstop['Percent good CWV']

fig = make_subplots(rows=2, cols=1, subplot_titles=("Berdasarkan Jumlah penggunaan", "Berdasarkan persen CWV"))
fig.add_trace(go.Scatter(
    x=x,
    y=y1,
    mode='lines+markers',  # Garis dengan penanda
    name='Data Mobile',         # Nama untuk legend
    line=dict(color='blue')
),row = 1, col=1)
fig.add_trace(go.Scatter(
    x=x,
    y=y2,
    mode='lines+markers',
    name='Data Dekstop',
    line=dict(color='red')
),row = 1, col=1)

fig.add_trace(go.Scatter(
    x=x,
    y=y3,
    mode='lines+markers',  # Garis dengan penanda
    name='Data Mobile',         # Nama untuk legend
    line=dict(color='blue')
),row = 2, col=1)
fig.add_trace(go.Scatter(
    x=x,
    y=y4,
    mode='lines+markers',
    name='Data Dekstop',
    line=dict(color='red')
),row = 2, col=1)

fig.update_layout(
    title="Perkembangan penggunaan teknologi 'React' selama enam bulan terakhir",
    xaxis_title="Bulan",
    yaxis_title="Penggunaan",
    template="plotly_white"
)
fig.show()
fig.write_html("grafik data mobile dan dekstop.html")

fig2 = make_subplots(rows=2, cols=1, subplot_titles=("Berdasarkan Jumlah penggunaan", "Berdasarkan persen CWV"))
fig2.add_trace(go.Scatter(
    x=x,
    y=y1,
    mode='lines+markers',  # Garis dengan penanda
    name='Data Mobile',         # Nama untuk legend
    line=dict(color='blue')
),row = 1, col=1)
fig2.add_trace(go.Scatter(
    x=x,
    y=y3,
    mode='lines+markers',  # Garis dengan penanda
    name='Data Mobile',         # Nama untuk legend
    line=dict(color='blue')
),row = 2, col=1)
fig2.update_layout(
    title="Perkembangan penggunaan teknologi 'React' selama enam bulan terakhir",
    xaxis_title="Bulan",
    yaxis_title="Penggunaan",
    template="plotly_white"
)
fig2.show()
fig2.write_html("grafik data mobile.html")

fig3 = make_subplots(rows=2, cols=1, subplot_titles=("Berdasarkan Jumlah penggunaan", "Berdasarkan persen CWV"))
fig3.add_trace(go.Scatter(
    x=x,
    y=y2,
    mode='lines+markers',  # Garis dengan penanda
    name='Data Dekstop',         # Nama untuk legend
    line=dict(color='blue')
),row = 1, col=1)
fig3.add_trace(go.Scatter(
    x=x,
    y=y4,
    mode='lines+markers',  # Garis dengan penanda
    name='Data Dekstop',         # Nama untuk legend
    line=dict(color='blue')
),row = 2, col=1)
fig3.update_layout(
    title="Perkembangan penggunaan teknologi 'React' selama enam bulan terakhir",
    xaxis_title="Bulan",
    yaxis_title="Penggunaan",
    template="plotly_white"
)
fig3.show()
fig3.write_html("grafik data dekstop.html")
