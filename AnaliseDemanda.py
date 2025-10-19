'''Objetivos:

Qual o horário de maior demanda?

Qual o dia da semana tem mais corridas?

'''

#Tecnologias necessarias: Pandas(para analise exploratoria)

import pandas as pd

df = pd.read_csv("uber-raw-data-apr14.csv")
df.head()

#Informaçoes basicas
print("Linhas: {} e colunas: {}\n".format(df.shape[0], df.shape[1])) #564516 linhas e 4 colunas
print(df.info(), '\n') #Preciso converte data
print("valores nulos: \n", df.isnull().sum()) #Sem valores nulo

#Conversão de data
df['Date/Time'] = pd.to_datetime(df['Date/Time'], errors='coerce', infer_datetime_format=True)
print('\nData e tempo: ',df['Date/Time'].dtypes) #Data convertida

#Extraindo informaçoes de datas
df['hora'] = df['Date/Time'].dt.hour
df['dia_semana'] = df['Date/Time'].dt.day_name()

#Horario de maior demanda:
horario_maior_demanda = df['hora'].value_counts().sort_index()#ordena um df ou uma serie pelo id
print('\n',horario_maior_demanda)
print(f"Horario de maior demanda: {horario_maior_demanda.idxmax()}h")

#Dia da semana que tem mais corridas
semana_maior_demanda = df['dia_semana'].value_counts().sort_index()
print('\n',semana_maior_demanda)
print(f"Dia da semana de maior demanda: {semana_maior_demanda.idxmax()}")


#heatmap textual(para o grafico):

# Definindo a ordem correta das semanas
ordem_dias = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# Transforme a coluna dia_semana em categoria com a ordem desejada
df['dia_semana'] = pd.Categorical(df['dia_semana'], categories=ordem_dias, ordered=True)
'''
pd.Categorical(..., ordered=True) permite que o pandas saiba qual é a ordem lógica, e não apenas alfabética.
'''
# Dia da semana x hora
heatmap = df.groupby(['dia_semana', 'hora']).size().unstack(fill_value=0)
print('\n',heatmap)
'''
Linhas → dias da semana

Colunas → hora do dia (0–23)

Valores → quantidade de corridas (demanda)
'''

