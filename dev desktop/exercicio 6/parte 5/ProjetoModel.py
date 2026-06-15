import sqlite3 as sq

def criar_tabela(patr,equip,defeito,cep):

    valores = (patr,equip,defeito,cep)
    
    conexao = sq.connect('banco.db')

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registros(
    patrimonio INTEGER PRIMARY KEY,
    equipamento TEXT NOT NULL,
    defeito TEXT NOT NULL,
    cep INTEGER NOT NULL
    )
    
""")

    cursor.execute("""
    INSERT INTO registros(patrimonio,equipamento,defeito,cep)
    VALUES(?,?,?,?)
""",valores)

    print('tabela criada')
    conexao.commit()
    conexao.close()

def ler_dados():
    
    conexao = sq.connect('banco.db')

    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM registros""")

    dados = cursor.fetchall()

    conexao.close()

    return dados
