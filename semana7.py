import streamlit as st

def mostrar_menu():
    st.title("Ejemplo de Menu")
    st.write("Selecciona una opcion del menu")

    menu = ["Archivo" , "Editar", "Ver", "Salir"]
    seleccion=""

    seleccion = st.radio("Menu", menu)


    if seleccion=="Archivo":
        st.write("Seleccionaste: Archivo")
    elif seleccion=="Editar":
        st.write("Seleccionaste: Editar")
    elif seleccion=="Ver":
        st.write("Seleccionaste: Ver")
    elif seleccion=="Salir":
        st.write("Seleccionaste: Salir")

if __name__=="__main__":
    mostrar_menu()