Algoritmo "Preço com desconto"
// Descrição   : Alteração de valor de produto baseado em percentual de desconto
// Autor(a)    : Guilherme Chadt Silva
// Data atual  : 07/02/2025
Var
   preco, novopreco, percentual: real
Inicio
   escreva("Digite o preço do produto: ")
   leia(preco)
   escreva("Digite o percentual de desconto: ")
   leia(percentual)
   novopreco <- (preco - (preco*percentual/100))
   escreva("Valor do produto com desconto é de: ", novopreco)
Fimalgoritmo