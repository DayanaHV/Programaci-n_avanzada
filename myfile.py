#$ pip install streamlit --upgrade
import urllib.request
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np



#TITULO
st.title('Fallecidos por COVID-19 - [Ministerio de Salud - MINSA]')
st.write("------------------------------------------------------------------------------------------------")
st.markdown("**PROYECTO FINAL PROGRAMACIÓN 2022-2**")

#INTRODUCCIÓN
image_INTRODUCCION = Image.open('INTRODUCCION.jpg')
st.image(image_INTRODUCCION)

#IMAGEN PORTADA
imagen_portada = Image.open('imagenportada.jpg')
st.image(imagen_portada)

st.markdown("""
	Esta app permite al usuario visualizar los datos de fallecidos por COVID-19
	* **Base de datos:** [MINAM-Ministerio de Salud del Perú (https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa).
	""")


#CRITERIOS
st.subheader("**CRITERIOS TECNICOS**")    
st.write("""A partir del 31.mayo.2021 se cambió el criterio de “Fallecidos por Covid-19” por “Muertes por Covid-19” y como resultado el dataset creció casi al triple en el número de registros. Esta nueva clasificación está definida por el cumplimiento de al menos uno de los siguientes siete criterios técnicos:""")
image_CRITERIOS = Image.open('CRITERIOS.jpg')
st.image(image_CRITERIOS)

#CONTEXTO
st.write("Con ese contexto, resulta necesario que el país cuente con un registro actualizado del número de personas fallecidas como consecuencia del COVID-19, que permita contar,en el menor tiempo posible con data que ayude a planificar, presupuestar y responder a la pandemia enfocándose en los grupos (sexo y edad) y/o zonas (departamento, provincia y distrito) más afectadas por la pandemia. Además, muestre el impacto que tuvo la pandemia y si las medidas de protección específicas, como la vacunación, están siendo efectivas.")

#OBJETIVO:
st.subheader("**OBJETIVO DE LA PAGINA**")   
st.write("Facilitar la busqueda de datos relacionados a los fallecidos por covid-19 (sexo, edad, departamento, provincia, distrito y ubigeo) para conocer la magnitud del efecto.")

st.subheader("**Variables de la data**") 
st.markdown("""
	* **FECHA CORTE** Fecha de corte de información.
	""")
st.markdown("""
	* **UUID:** ID de la persona fallecida..
	""")
st.markdown("""
	* **FECHA_FALLECIMIENTO:** Fecha de fallecimiento.
	""")
st.markdown("""
	* **EDAD_DECLARADA:** Edad de la persona fallecida.
	""")
st.markdown("""
	* **SEXO:** Sexo de la persona fallecida.
	""")
st.markdown("""
	* **CLASIFICACION_DEF:** Criterios utilizados para la confirmación de la defunción
	""")
st.markdown("""
	* **UBIGEO:** Código de Ubicación Geografica que denotan "DDppdd" (Departamento, provincia,distrito), fuente INEI.
	""")
st.markdown("""
	* **DEPARTAMENTO:** Departamento donde reside la persona fallecida. 
	""")
st.markdown("""
	* **PROVINCIA:** Provincia donde reside la persona fallecida.
	""")
st.markdown("""
	* **DISTRITO:** Distrito donde reside la persona fallecida.
	""")
st.header("DATA FALLECIDOS COVID")
@st.experimental_memo
def download_data():
   url="https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid.csv"
   df=pd.read_csv("fallecidos_covid.csv")
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

st.subheader('Relaión provincia-edad_declrada') 
#url del archivo en formato raw
url = 'https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid%20(3)%20(2).csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='CLASIFICACION_DEF', y='DEPARTAMENTO')

#VIDEO DE YOUTUBE
st.subheader("**VIDEO INFORMATIVO DE LA PROBLEMATICA**")    
video_file = open('Coronavirus Covid-19_ Claves para entender la enfermedad y protegerse - Clínica Alemana.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("**Fuente**: Clínica Alemana. (2020). https://www.youtube.com/watch?v=vlzxSleRnmg")

#Construccion del set/list de departamentos (Valores unicos sin NA)
set_departamentos = np.sort(df['DEPARTAMENTO'].dropna().unique())
#Seleccion del departamento
opcion_departamento = st.selectbox('Selecciona un departamento', set_departamentos)
df_departamentos = df[df['DEPARTAMENTO'] == opcion_departamento]
num_filas = len(df_departamentos.axes[0]) 

#Construccion del set/list de provincias (Valores unicos sin NA)
set_provincias = np.sort(df_departamentos['PROVINCIA'].dropna().unique())
#Seleccion de la provincia
opcion_provincia = st.selectbox('Selecciona una provincia', set_provincias)
df_provincias = df_departamentos[df_departamentos['PROVINCIA'] == opcion_provincia]
num_filas = len(df_provincias.axes[0]) 

#Construccion del set/list de distritos (Valores unicos sin NA)
set_distritos = np.sort(df_departamentos['DISTRITO'].dropna().unique())
#Seleccion de la distrito
opcion_distrito = st.selectbox('Selecciona un distrito', set_distritos)
df_distritos = df_departamentos[df_departamentos['DISTRITO'] == opcion_distrito]
num_filas = len(df_distritos.axes[0]) 

st.write('Numero de registros:', num_filas)

#Gráficas

#Gráfica de pie de METODODX
df_metododx = df_distritos.METODODX.value_counts()
df_metododx = pd.DataFrame(df_metododx)
df_metododx = df_metododx.reset_index()  
df_metododx.columns = ['METODODX', 'Total']

fig1, ax1 = plt.subplots()
ax1.pie(df_metododx['Total'], labels=df_metododx['METODODX'], autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.write('Distribución por METODODX:')
st.pyplot(fig1)

