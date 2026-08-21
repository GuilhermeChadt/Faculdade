#EXPLORANDO RECURSOS

texto = "Olá, mundo!"
print(type(texto)) # imprimindo tipo da variável
print("Texto: ", texto, "Número de vezes que aparece a letra 'o': ", texto.count('o')) # função count() conta quantas vezes aparece a letra 'o'
print("As 5 primeiras letras são: ", texto[:5]) # fatiamento de string, pegando do início até a posição 5
cores = ['Branco', 'Vermelho', 'Verde', 'Azul', 'Preto'] 
for cor in cores:
    print("Posição:", cores.index(cor), "Cor:",cor) # imprimindo posição e valor de cada elemento da lista
converterTexto1 = texto.upper() # convertendo texto para maiúsculas
print("Texto convertido para maiúsculas: ", converterTexto1)
converterTexto2 = texto.lower() # convertendo texto para minúsculas
print("Texto convertido para minúsculas: ", converterTexto2)