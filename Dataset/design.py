
#* streamlit run (file name)
# pip install openpyxl


import pandas as pd
import streamlit as st

df = pd.read_csv('Web-Developers-Salaries-Egypt-2024.csv' )
st.write( df )


df2 = pd.read_csv('Cleaned_Wuzzuf_Jobs.csv')
st.write( df2 )


df3 = pd.read_excel( 'dataset3.xlsx' )
st.write( df3 )


df4 = df[df['What Is your Company'] != 'Not Egyptian and site out of egypt']
st.write(df)