import streamlit as st
#funcion principal para verificar automoviles
def verificar_automoviles():
    st.title("Centro de verificacion de Automoviles")

    #lista para almacenar los puntos contaminantes
    if 'puntos_contaminantes' not in st.session_state
        st.session_state.puntos_contaminantes = []

    #input para los puntos contaminantes del automovil
    puntos = st.number_input("Ingrese los puntos contaminantes del automovil", min_value=0.0. step=0.1)

    #boton para registrar los automoviles
    if st.button("Registrar Automovil"):
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"Automovil registrado con {puntos} puntos contaminante.")
    #Mostrar los datos registrados  hasta el momento
    if len(st.session_state.puntos_contaminantes) > 0 and st.button("Calcular Resultados"):
        promedio = sum(st.session_state.puntos_contaminantes) / len(st.session_state.puntos_contaminantes)
        menos_contaminacion = min(st.session_state.puntos_contaminantes)
        mas_contaminacion = max(st.session_state.puntos_contaminantes)
        
        #Mostrar los resultados
        st.write(f"Promedio de puntos contaminantes: {promedio:.2f}")
        st.write(f"El automovil que menos contamino tiene {menos_contaminacion}")
        st.write(f"El automovil que mas contamino tiene {mas_contaminacion}")

    #opcion para reiniciar los datos
    if st.button("Reiniciar datos:"):
        st.session_state.puntos_contaminantes = []
        st.success("Datos reiniciados correctamente")

#Ejecutar la funcion
if __name__ == "__main__":
    verificar_automoviles()