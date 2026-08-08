# ESTRUTURAS CONDICIONAIS

import time #utilizar a função time.sleep() e criar pausas no programa
import sys  #utilizar a função sys.exit() para encerrar o programa

# Validação de idade
print("------------Validação de idade------------")
time.sleep(1)
idade = int(input("Digite sua idade: "))
print("Validando sua idade, aguarde...")
time.sleep(2)
if idade <= 18:
    print("Menor de idade ou adolescente")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")
time.sleep(1)

# Condição de aceite para recomendação de filme
print("------------Condição de aceite para recomendação de filme------------")
time.sleep(1)   
aceite = input("Você aceita receber recomendações de filmes? (Sim/Não): ")
print("Validando sua resposta, aguarde...")
time.sleep(2)
if aceite == "Sim" or aceite == "SIM"or aceite == "sim":
    print("Recomendação de filmes ativada!")
else:
    print("Recomendação de filmes desativada! Obrigado por utilizar nosso sistema!")
    sys.exit()
time.sleep(1)

# Recomendação de filme por idade
filme_12anos = "A Era do Gelo"
filme_14anos = "A Rede Social"
filme_18anos = "O Clube da Luta"
print("------------Recomendação de filme por idade------------")
idade = int(input("Digite sua idade novamente para receber a recomendação de filmes: "))
print("Validando sua idade, aguarde...")
time.sleep(2)
if idade < 12:
    print("Por favor, retorne com um responsável maior de 18 anos para comprar o ingresso! O filme recomendado para você é: " + filme_12anos + "!")
elif idade >= 14 and idade < 18:
    print("Por favor, retorne com um responsável maior de 18 anos para comprar o ingresso! Recomendamos os filmes: " + filme_12anos + " e " + filme_14anos)
else:
    print("Recomendamos o filme: " + filme_12anos + ", " + filme_14anos + " e " + filme_18anos + ". Aproveite o filme!")
    
