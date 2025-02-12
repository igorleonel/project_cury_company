import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home')

image_path = 'logo.png'
image = Image.open(image_path)
st.sidebar.image(image, width=200)

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown('---')
st.sidebar.info('Análise dos dados de entregas, pedidos e avaliações disponibilizados pelo aplicativo da Cury Company, que conecta restaurantes, entregadores e consumidores. Projeto de Data Science voltado para a análise exploratória dos principais KPIs de crescimento da empresa.')

st.write('# Cury Company Growth Dashboard')

st.markdown("""
Growth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes.
### Como utilizar esse Growth Dashboard?
- Visão Empresa:
    - Visão Gerencial: Métricas gerais de comportamento.
    - Visão Tática: Indicadores semanais de crescimento.
    - Visão Geográfica: Insights de geolocalização.
- Visão Entregador:
    - Acompanhamento dos indicadores semanais de crescimento
- Visão Restaurante:
    - Indicadores semanais de crescimento dos restaurantes
""")