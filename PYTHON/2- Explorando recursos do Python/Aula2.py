# EXPLORANDO RECURSOS AULA 2
# SETS, ARRAY NUMPY, DICT

conjunto = set() # criando um set vazio
conjunto.add(1) # adicionando elementos ao set
conjunto.add('vermelho')
conjunto.add(78)
print("Set: ", conjunto) # imprimindo o set

notebooks = [
    {'Marca': 'Dell', 'Modelo': 'Inspiron', 'Ano': 2020, 'Preço': 5000, 'Quantidade': 8},
    {'Marca': 'Apple', 'Modelo': 'Air', 'Ano': 2024, 'Preço': 8000, 'Quantidade': 1},
    {'Marca': 'Lenovo', 'Modelo': 'Ideapad', 'Ano': 2022, 'Preço': 4000, 'Quantidade': 4}
    ] # criando um dicionário
print("Notebooks disponíveis: ", [(notebook['Marca'], notebook['Modelo']) for notebook in notebooks]) # imprimindo o dicionário

'''notebook1['Preço'] = 4500 # alterando o valor de uma chave
print("Valor do produto atualizado para: ", notebook1['Preço']) # imprimindo o dicionário atualizado
print("Quantidade disponível: ", notebook1['Quantidade']) # imprimindo a quantidade disponível'''



