#$ pip install streamlit --upgrade
import urllib.request
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

st.header("DATA DE FALLECIDOS POR COVID-19")
@st.experimental_memo
def download_data():
   url="https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid.csv"
   df=pd.read_csv("fallecidos_covid.csv")
   return df
c=download_data()

c=download_data()
st.write('*Dimensiones de la tabla:*') 
st.write('* Fila: ' + str(c.shape[0]))
st.write('* Columnas: ' + str(c.shape[1]))
st.dataframe(c)

st.subheader("Características del Dataset")
st.write(c.describe())

st.subheader('Relción de ') 
url = 'https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid%20(3)%20(1).csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='CLASIFICACION_DEF', y='DEPARTAMENTO')



#TITULO
st.title('Fallecidos por COVID-19 - [Ministerio de Salud - MINSA]')
st.markdown("*PROYECTO FINAL PROGRAMACIÓN 2022-2*")
st.write("------------------------------------------------------------------------------------------------")

#IMAGEN PORTADA
imagen_portada = Image.open('imagenportada.jpg')
st.image(imagen_portada)



#INTRODUCCIÓN
image_INTRODUCCION = Image.open('INTRODUCCION.jpg')
st.image(image_INTRODUCCION)

st.markdown("""
	Esta app permite al usuario visualizar los datos de fallecidos por COVID-19
	* *Base de datos:* [MINAM-Ministerio de Salud del Perú (https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa).
	""")


#CRITERIOS
st.subheader("*CRITERIOS TECNICOS*")    
st.write("""A partir del 31.mayo.2021 se cambió el criterio de “Fallecidos por Covid-19” por “Muertes por Covid-19” y como resultado el dataset creció casi al triple en el número de registros. Esta nueva clasificación está definida por el cumplimiento de al menos uno de los siguientes siete criterios técnicos:""")
image_CRITERIOS = Image.open('CRITERIOS.jpg')
st.image(image_CRITERIOS)

#CONTEXTO
st.write("Con ese contexto, resulta necesario que el país cuente con un registro actualizado del número de personas fallecidas como consecuencia del COVID-19, que permita contar,en el menor tiempo posible con data que ayude a planificar, presupuestar y responder a la pandemia enfocándose en los grupos (sexo y edad) y/o zonas (departamento, provincia y distrito) más afectadas por la pandemia. Además, muestre el impacto que tuvo la pandemia y si las medidas de protección específicas, como la vacunación, están siendo efectivas.")

#OBJETIVO:
st.subheader("*OBJETIVO DE LA PAGINA*")   
st.write("Facilitar la busqueda de datos relacionados a los fallecidos por covid-19 (sexo, edad, departamento, provincia, distrito y ubigeo) para conocer la magnitud del efecto.")

st.subheader("*Variables de la data*") 
st.markdown("""
	* *FECHA CORTE* Fecha de corte de información.
	""")
st.markdown("""
	* *UUID:* ID de la persona fallecida..
	""")
st.markdown("""
	* *FECHA_FALLECIMIENTO:* Fecha de fallecimiento.
	""")
st.markdown("""
	* *EDAD_DECLARADA:* Edad de la persona fallecida.
	""")
st.markdown("""
	* *SEXO:* Sexo de la persona fallecida.
	""")
st.markdown("""
	* *CLASIFICACION_DEF:* Criterios utilizados para la confirmación de la defunción
	""")
st.markdown("""
	* *UBIGEO:* Código de Ubicación Geografica que denotan "DDppdd" (Departamento, provincia,distrito), fuente INEI.
	""")
st.markdown("""
	* *DEPARTAMENTO:* Departamento donde reside la persona fallecida. 
	""")
st.markdown("""
	* *PROVINCIA:* Provincia donde reside la persona fallecida.
	""")
st.markdown("""
	* *DISTRITO:* Distrito donde reside la persona fallecida.
	""")

#VIDEO DE YOUTUBE
st.subheader("*VIDEO INFORMATIVO DE LA PROBLEMATICA*")    
video_file = open('Coronavirus Covid-19_ Claves para entender la enfermedad y protegerse - Clínica Alemana.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("*Fuente*: Clínica Alemana. (2020). https://www.youtube.com/watch?v=vlzxSleRnmg")






