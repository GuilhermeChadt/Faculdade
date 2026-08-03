# AULA 1 (isto é um comentário)
print("Hello World!")

# Imprimindo boas vindas ao usuário
nome_usuario = input("Digite seu nome: ")
print("Bem-vindo(a),", nome_usuario, "!")

# Definição variáveis
x = 10
nome = "João"
preço = 19.99
fez_inscrição = True

# Imprimindo os tipos das variáveis
print(type(x))
print(type(nome))
print(type(preço))
print(type(fez_inscrição))

# Programa média 7
# Solicitar ao usuário que digite quatro notas
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

# Média das notas e condição de aprovação
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Parabéns, ", nome_usuario, "aprovado(a)!", "Sua média foi:", media)
else:
    print("Reprovado(a)!", "Sua média foi:", media)
    
# Imprimir a média
# print("A média das notas é:", media)

