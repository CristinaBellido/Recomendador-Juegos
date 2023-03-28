import streamlit as st
import pandas as pd
df = pd.read_csv('C:\\Users\\Usuario ASUS\\Documents\\Repositoris Github\\PROYECTOSPOTY\\Moviles\\df_streamlit.csv')

# Define el título de la página
st.set_page_config(page_title='Recomendador de juegos', page_icon=':gráfico_de_barras:', layout='wide')

# Define el menú de la izquierda
st.sidebar.title('Menu')

# Define las opciones del menú
options_etl = ["Visualizaciones", "Librerias"]
options_recomendador = ["Recomendador"]

# Define la pestaña ETL
if st.sidebar.button('ETL'):
    st.header("ETL")
    st.write("El objetivo principal de este proyecto de machine learning es crear un recomendador de videojuegos personalizado, que sugiera títulos basados en las preferencias del usuario. Para ello, se han utilizado datos recopilados de la API de RAWG, que incluyen información sobre diversos aspectos de los videojuegos, tales como género, plataforma, rating, horas de juego etc.")
    st.write("Para poder entrenar el modelo, se han transformado los datos de tal manera que el dataframe cuenta con 63 columnas de 0s y 1s que indican la presencia o ausencia de una determinada característica en cada juego. Estas columnas representan las características más relevantes de cada título, lo que permitirá al modelo hacer recomendaciones precisas.")
    st.write("Tras la transformación y limpieza de los datos obtenidos, este fue el resultado final del DataFrame")
    st.write(df)
    # Agregar subopciones dentro de la pestaña ETL
    choice_etl = st.sidebar.selectbox("Seleccione una opción", options_etl)
    if choice_etl == "Visualizaciones":
        st.write("Aquí van las visualizaciones")
    elif choice_etl == "Librerias":
        st.write("Aquí van las librerías")

# Define la pestaña Recomendador
if st.sidebar.button('Recomendador'):
    st.header("Recomendador")
    st.write("Aquí va la pestaña del recomendador")
    
# Muestra la opción seleccionada
st.write(f"Has seleccionado la opción de {choice_etl}")