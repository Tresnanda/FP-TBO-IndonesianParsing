import streamlit as st
from module.cnf import *
from module.cyk import *
import pandas as pd

st.header("Parsing Bahasa Indonesia Menggunakan Algoritma CYK")

rule = run_conversion()

kalimat = st.text_input("Kalimat yang ingin dicek", placeholder='Masukkan kalimat disini')
n = len(kalimat.split())

if not kalimat:
    st.write("Kalimat tidak boleh kosong!")
else:
    table = parse(kalimat)
    if 'K' in table[0][0]:
        st.write(f'Kalimat "{kalimat}" adalah kalimat :green[valid!]')
    else:
        st.write(f'Kalimat "{kalimat}" adalah kalimat :red[tidak valid!]')
    st.write(f"Tabel pengisian CYK kalimat '{kalimat}' adalah sebagai berikut: ")
    #table_str = [[str(cell) for cell in row] for row in table]
    table_str = [['Ø' if not cell else str(cell) for cell in row] for row in table]
    triangular_table = [[table_str[i][j] if j <= i else '' for j in range(n)] for i in range(n)]
    #st.table(tabulate(table, headers=[f"{idx}" for idx in range(n)], tablefmt="fancy_grid"))
    st.table(triangular_table)