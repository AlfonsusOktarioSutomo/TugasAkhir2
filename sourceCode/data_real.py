# -*- coding: utf-8 -*-
"""
Created on Mon May  5 18:31:17 2025

@author: frans
"""

import pandas as pd
import plotly.graph_objects as go


#Cleaning
df = pd.read_csv('data_real.csv')
df = df[df['technology'] != " "]
df = df[df['technology'] != " 0); border-style: none; margin: 0px; border-radius: 0px; padding: 0px;"]
df = df[df['technology'] != " 255"]
df = df[df['technology'] != " 1.11.3"]
df = df[df['technology'] != " 2017"]
df = df[~df['date'].str.contains('2018-')]
x = df[['technology']]
tekno_anomali = [" (Math.PI / 180) * 360", " 0", " 1"," 15.06.2017", " 2022", " 255);", " 255); border-style: none; margin: 0px; border-radius: 0px; padding: 0px;"]
for x in tekno_anomali:
    df = df[df['technology'] != x]
    
#Semua client
df_gb_date = df.groupby('date').sum('f0_')
df_pivot_baru= df.pivot_table(index='date', columns='technology', values='f0_')
df3 = df_pivot_baru
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
fig.write_html("sample jumlah real.html")

#persentase
df_pivot_baru['jumlah'] = df_pivot_baru.sum(axis=1)
df_pivot['jumlah'] = df_pivot_baru['jumlah']

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
fig2.write_html("sample persentase real.html")

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
    
    #Persentase
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
    fig2.write_html(f"sample persentase {client} real.html")
    
visualisasi('mobile')
visualisasi('desktop')

def perbandingan(tekno1,tekno2):

    df_pivot_baru = df3
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(x=df_pivot_baru.index, y=df_pivot_baru[f'{tekno1}'], mode='lines+markers', name=f'{tekno1}'))
    fig2.add_trace(go.Scatter(x=df_pivot_baru.index, y=df_pivot_baru[f'{tekno2}'], mode='lines+markers', name=f'{tekno2}'))
    
    fig2.update_layout(
        title=f"Perbandingan jumlah penggunaan teknologi {tekno1} dan {tekno2}",
        xaxis_title="Tanggal",
        yaxis_title="Jumlah penggunaan",
        template="plotly_white"
    )
    fig2.show()
    fig2.write_html(f"sample {tekno1,tekno2}.html")
    
    #persentase
    
    df_pivot_baru['jumlah'] = df_pivot_baru.sum(axis=1)
    #df2_pivot.to_excel(f"10 teknologi populer {client}.xlsx")
    for i in df_pivot_baru.columns:
          df_pivot_baru[i] = df_pivot_baru[i]/df_pivot_baru['jumlah']
    
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(x=df_pivot_baru.index, y=df_pivot_baru[f'{tekno1}'], mode='lines+markers', name=f'{tekno1}'))
    fig2.add_trace(go.Scatter(x=df_pivot_baru.index, y=df_pivot_baru[f'{tekno2}'], mode='lines+markers', name=f'{tekno2}'))    
    fig2.update_layout(
        title=f"Perbandingan persentase penggunaan teknologi {tekno1} dan {tekno2}",
        xaxis_title="Tanggal",
        yaxis_title="Peresentase penggunaan",
        template="plotly_white"
    )
    fig2.show()
    fig2.write_html(f"sample persentase {tekno1,tekno2}.html")
    
perbandingan('jQuery', 'Angular')

def get_pivot():
    df = pd.read_csv('data_real.csv')
    df = df[df['technology'] != " "]
    df = df[df['technology'] != " 0); border-style: none; margin: 0px; border-radius: 0px; padding: 0px;"]
    df = df[df['technology'] != " 255"]
    df = df[df['technology'] != " 1.11.3"]
    df = df[df['technology'] != " 2017"]
    df = df[~df['date'].str.contains('2018-')]
    tekno_anomali = [" (Math.PI / 180) * 360", " 0", " 1"," 15.06.2017", " 2022", " 255);", " 255); border-style: none; margin: 0px; border-radius: 0px; padding: 0px;"]
    for x in tekno_anomali:
        df = df[df['technology'] != x]
        
    df_gb = df.groupby(["technology"]).sum('f0_')
    df_sorted = df_gb.sort_values(by='f0_', ascending=False)
    df_10 = df_sorted.head(10)
    df_baru = df.loc[df['technology'].isin(df_10.index)]
    df_baru = df_baru[['date','technology','f0_']]
    df_baru.drop_duplicates(subset='date')      
    df_pivot = df_baru.pivot_table(index="date", columns='technology', values='f0_')
    return df_pivot

def get_percent():
   df = pd.read_csv('data_real.csv')
   df = df[df['technology'] != " "]
   df = df[df['technology'] != " 0); border-style: none; margin: 0px; border-radius: 0px; padding: 0px;"]
   df = df[df['technology'] != " 255"]
   df = df[df['technology'] != " 1.11.3"]
   df = df[df['technology'] != " 2017"]
   df = df[~df['date'].str.contains('2018-')]
   tekno_anomali = [" (Math.PI / 180) * 360", " 0", " 1"," 15.06.2017", " 2022", " 255);", " 255); border-style: none; margin: 0px; border-radius: 0px; padding: 0px;"]
   for x in tekno_anomali:
       df = df[df['technology'] != x]
       
   df_pivot_baru= df.pivot_table(index='date', columns='technology', values='f0_')
   df_pivot = get_pivot()
   df_pivot_baru['jumlah'] = df_pivot_baru.sum(axis=1)
   df_pivot['jumlah'] = df_pivot_baru['jumlah']

   for i in df_pivot.columns:
         df_pivot[i] = df_pivot[i]/df_pivot['jumlah']

   df_pivot = df_pivot.drop(columns = 'jumlah')
   
   return df_pivot


fig3 = go.Figure()
 
fig3.add_trace(go.Scatter(x=x.index, y=x, mode='lines+markers', name='jumlah'))    
fig3.update_layout(
    title="Perubahan Jumlah sample",
    xaxis_title="Tanggal",
    yaxis_title="jumlah",
    template="plotly_white"
)
fig3.show()
fig3.write_html("jumlah sample.html")
