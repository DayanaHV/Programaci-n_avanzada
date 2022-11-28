#$ pip install streamlit --upgrade
import urllib.request
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

#TITULO
st.title('Fallecidos por COVID-19 - [Ministerio de Salud - MINSA]')
st.markdown("**PROYECTO FINAL PROGRAMACIÓN 2022-2**")
#IMAGEN PORTADA
imagen_portada = Image.open('imagenportada.jpg')
st.image(imagen_portada)

#INTRODUCCIÓN
image_INTRODUCCION = Image.open('INTRODUCCION.jpg')
st.image(image_INTRODUCCION)



st.write("------------------------------------------------------------------------------------------------")




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

st.header("DATA DE FALLECIDOS POR COVID-19")
@st.experimental_memo
def download_data():
   url="https://raw.githubusercontent.com/DayanaHV/Programaci-n_avanzada/main/fallecidos_covid.csv"
   df=pd.read_csv("fallecidos_covid.csv")
   return df

c=download_data()
st.write('**Dimensiones de la tabla:**') 
st.write('* Fila: ' + str(c.shape[0]))
st.write('* Columnas: ' + str(c.shape[1]))
st.dataframe(c)

st.subheader("Características del Dataset")
st.write(c.describe())




#VIDEO DE YOUTUBE
st.subheader("**VIDEO INFORMATIVO DE LA PROBLEMATICA**")    
video_file = open('Coronavirus Covid-19_ Claves para entender la enfermedad y protegerse - Clínica Alemana.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("**Fuente**: Clínica Alemana. (2020). https://www.youtube.com/watch?v=vlzxSleRnmg")

#ENTRADA DEL USUARIO
st.sidebar.header("Entradas del usuario")
#Filtro edad
año_seleccionado=st.sidebar.selectbox('Edad', list(reversed(range(0,110))))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_data(edad):
	df = download_data()
	df=df.astype({'EDAD_DECLARADA':'str'})
	df['FECHA_CORTE'] = pd.to_numeric(df['FECHA_CORTE'])
	df['FECHA_FALLECIMIENTO'] = pd.to_numeric(df['FECHA_FALLECIMIENTO'])
	df['UUID'] = pd.to_numeric(df['UUID'])
	grouped = df.groupby(df.EDAD_DECLARADA)
	df_edad = grouped.get_group(edad)
	return df_edad

data_año=load_data(str(año_seleccionado))
sorted_unique_departamento = sorted(data_año.DEPARTAMENTO.unique())
selected_departamento=st.sidebar.multiselect('Departamento', sorted_unique_departamento, sorted_unique_departamento)

unique_data=['FECHA_CORTE', 'FECHA_FALLECIMIENTO', 'UUID']
selected_data=st.sidebar.multiselect('Clasificación', unique_data, unique_data)

df_selected=data_año[(data_año.DEPARTAMENTO.isin(selected_departamento))]

def remove_columns(dataset, cols):
	return dataset.drop(cols, axis=1)

cols=np.setdiff1d(unique_data, selected_data)

st.subheader('Mostrar data de distrito(s) y clasificacion(s) seleccionado(s)')
data=remove_columns(df_selected, cols)
st.write('Dimensiones: ' + str(data.shape[0]) + ' filas y ' + str(data.shape[1]) + ' columnas')
st.dataframe(data)

#NO MODIFIQUEN NADAAAAAAAAAAAA HASTA AQUI NADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

#----------------------------------------------------------------------------------------------
				
lsta_clasificación=['Criterio virolÃ³gico', 'Criterio SINADEF', 'Criterio clÃ­nico', 'Criterio nexo epidemiolÃ³gico', 'Criterio investigaciÃ³n EpidemiolÃ³gica', 'Criterio radiolÃ³gico', 'Criterio serolÃ³gico']
distrits_names = pd.unique(df["DISTRITO"])

st.header('Evaluación de clasificación por distrito')
selec_ditrit = st.selectbox('Evaluación de contaminates por distrito', distrits_names)
st.subheader("Distrito seleccionado:")
st.subheader(str(selec_ditrit))

grouped_g2 = df.groupby(df.DISTRITO)
distrito = grouped_g2.get_group(selec_ditrit)
fecha = list(distrito.iloc[0,range(2,5)])
fecha_ini = str(fecha[0])+'/'+str(int(fecha[1]))+'/'+str(int(fecha[2]))

rango = int(list(distrito.shape)[0])
index = pd.date_range(start=fecha_ini, periods=rango, freq='60T')











st.header('Si no recuerdan la edad coloquen un rango')	
minYear = st.selectbox('Desde', list(range(0,110)))
maxYear = st.selectbox('Hasta', list(reversed(range(0,110))))

anios = st.button('Gráfico entre años')







################------------------------------------------------------------------------------
#df=c
#filt=(df["EDAD_DECLARADA"]==año_seleccionado)
#df[filt]
#Filtro sexo
#sexxo=[MASCULINO,FEMENINO]
#sexo_seleccionado=st.sidebar.selectbox('SEXO',sexxo) ### Modificar parametro
#df=c
#filt=(df["SEXO"]==sexo_seleccionado)
#df[filt]

#Quien somos 
st.write('**Quien somos:**') 
