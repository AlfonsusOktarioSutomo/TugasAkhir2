import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
import webbrowser
import tempfile
import os
from data_real import get_pivot
from data_real import get_percent

# Contoh data

df = get_pivot()
df.index = pd.to_datetime(df.index)

df_persen = get_percent()
df_persen.index = pd.to_datetime(df_persen.index)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Perkembangan Teknologi Web di Dunia")

        ttk.Label(root, text="Pilih Teknologi:").pack()

        self.checkbox_frame = ttk.Frame(root)
        self.checkbox_frame.pack()

        self.tech_vars = {}
        for tech in df.columns:
            var = tk.BooleanVar(value=False)
            cb = ttk.Checkbutton(self.checkbox_frame, text=tech, variable=var)
            cb.pack(anchor='w')
            self.tech_vars[tech] = var

        frame = ttk.Frame(root)
        frame.pack(pady=10)

        ttk.Label(frame, text="Dari (YYYY-MM):").grid(row=0, column=0)
        self.start_var = tk.StringVar(value=df.index[0])
        self.start_entry = ttk.Entry(frame, textvariable=self.start_var, width=10)
        self.start_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Sampai (YYYY-MM):").grid(row=0, column=2)
        self.end_var = tk.StringVar(value=df.index[-1])
        self.end_entry = ttk.Entry(frame, textvariable=self.end_var, width=10)
        self.end_entry.grid(row=0, column=3)

        # Pilihan jumlah atau persentase
        mode_frame = ttk.Frame(root)
        mode_frame.pack(pady=10)
        ttk.Label(mode_frame, text="Tampilkan berdasarkan:").pack(anchor='w')

       


        self.btn = ttk.Button(root, text="Tampilkan Grafik", command=self.show_plot)
        self.btn.pack(pady=5)

    def show_plot(self):
     selected_techs = [tech for tech, var in self.tech_vars.items() if var.get()]
 
     if not selected_techs:
         messagebox.showwarning("Pilih teknologi", "Silakan pilih minimal satu teknologi.")
         return
 
     try:
         start = pd.to_datetime(self.start_var.get())
         end = pd.to_datetime(self.end_var.get())
     except Exception:
         messagebox.showerror("Format tanggal salah", "Format tanggal harus YYYY-MM.")
         return
 
     mode = self.mode_var.get()
     # Pilih dataframe yang sesuai
     if mode == "jumlah":
         df_to_use = df
         y_title = "Jumlah Penggunaan"
     else:
         df_to_use =df_persen
         y_title = "Persentase (%)"
 
     filtered = df_to_use[(df_to_use.index >= start) & (df_to_use.index <= end)]
 
     if filtered.empty:
         messagebox.showwarning("Data kosong", "Tidak ada data pada rentang waktu tersebut.")
         return
 
     fig = go.Figure()
     for tech in selected_techs:
         fig.add_trace(go.Scatter(x=filtered.index, y=filtered[tech], mode='lines+markers', name=tech))
 
     fig.update_layout(
         title=f'Perkembangan Teknologi dari {start.strftime("%Y-%m")} sampai {end.strftime("%Y-%m")} ({y_title})',
         xaxis_title='Bulan',
         yaxis_title=y_title
     )
 
     with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
         plot(fig, filename=f.name, auto_open=False)
         webbrowser.open('file://' + os.path.realpath(f.name))



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
