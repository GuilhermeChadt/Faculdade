# EXPLORANDO RECURSOS - AULA 2
# SETS, ARRAY NUMPY, DICT
import numpy as np # importando a biblioteca numpy

conjunto = set() # criando um set vazio
conjunto.add(1) # adicionando elementos ao set
conjunto.add('vermelho')
conjunto.add(78)
print("Set: ", conjunto) # imprimindo o set

numeros_repetidos = [1, 2, 3, 4, 5, 1, 2, 3] # criando uma lista com números repetidos
conjunto_numeros = set(numeros_repetidos) # convertendo a lista para set, eliminando os números repetidos
print("Lista com números repetidos: ", numeros_repetidos) # imprimindo a lista
print("Set sem números repetidos: ", conjunto_numeros) # imprimindo o set

# criando um dicionário
notebooks = [
    {'Marca': 'Dell', 'Modelo': 'Inspiron', 'Ano': 2020, 'Preço': 5000, 'Estoque': 8},
    {'Marca': 'Apple', 'Modelo': 'Air', 'Ano': 2024, 'Preço': 8000, 'Estoque': 1},
    {'Marca': 'Lenovo', 'Modelo': 'Ideapad', 'Ano': 2022, 'Preço': 4000, 'Estoque': 4}
    ] 
print("Notebooks disponíveis: ", [(notebook['Marca'], notebook['Modelo']) for notebook in notebooks]) # imprimindo o dicionário

'''notebook1['Preço'] = 4500 # alterando o valor de uma chave
print("Valor do produto atualizado para: ", notebook1['Preço']) # imprimindo o dicionário atualizado
print("Quantidade disponível: ", notebook1['Quantidade']) # imprimindo a quantidade disponível'''

# criando uma lista de números

array = [1, 2, 3, 4, 5]
print("Array: ", array) # imprimindo o array


