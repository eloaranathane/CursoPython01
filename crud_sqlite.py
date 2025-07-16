import sqlite3

# Primeiro vamos nos conectar ao banco de dados (ou criar um novo se não existir)

def conectar_banco() :
    conexao = sqlite3.connect('exemplo.db') # Nome do banco de dados
    return conexao

# Criar tabela no novo banco exemplo.db
def criar_tabela() :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER       
        )
    ''')
    conexao.commit()
    conexao.close()

# Inserir dados na tabela
def inserir_usuario(campo_nome, campo_idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade) VALUES (?, ?)
    ''', (campo_nome, campo_idade))
    conexao.commit()
    conexao.close()

# Ler dados do banco
def inserir_usuario(campo_nome, campo_idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
    ''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

# Atualizar dados do banco
def inserir_usuario(id, novo_nome, nova_idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE usuarios
        SET nome = ?,
        idade = ?
        WHERE id = ?
    ''',(novo_nome, nova_idade, id))
    # Exemplo de explicação: VOU AO mercado COMPRAR uva, banana, maca SE DESEJAR ALGO ME AVISA
    conexao.commit()
    conexao.close()

# Excluir dados do banco
def inserir_usuario(campo_nome, campo_idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM usuarios WHERE id = ?
''',(id,))
    conexao.commit()
    conexao.close()

# Exemplos de uso das Funções CRUD

# Criar a tabela (execute um única vez)
criar_tabela()

# Inserir alguns dados!
inserir_usuario('Caio', 19)
inserir_usuario('Eloara', 32)
inserir_usuario('José', 60)
inserir_usuario('Nathan', 22)
inserir_usuario('Adilson', 30)
inserir_usuario('Rayane', 54)

# Ver os dados cadastrados
print("Ver dados antes de serem atualizados")
listar_usuarios()

# Atualizar a idade de um usuário!
atualizar_usuario(1, 'Eloara', 38)

# Listar usuarios após a atualização
print('\n Lista de usuarios atualizada')
listar_usuarios()

# Excluir usuario
excluir_usuario(1)

# Listar usuarios apos a exclusao
print('\n Lista de usuarios atualizada')
listar_usuarios()