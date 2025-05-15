# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data_sample2.csv") 
df_pivot_baru= df.pivot_table(index='date', columns='technology', values='f0_')
df_gb = df.groupby(["technology"]).sum('f0_')
df_sorted = df_gb.sort_values(by='f0_', ascending=False)
df_10 = df_sorted.head(10)
df_baru = df.loc[df['technology'].isin(df_10.index)]
df_baru = df_baru[['date','technology','f0_']]
df_baru.drop_duplicates(subset='date')      
df_pivot = df_baru.pivot_table(index="date", columns='technology', values='f0_')
fig = go.Figure()
for col in df_pivot.columns:
    fig.add_trace(go.Scatter(x=df_pivot.index, y=df_pivot[col], mode='lines+markers', name=col))
    
fig.update_layout(
    title="Perkembangan 10 teknologi populer",
    xaxis_title="Tanggal",
    yaxis_title="Jumlah penggunaan",
    template="plotly_white"
)
fig.show()
fig.write_html("sample jumlah.html")
df_pivot_baru['jumlah'] = df_pivot_baru.sum(axis=1)
df_pivot['jumlah'] = df_pivot_baru['jumlah']
df_pivot_baru.to_excel("10 teknologi populer.xlsx")
for i in df_pivot.columns:
      df_pivot[i] = df_pivot[i]/df_pivot['jumlah']
df_pivot = df_pivot.drop(columns = 'jumlah')
df_filled = df_pivot.fillna('0')

fig2 = go.Figure()
for col in df_pivot.columns:
    fig2.add_trace(go.Scatter(x=df_pivot.index, y=df_pivot[col], mode='lines+markers', name=col))
    
fig2.update_layout(
    title="Perkembangan 10 teknologi populer",
    xaxis_title="Tanggal",
    yaxis_title="Peresentase penggunaan",
    template="plotly_white"
)
fig2.show()
fig2.write_html("sample persentase.html")

def visualisasi(client):
    df2 = df[df['client'] == client]
    df2_pivot = df2.pivot_table(index='date', columns='technology', values='f0_')
    df_gb = df2.groupby(["technology"]).sum('f0_')
    df_sorted = df_gb.sort_values(by='f0_', ascending=False)
    df_10 = df_sorted.head(10)
    df_baru = df2.loc[df['technology'].isin(df_10.index)]
    df_baru = df_baru[['date','technology','f0_']]
    df_baru.drop_duplicates(subset='date')      
    df_pivot = df_baru.pivot_table(index="date", columns='technology', values='f0_')
    fig = go.Figure()
    for col in df_pivot.columns:
        fig.add_trace(go.Scatter(x=df_pivot.index, y=df_pivot[col], mode='lines+markers', name=col))
        
    fig.update_layout(
        title=f"Perkembangan 10 teknologi populer untuk client {client}",
        xaxis_title="Tanggal",
        yaxis_title="Jumlah penggunaan",
        template="plotly_white"
    )
    fig.show()
    fig.write_html(f"sample jumlah {client}.html")
    df2_pivot['jumlah'] = df2_pivot.sum(axis=1)
    df_pivot['jumlah'] = df2_pivot['jumlah']
    df2_pivot.to_excel(f"10 teknologi populer {client}.xlsx")
    for i in df_pivot.columns:
          df_pivot[i] = df_pivot[i]/df_pivot['jumlah']
    df_pivot = df_pivot.drop(columns = 'jumlah')

    fig2 = go.Figure()
    for col in df_pivot.columns:
        fig2.add_trace(go.Scatter(x=df_pivot.index, y=df_pivot[col], mode='lines+markers', name=col))
        
    fig2.update_layout(
        title=f"Perkembangan 10 teknologi populer untuk client {client}",
        xaxis_title="Tanggal",
        yaxis_title="Peresentase penggunaan",
        template="plotly_white"
    )
    fig2.show()
    fig2.write_html(f"sample persentase {client}.html")
    

visualisasi("mobile")
visualisasi("desktop")