# TABELA CADASTRO COM CRUD COMPLETO - id, nome, email, telefone
# DICA: SEMPRE UTILIZAR con.commit() após o término do comando, utilizar conn.close() ao finalizar o programa

# IMPORTANDO LIB SQLITE3
import sqlite3
# CONECTANDO AO BANCO DE DADOS
conn = sqlite3.connect("Cadastro.db")
cursor = conn.cursor() # PERMITE EXECUTAR OS COMANDOS SQL

# CRIANDO TABELA
cursor.execute("""
               CREATE TABLE IF NOT EXISTS Cadastro (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   email TEXT,
                   telefone TEXT
               )
               """)
print("TABELA CRIADA")

# MULTIPLOS CADASTROS COM EXECUTEMANY - INSERT INTO
dados_teste = [
    ("HARRY", "HARRY777@GMAIL.COM", "1599999999"),
    ("JANETE", "JANETEEUMESMA@HOTMAIL.COM", "11999999999"),
    ("MARCIN", "MM123@BOL.COM,BR", "139999999")
]
cursor.executemany("INSERT INTO Cadastro (nome, email, telefone) VALUES (?, ?, ?)",dados_teste)
conn.commit() # CONFIRMANDO ALTERAÇÕES

# LEITURA DO BANCO DE DADOS COM SELECT/ FROM
cursor.execute("SELECT * FROM Cadastro")
cadastro = cursor.fetchall() # RETORNA TODA INFO COMO TUPLA
print("Cadastros: ")
for cadastro in cadastro:
    print("CADASTRO:", cadastro)

# ATUALIZANDO CADASTRO DE ID 1 - UPDATE/ SET/ WHERE
cursor.execute(
    "UPDATE Cadastro SET telefone = ? WHERE ID = ?",
    ("1111111111","1")
)
conn.commit() # CONFIRMANDO ALTERAÇÕES
print("UPDATE CADASTRO:", cadastro)

# DELETANDO UM ID COM DELETE FROM/ WHERE
cursor.execute("DELETE FROM Cadastro WHERE id = ?, (2)") 
conn.commit() # CONFIRMANDO ALTERAÇÕES

# TABELA ATUALIZADA
cursor.execute("SELECT * FROM Cadastro") # EXECUTANDO COMANDO DE LEITURA GERAL DO BANCO DE DADOS
for cadastro in cadastro: # PERCORRENDO TABELA
    print("TABELA FINAL: ", cadastro) # IMPRIMINDO RESULTADO FINAL
conn.commit() # CONFIRMANDO ALTERAÇÕES
    
conn.close() # ENCERRANDO CONSULTA
    
