
#* streamlit run (file name)
# pip install openpyxl


# import
import pandas as pd
import streamlit as st


#! dataset 1
df1 = pd.read_csv('Web-Developers-Salaries-Egypt-2024.csv' )
st.write( df1 )



#! dataset 2
df2 = pd.read_csv('Cleaned_Wuzzuf_Jobs.csv')
st.write( df2 )



#! dataset 3
df3 = pd.read_excel( 'dataset3.xlsx' )
st.write( df3 )



#! dataset 4
keywords = [
    'not egyptian', 
    'site out of egypt', 
    'foreign', 
    'non egypt', 
    'not egypt'
]

mask = df3.apply(lambda row: row.astype(str).str.lower().str.contains('|'.join(keywords)).any(), axis=1)

df3_clean = df3[~mask]

st.write(df3_clean)