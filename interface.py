import streamlit as st
import sistema_de_recomendacion as sr

st.write("# Sistema de recomendación de video juegos")
st.write("Selecciones una calificación entre 1 y 10 para cada uno de los video juegos que se proponen.")
st.write("Si no ha jugado el videojuego, deje la calificación en cero.")

st.sidebar.write("### Video Juegos")

calificaciones=[]
for i in range(len(sr.nombreVideojuegos)):
    calificacion1i= st.sidebar.slider(sr.nombreVideojuegos[i], min_value=0, max_value=10)
    calificaciones.append(calificacion1i)

#st.write('Estas son las calificaciones ingresadas:')
#st.write(calificaciones)

if any(calificaciones):
    st.write("## Recomendaciones")
    st.write('De acuerdo con sus calificaciones, los juegos más recomendados son:')
    recomendaciones = sr.recomendar_videojuegos(calificaciones)

    st.write('#### 1. ' + recomendaciones.index[0])
    st.write('#### 2. ' + recomendaciones.index[1])
    st.write('#### 3. ' + recomendaciones.index[2])
    
    st.write("## Matriz de recomendaciones")
    st.write('Entre más baja la similitud, mas recomendado es:')
    st.write(recomendaciones)