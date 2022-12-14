#$ pip install streamlit --upgrade

##################  LIBRERIA IMPORTADA  ##################################
import urllib.request
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np


#TITULO "FALLECIDOS POR COVID-19"
st.title('Fallecidos por COVID-19 - [Ministerio de Salud - MINSA]')
st.markdown("**PROYECTO FINAL PROGRAMACIÓN 2022-2**")

#IMPORTAR LA IMAGEN DE PORTADA
imagen_portada = Image.open('imagenportada.jpg')
st.image(imagen_portada)

#IMPORTAR IMAGEN QUE RESUMA LA INTRODUCCIÓN *elaboración propia de la imagen
image_INTRODUCCION = Image.open('INTRODUCCION.jpg')
st.image(image_INTRODUCCION)

st.write("------------------------------------------------------------------------------------------------")


#DESCRIPCIÓN DE LOS CRITERIOS TECNICOS
st.subheader("**CRITERIOS TECNICOS**")    
st.write("""A partir del 31.mayo.2021 se cambió el criterio de “Fallecidos por Covid-19” por “Muertes por Covid-19” y como resultado el dataset creció casi al triple en el número de registros. Esta nueva clasificación está definida por el cumplimiento de al menos uno de los siguientes siete criterios técnicos:""")
image_CRITERIOS = Image.open('CRITERIOS.jpg')
st.image(image_CRITERIOS)

#CONTEXTO
st.write("Con ese contexto, resulta necesario que el país cuente con un registro actualizado del número de personas fallecidas como consecuencia del COVID-19, que permita contar,en el menor tiempo posible con data que ayude a planificar, presupuestar y responder a la pandemia enfocándose en los grupos (sexo y edad) y/o zonas (departamento, provincia y distrito) más afectadas por la pandemia. Además, muestre el impacto que tuvo la pandemia y si las medidas de protección específicas, como la vacunación, están siendo efectivas.")

#OBJETIVO
st.subheader("**OBJETIVO DE LA PAGINA**")   
st.write("Facilitar la busqueda de datos relacionados a los fallecidos por covid-19 (sexo, edad, departamento, provincia, distrito y ubigeo) para conocer la magnitud del efecto.")

#DESCRIPCIÓN DEL USO DE LA PAGINA WEB
st.markdown("""
	Esta app permite al usuario visualizar los datos de fallecidos por COVID-19
	* **Base de datos:** [MINAM-Ministerio de Salud del Perú (https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa).
	""")


#DESCRIPCIÓN DE kAS VARIABLES DE LA DATA
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

#DESCARGAR LA DATA
st.header("DATA DE FALLECIDOS POR COVID-19")
@st.experimental_memo
def download_data():
   url="https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid.csv"
   df=pd.read_csv("fallecidos_covid.csv")
   return df

#DIMENSIONES Y CARACTERISTICA DE LA DATA
c=download_data()
st.write('**Dimensiones de la tabla:**') 
st.write('* Fila: ' + str(c.shape[0]))
st.write('* Columnas: ' + str(c.shape[1]))
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())

#------------------------------------------------------------------------------------------------------------------------------------

#ENTRADA DEL USUARIO
st.sidebar.header("Entradas del usuario")
#FILTRO DE RANGO DE EDAD_DECLARADA 
edad_select=st.sidebar.selectbox('Edad_declarada', list(reversed(range(0,110))))

def load_data(edad):
	df = download_data()
	df=df.astype({'EDAD_DECLARADA':'str'})
	df['FECHA_CORTE'] = pd.to_numeric(df['FECHA_CORTE'])
	df['FECHA_FALLECIMIENTO'] = pd.to_numeric(df['FECHA_FALLECIMIENTO'])
	df['UUID'] = pd.to_numeric(df['UUID'])
	grouped = df.groupby(df.EDAD_DECLARADA)
	df_edad = grouped.get_group(edad)
	return df_edad

data_EDAD=load_data(str(edad_select))
sorted_DEPARTAMENTO = sorted(data_EDAD.DEPARTAMENTO.unique())
selected_departamento=st.sidebar.multiselect('Departamento', sorted_DEPARTAMENTO, sorted_DEPARTAMENTO)

unique_data=['FECHA_CORTE', 'FECHA_FALLECIMIENTO', 'UUID']
selected_data=st.sidebar.multiselect('Clasificación', unique_data, unique_data)

df_selected=data_EDAD[(data_EDAD.DEPARTAMENTO.isin(selected_departamento))]

def remove_columns(dataset, cols):
	return dataset.drop(cols, axis=1)

