import streamlit as st

st.title("Herramienta de Evaluación de Riesgos")

st.header("Ingreso de Datos")

riesgo_nombre = st.text_input("Nombre del Riesgo:")

probabilidad = st.selectbox("Probabilidad del Riesgo:", ["Baja", "Media", "Alta"])

impacto = st.selectbox("Impacto del Riesgo:", ["Bajo", "Medio", "Alto"])

def calcular_puntuacion(probabilidad, impacto):
    puntuacion = 0
    
    if probabilidad == "Baja":
        puntuacion += 1
    elif probabilidad == "Media":
        puntuacion += 2
    else:
        puntuacion += 3
        
    if impacto == "Bajo":
        puntuacion += 1
    elif impacto == "Medio":
        puntuacion += 2
    else:
        puntuacion += 3
        
    return puntuacion

if st.button("Evaluar Riesgo"):
    if riesgo_nombre:
        puntuacion_riesgo = calcular_puntuacion(probabilidad, impacto)
        st.write(f"Riesgo: {riesgo_nombre}")
        st.write(f"Probabilidad: {probabilidad}")
        st.write(f"Impacto: {impacto}")
        st.write(f"Puntuación del Riesgo: {puntuacion_riesgo}")
        
        # Clasificación del riesgo
        if puntuacion_riesgo <= 2:
            st.success("Riesgo Bajo")
        elif puntuacion_riesgo <= 4:
            st.warning("Riesgo Medio")
        else:
            st.error("Riesgo Alto")
    else:
        st.warning("Por favor, ingrese el nombre del riesgo.")

