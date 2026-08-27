# CLASSES E MÉTODOS EM PYTHON
# OBJETIVO: CRIAR UMA CLASSE VEÍCULO QUE MOSTRE O RESUMO E STATUS, COM CARRO E BICICLETA HERDANDO DELA

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def resumo(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Gênero: {self.genero}'
    
    def cumprimentar(self):
        return f'Olá, {self.nome}!'
    
    def aniversario(self):
        self.idade += 1
        return f'Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos.'
    
pessoa1 = Pessoa('Alice', 30, 'Feminino')

print(pessoa1.resumo())
print(pessoa1.cumprimentar())
print(pessoa1.aniversario())


