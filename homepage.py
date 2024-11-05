import streamlit as st 


#Containers 
# columns

secao_usuario = st.session_state
nome_usuario = None

if 'username' in secao_usuario:
    nome_usuario = secao_usuario.name

coluna_esquerda, coluna_direita = st.columns([1, 1.5])

coluna_esquerda.title('Hash&Co')
if nome_usuario:
    coluna_esquerda.write(f'#### Bem vindo, {nome_usuario}')

botao_dashboards = st.button('Dashboards Projetos')
botao_indicadores = st.button('Principais Indicadores')

if botao_dashboards:
    st.switch_page('dashboard.py')
if botao_indicadores:
    st.switch_page('indicadores.py')

contanier = coluna_direita.container(border=True)
contanier.image('imagens/time-comunidade.webp')
