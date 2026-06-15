import sqlite3 as sq

def criar_banco(patr,setor,equip,prio):

    valores = (patr,setor,equip,prio)
    
    conexao = sq.connect('Meu_banco_de_dados.db')

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registros (
        patrimonio INTEGER PRIMARY KEY,
        setor TEXT NOT NULL,
        equipamento TEXT NOT NULL,
        prioridade TEXT NOT NULL
    )
    """)

    cursor.execute("""
        INSERT INTO registros(patrimonio,setor,equipamento,prioridade)
        VALUES(?,?,?,?)

    """, valores)

    conexao.commit()
    conexao.close()

def ler_registros():
    conexao = sq.connect('Meu_banco_de_dados.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM registros")
    
    dados = cursor.fetchall()
    
    conexao.close()
    return dados
