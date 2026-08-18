# SISTEMAS DE GESTÃO DE NOTAS DE ALUNO

import time #inserir pausas entre comandos

'''Cadastro de Notas:
• O sistema deve permitir que o usuário insira as notas dos alunos.
• As notas devem ser armazenadas em uma lista.
----------
Cálculo da Média:
• O sistema deve calcular a média das notas inseridas.
----------
Determinação da Situação:
• Se a média for maior ou igual a 7, o aluno está aprovado.
• Se a média for menor que 7, o aluno está reprovado.
----------
Relatório Final:
• Exibir as notas inseridas, a média e a situação do aluno.'''

#PROGRAMA
notas = []
print("--------SISTEMAS DE GESTÃO DE NOTAS DE ALUNO---------")
time.sleep(1)
nota1 = float(input("Digite sua primeira nota: "))
notas.append(nota1)
nota2 = float(input("Digite sua segunda nota: "))
notas.append(nota2)
nota3 = float(input("Digite sua terceira nota: "))
notas.append(nota3)
media = round((nota1 + nota2 + nota3) / 3)
print("Calculando sua média.. Aguarde...")
time.sleep(1)
if media >= 7:
    print("Aluno aprovado! Média: ", media)
else:
    print("Aluno reprovado, agende sua recuperação na secretaria! Média: ", media)