cols=np.setdiff1d(unique_data, selected_data)

st.subheader('Mostrar data de distrito(s) y clasificacion(s) seleccionado(s)')
data=remove_columns(df_selected, cols)
st.write('Dimensiones: ' + str(data.shape[0]) + ' filas y ' + str(data.shape[1]) + ' columnas')
st.dataframe(data)


#-----------------------------------------------------------------------------------------------
st.write("------------------------------------------------------------------------------------------------------------------------------------")

set_departamentos = np.sort(c['DEPARTAMENTO'].dropna().unique())
#Seleccion del departamento
opcion_departamento = st.selectbox('Selecciona un departamento', set_departamentos)
df_departamentos = c[c['DEPARTAMENTO'] == opcion_departamento]
num_filas = len(df_departamentos.axes[0]) 

#Construccion del set/list de provincias (Valores unicos sin NA)
set_provincias = np.sort(df_departamentos['PROVINCIA'].dropna().unique())

#Seleccion de la provincia
opcion_provincia = st.selectbox('Selecciona una provincia', set_provincias)
df_provincias = df_departamentos[df_departamentos['PROVINCIA'] == opcion_provincia]
num_filas = len(df_provincias.axes[0]) 

set_distritos = np.sort(df_departamentos['DISTRITO'].dropna().unique())
#Seleccion de la distrito
opcion_distrito = st.selectbox('Selecciona un distrito', set_distritos)
df_distritos = df_departamentos[df_departamentos['DISTRITO'] == opcion_distrito]
num_filas = len(df_distritos.axes[0]) 

st.write('Numero de registros:', num_filas)

#Gráficas
#Gráfica de barras de SEXO
df_SEXO = df_distritos.SEXO.value_counts()
st.write('Distribución por SEXO:')
st.bar_chart(df_SEXO)

#Gráfica de barras de EDAD
df_edad = df_distritos.EDAD_DECLARADA.value_counts()
st.write('Distribución por EDAD:')
st.bar_chart(df_edad)

#Gráfica de barras de CLASIFICACION_DEF
df_CLASIFICACION_DEF = df_distritos.CLASIFICACION_DEF.value_counts()
st.write('Distribución por CLASIFICACION_DEF:')
st.bar_chart(df_CLASIFICACION_DEF)


st.write("------------------------------------------------------------------------------------------------------------------------------------")



#VIDEO DE YOUTUBE
st.subheader("**VIDEO INFORMATIVO DE LA PROBLEMATICA**")    
video_file = open('Coronavirus Covid-19_ Claves para entender la enfermedad y protegerse - Clínica Alemana.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("**Fuente**: Clínica Alemana. (2020). https://www.youtube.com/watch?v=vlzxSleRnmg")


if st.sidebar.button("¿Quiénes somos?"):
	st.header("¿Quiénes somos?")
	st.write("Somos un grupo de estudiantes de V ciclo de Ingeniería de la Universidad Peruano Cayetano Heredia (UPCH). Nos apasiona el procesamiento y visualización de datos medioambientales que puedan ayudar al público general a comprender mejor el problema de la contaminación del aire.")
	
	col1, col2, col3, col4 = st.columns(4)
	image1 = Image.open('ELIZABETH.jpg')
	col1.header("ELIZABETH CHAVEZ")
	col1.image(image1, use_column_width=True)
	grayscale = image1.convert('LA')
	col2.image(grayscale, use_column_width=True)
	image2 = Image.open('ANDREA.jpeg')
	col3.header("ANDREA ALBUJAR")
	col3.image(image2, use_column_width=True)
	grayscale = image2.convert('LA')
	col4.image(grayscale, use_column_width=True)
	
	col5, col6, col7, col8 = st.columns(4)
	image3 = Image.open('SebastianFranco.jpeg')
	col5.header("SEBASTIAN FRANCO")
	col5.image(image3, use_column_width=True)
	grayscale = image3.convert('LA')
	col6.image(grayscale, use_column_width=True)
	image4 = Image.open('DAYANA.jpg')
	col7.header("DAYANA HERRERA")
	col7.image(image4, use_column_width=True)
	grayscale = image4.convert('LA')
	col8.image(grayscale, use_column_width=True)
	
	col9, col10 = st.columns(2)
	image5 = Image.open('ANGELA.jpeg')
	col9.header("ANGELA VILLANUEVA")
	col9.image(image5, use_column_width=True)
	grayscale = image5.convert('LA')
	col10.image(grayscale, use_column_width=True)



