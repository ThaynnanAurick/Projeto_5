import pandas as pd 
import plotly.express as px
import streamlit as st

st.header("Análise de Veículos Usados")
car_data = pd.read_csv("vehicles.csv.csv")
hist_button = st.button("Criar histograma de Veículos usados")

if hist_button:
    st.write("Criando um histograma para o conjunto de dados de anúncio de veiculos de vendas de carros")

    fig = px.histogram(car_data, x="odometer")

    st.plotly.chart(fig, user_container_width=True)