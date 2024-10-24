import pandas as pd 
import plotly.express as px
import streamlit as st

st.header("Análises de Veículos Usados")
car_data = pd.read_csv("vehicles.csv.csv")
hist_button = st.button("Criar histograma de Veículos usados")

if hist_button:
    st.write("Criando um histograma para o conjunto de dados de anúncio de veiculos de vendas de carros")

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, user_container_width=True)

elif scatter_button:  
    st.write("Criando um gráfico de dispersão para o conjunto de dados de anúncio de veículos de vendas de carros")

    fig = px.scatter(car_data, x="odometer", y="price")
    
    st.plotly_chart(fig, use_container_width=True)


import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles.csv.csv") # lendo os dados
fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
fig.show() # exibindo
   