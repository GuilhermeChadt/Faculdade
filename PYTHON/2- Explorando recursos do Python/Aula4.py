# BIBLIOTECAS E MÓDULOS - AULA 4 

import math # operações matemáticas
import matplotlib.pyplot as plt # operações para visualização de dados

'''sqrt(): raiz quadrada
cos() - cosseno
​ceil(): arredonda para cima
floor(): arredonda para baixo
​trunc(): remove decimais
​fabs(): valor absoluto
​factorial(): fatorial
​sqrt(): raiz quadrada
​pow(x, y): potência (x^y)
​exp(x): exponencial (e^x)
​log(x, [base]): logaritmo
​log10(): logaritmo na base 10
​sin() / cos() / tan(): seno, cosseno e tangente
​asin() / acos() / atan(): funções trigonométricas inversas
degrees() / radians(): conversão de ângulos
​gcd(a, b): maior divisor comum
​comb(n, k) / perm(n, k): combinações e permutações'''

 # Existem outras formas de import - import math as m (apelido), import math, import math from sqrt, cos, log (especifíca)
 
print("Raiz quadrada de 25: ", math.sqrt(25))
print("Cosseno de 45: ", math.cos(45))

# GRÁFICO 1
x = [1,2,3,4,5]
y = [2,4,1,3,5]
# Gráfico de linha
plt.plot(x,y)
# Adicionando rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
# Adicionando um título
plt.title('Gráfico 1')
# Exibindo gráfico
plt.show()

# GRÁFICO VENDAS MENSAIS
# Dados
meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL']
faturamento_mensal = [10000, 30000, 18000, 5000]
# Gráfico de barras
plt.bar(meses, faturamento_mensal, color = 'purple')
# Adicionando rótulos e título
plt.xlabel('MÊS')
plt.ylabel('FATURAMENTO MENSAL')
plt.title('VENDAS')
# Exibindo gráfico
plt.show()
