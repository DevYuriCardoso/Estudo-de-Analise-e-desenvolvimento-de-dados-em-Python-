#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd

#Pegar e importar a base de dados 
tabela = pd.read_csv("clientes.csv",encoding = "latin", sep=";")
#deletar coluna inutil 
tabela = tabela.drop("Unnamed: 8", axis = 1)
#Visualizar a base de dados
    #intender as informações disponiveis 
    #procurar erros na base de dados     
display(tabela)


# In[65]:


#Tratamento de dados 
    #Valores no formato errado 
tabela ["Salário Anual (R$)"]= pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
    #Valores vazios
tabela = tabela.dropna()
print(tabela.info())


# In[66]:


#Analise inicial = "entender a nota dos cliente" 

display (tabela.describe())


# In[67]:


#Analize Completa = "Traçar o perfil ideal de clientes"
import plotly.express as px

#criar gráfico 
for coluna in tabela.columns:
    grafico = px.histogram (tabela, x = "Salário Anual (R$)" , y ="Nota (1-100)", histfunc = "avg" , text_auto = True , nbins = 10 )
    #histfunc = "avg"capturar a função do hist que por padrão já bem com soma
    #exibir gráfico
    grafico.show()


# In[68]:


get_ipython().system('pip install plotly')


# In[69]:


#perfil ideal do Client :

#Clientes acima de 15 anos 

# Principais compradores : Pessoas das áreas de  Entreterimento e artistas
# Menores compradores: Pessoas da Construção Civil 
# Clientes entre 10 a 15 anos de experiência 
# Familias de até 7 pessoas 

#obs:
#O Salário não faz muita diferença, clientes que compram em promoção tem uma leve nota menor, mas não significativo


