# SISTEMA DE GERENCIAMENTO DE LIVROS - NEXUS BIBLIOTECA

import matplotlib.pyplot as plt # biblioteca de visualização de dados
import time # para inserir pausas entre respostas

# Mensagens de inicialização
print("\n---------------- SISTEMA DE GERENCIAMENTO DE LIVROS - NEXUS BIBLIOTECA ------------------------\n")
time.sleep(1) # Inserindo pausa
print("INICIALIZANDO SISTEMA...\n")
time.sleep(1) # Inserindo pausa

# Criando classe Livros com parâmetros titulo, autor, genero, estoque.
class Livros:
    def __init__(self, titulo, autor, genero, estoque):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.estoque = estoque
        
        # Definindo como será exibido
    def __str__(self):
        return f"TÍTULO: {self.titulo} / AUTOR: {self.autor} / GÊNERO: {self.genero} / ESTOQUE: {self.estoque}"
    
# Lista vazia para adicionar novos livros
livros = []

print("Adicionando livros... aguarde\n") 
# Método para adicionar novo livro
def adicionar_livro(titulo, autor, genero, estoque):
    livro_adicionado = Livros(titulo, autor, genero, estoque)
    livros.append(livro_adicionado)
    print(f"Livro: {titulo} foi adicionado!")
    time.sleep(1) # Inserindo pausa

# Método para listar livros
def listar_livros():
    print("\n------ BIBLIOTECA NEXUS ------\n")
    time.sleep(1) # Inserindo pausa
    # Percorrendo a lista e imprindo livro por livro
    for livro in livros:
        print(livro)

# Método para cadastrar novo livro
def cadastrar_livro():
    adicionar_livro("1984", "George Orwell", "Ficção Distópica", 5)
    adicionar_livro("O Senhor Dos Anéis", "J.R.R", "Fantasia Épica", 2)
    adicionar_livro("Orgulho e Preconceito", "Jane Austen", "Romance", 4)
    adicionar_livro("Dom Casmurro", "Machado de Assis", "Romance Realista", 10)
    
    listar_livros()
    
# Exibindo método cadastrar_livro()
cadastrar_livro()
time.sleep(1)

# Método para busca de livro pelo título
def buscar_livro(titulo_busca):
    encontrado = False
    for livro in livros:
        # .lower() para evitar problemas se o usuário digitar maiúsculas/minúsculas diferentes
        if livro.titulo.lower() == titulo_busca.lower():
            print("\n------ LIVRO ENCONTRADO ------")
            print(livro)
            encontrado = True
            break
            
    if not encontrado:
        print(f"\nO livro '{titulo_busca}' não foi encontrado no acervo.")

# Exemplo de uso após cadastrar os livros:
print("\nEncontre o livro que busca!\n")
time.sleep(1)
livro_encontrado = input("Digite abaixo o nome do livro que procura:\n")
buscar_livro(livro_encontrado)

# Extraindo dados da lista livros
titulo_livro = [livro.titulo for livro in livros]
estoque_livro = [livro.estoque for livro in livros]

print("Em seguida informaremos nossos livros disponíveis e estoque!\n")
print("\nCarregando gráfico, aguarde...\n")
# Inserindo pausa
time.sleep(1)

# Criando gráfico básico
plt.bar(titulo_livro,estoque_livro, color = 'lightblue')
plt.title("BIBLIOTECA NEXUS")
plt.xlabel("TÍTULO")
plt.ylabel("ESTOQUE")
plt.show()
print("Encerrando sistema, obrigado!")
time.sleep(1)