import streamlit as st
#titulo de la aplicacion
st.title("Efercicios con bucles basicos en python")

#ejercicio 1: imprimir 10 veces 'Hola Mundo'
st.title("Ejercicio 1: imprimir 'Hola Mundo'10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")
#ejercicio 2: Imprimir los primeros 10 numeros
st.subheader("Ejercicio 3: Imprimir los primeros 10 numeros")
if st.button("Ejecutar Ejercicio 2"):
    for i in range(1, 11):
        st.write(i)
#Ejercicio 3: Tabla de multiplicar
st.subheader("Ejercicio 3: Imprimir la tabla de multiplicar del numero ingresado")
num = st.number_input("Ingrese un numero para ver su tabla de multiplicar del 1 al 12", min_value=1)
if st.button("ejercutar Ejercicio 3"):
    for i in range(1,13):
        st.write(f"{num} x {i} = {num*i}")
#ejercicio4
st.subheader("Ejercicio 4: Comparar 10 con el valor de 10")
numeros_ej1 = st.text_input("Ingresa 10 numeros separados por coma","12,7,15,10,20,5,11,6,9,8")

if st.button("Ejecutar Ejercicio 4"):

    lista_numeros= [int(num) for num in numeros_ej1.split(",")]
    media = sum(lista_numeros) / len(lista_numeros)
    mayores = len([num for num in lista_numeros if num > 10])
    iguales = len([num for num in lista_numeros if num == 10])
    menores = len([num for num in lista_numeros if num < 10])
    