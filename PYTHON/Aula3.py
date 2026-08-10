# ESTRUTURAS DE REPETIÇÃO FOR, WHILE, RANGE
import time
import sys

# For(lista de 0 a 10 com incremento 2)
print("--------------FOR (imprime lista de 0 a 10 com incremento 2)---------------")
for i in range(0, 10, 2):
    print("Valor: ", i)
    time.sleep(1)

# While(contador 5 incrementando 1)
print("--------------WHILE (contador 5 incrementando 1)---------------")
contador = 0
while contador < 5:
    print("Valor do contador:", contador)
    contador += 1
    time.sleep(1)
    
# While(sorteio de prêmios)
print("------------Sorteio de prêmios------------")
premios = {
    1: "VOCÊ GANHOU UMA GARRAFA TÉRMICA",
    2: "VOCÊ GANHOU UM KIT DE CANECAS",
    3: "VOCÊ GANHOU UM KIT DE CHAVEIROS",
    4: "VOCÊ GANHOU UM FONE DE OUVIDO",
}
print("Vamos jogar?")
time.sleep(1)
if input("Digite 'sim' para jogar: ") == "sim" or "Sim" or "SIM":
    print("Ótimo! Vamos começar!")
    time.sleep(1)   
else:
    print("Que pena! Você não poderá participar do sorteio.")
    time.sleep(1)
    sys.exit()  
    
numero = int(input("Digite um número: "))
while numero < 1 or numero > 4:
    print("Número inválido. Digite um número entre 1 e 4.")
    numero = int(input("Digite um número: "))
print(premios[numero])
