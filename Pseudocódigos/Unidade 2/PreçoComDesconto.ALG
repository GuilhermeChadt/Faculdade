Algoritmo "Pre�o com desconto"
// Descri��o   : Altera��o de valor de produto baseado em percentual de desconto
// Autor(a)    : Guilherme Chadt Silva
// Data atual  : 07/02/2025
Var
   preco, novopreco, percentual: real
Inicio
   escreva("Digite o pre�o do produto: ")
   leia(preco)
   escreva("Digite o percentual de desconto: ")
   leia(percentual)
   novopreco <- (preco - (preco*percentual/100))
   escreva("Valor do produto com desconto � de: ", novopreco)
Fimalgoritmo