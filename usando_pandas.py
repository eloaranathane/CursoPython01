import pandas as pd

# Criando um dataframe com pandas
data = {
    'Nome' : ['Caio', 'Andressa', 'Emily', 'Davi', 'Jesreel', 'Eloara', 'Alice'],
    'Idade': [15, 20, 25, 30, 35, 40, 45],
    'Salario' : [1000, 2000, 3000, 4000, 5000, 6000, 7000]
    }
df = pd.DataFrame(data)

# Exibir o dataframe
print('DataFrame criado:')
print(df)

# Selecionar uma coluna específica
print('\n Mostra a coluna de nome')
print(df['Nome'])

# Filtrar linhas
print('\n Pessoas com idade maior que 30: ')
print(df[df['Idade'] > 30])

# Adicionar uma nova coluna
df['Imposto'] = df['Salario'] * 0.1
print('\n Dataframe agora com a coluna do imposto')
print(df)

# Média dos salarios
media_salario = df['Salario'].mean()
print('\n Média de salario')
print(media_salario)

# Média dos impostos
media_imposto = df['Imposto'].mean()
print('\n Média de Imposto')
print(media_imposto)

# Salvando o dataframe em um arquivo csv
df.to_csv('salarios.csv', index=False)

# Carregar arquivo externo de dados
df_externo = pd.read_csv('salarios.csv')
print('\n Tabela CSV externa')
print(df_externo)