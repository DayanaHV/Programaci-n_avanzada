#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("Conjunto de datos FALLECIDOS COVID")

@st.experimental_memo
def download_data():
   url="https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid.csv"
   df=pd.read_csv("fallecidos_covid.csv")
   return df
c=download_data()

st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)

df=c

st.sidebar.header("Entradas del usuario")
año_seleccionado=st.sidebar.selectbox('Edad', list(reversed(range(0,111))))
filt=(df["EDAD_DECLARADA"]==año_seleccionado)
df[filt]

departamentos=["AMAZONAS","ANCASH","APURIMAC","AREQUIPA","AYACUCHO","CAJAMARCA","CALLAO","CUSCO","HUANCAVELICA","HUANUCO","ICA","JUNÍN","LA LIBERTAD","LAMBAYEQUE","LIMA","LORETO","MADRE DE DIOS","MOQUEGUA","PASCO","PIURA","PUNO","SAN MARTÍN","TACNA","TUMBES","UCAYALI"]
depa_seleccionado=st.sidebar.multiselect('Departamentos',departamentos,departamentos)
filt=(df["DEPARTAMENTO"]==depa_seleccionado)
df[filt]

sexo=["MASCULINO","FEMENINO"]
sexo_seleccionado=st.sidebar.selectbox("Sexo",sexo,sexo)
filt=(df["DEPARTAMENTO"]==sexo_seleccionado)
df[filt]

