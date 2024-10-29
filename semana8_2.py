import streamlit as st

def calcular(operacion, num1,num2):
    """Realiza la operacion especificada entre num1 y num2."""
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Por favor, ingrese numeros validos"

    if operacion == "Suma":
        return num1+num2
    elif operacion == "Resta":
        return num1-num2
    elif operacion == "Multiplicacion":
        return num1*num2
    elif operacion == "Division":
        if num2 == 0:
            return "Error: no se puede dividir entre 0"
        return num1/num2
    else:
        return "Operacion no valida"

    def main():
        st.title("Calculadora Basica")
        st.title("Calculadora Básica")
    st.write("Seleccione la operación e ingrese los números: ")

    #Seleccione la operación
    operacion = st.selectbox("Operación", ("Suma", "Resta", "Multiplicación", "División"))

    #Entradas para los números
    num1 = st.text_input("Número 1")
    num2 = st.text_input("Número 2")

    #Botón para calcular
    if st.button("Calcular"):
        resultado = calcular(operacion, num1, num2)
        st.write("**Resultado:**", resultado)

if __name__ == "__main__":
    main()