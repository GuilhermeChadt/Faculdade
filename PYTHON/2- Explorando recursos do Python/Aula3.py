# CLASSES E MÉTODOS - AULA 3

class Pessoa: # construtor da classe
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    def resumo(self): # método que retorna um resumo das informações da pessoa
        return f'Nome: {self.nome}, Idade: {self.idade}, Gênero: {self.genero}'
    
    def cumprimentar(self): # método que retorna uma saudação personalizada
        return f'Olá, {self.nome}!'
    
    def aniversario(self): # método que incrementa a idade e retorna uma mensagem de aniversário
        self.idade += 1
        return f'Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos.'
    
# Criando uma instância da classe Pessoa    
pessoa1 = Pessoa('Alice', 30, 'Feminino') 
# Invocando os métodos da classe Pessoa e imprimindo os resultados
print(pessoa1.resumo()) 
print(pessoa1.cumprimentar())
print(pessoa1.aniversario())

class Veículo: # construtor da classe
    def __init__(self,marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.velocidade = 0 # veículo inicia parado 
  
    def acelerar(self, incremento):
        self.velocidade += incremento

    def freiar(self, decremento):
        self.velocidade -= decremento
    
    def resumo(self): # método que retorna um resumo das informações do veículo
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, '
                f'Veículo: {self.modelo}, Velocidade: {self.velocidade}km/h')

# TESTANDO
carro1 = Veículo('BMW', 'X1', 2019, 0)
print(carro1.resumo())
        