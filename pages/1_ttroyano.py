import streamlit as st


# Título de la aplicación
st.title('Tu IMC En Linea')
# imagen
st.image("imc/corazon.png")
# Entrada de peso en kilogramos
peso = st.number_input('Ingresa tu peso (en kilogramos)', min_value=1.0)

# Entrada de altura en metros
altura = st.number_input('Ingresa tu altura (en metros)', min_value=0.01)

# Calcular el IMC
if st.button('Calcular IMC'):
    imc = peso / (altura ** 2)
    st.write(f'Tu IMC es: {imc:.2f}')

    # Interpretación del IMC
    if imc < 18.5:
        st.write('Tienes un peso bajo.')
    elif 18.5 <= imc < 24.9:
        st.write('Tu peso es saludable.')
    elif 25 <= imc < 29.9:
        st.write('Tienes sobrepeso.')
    else:
        st.write('Tienes obesidad.')