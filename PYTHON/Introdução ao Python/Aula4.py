# FUNÇÕES
import time

print("------------- Função: Soma -----------------")
def soma(a, b):
    resultado = a+b
    return resultado
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
resultado = soma(a, b)
print("Calculando...")
time.sleep(1)
print("O resultado da soma é: ", resultado)

print("------------- Função: Número Par -----------------")
def numero_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

try:
    num = int(input("Digite um número: ")) 
    print("O número é par: ", numero_par(num))
except ValueError:
    print("O número digitado não é par.")    
