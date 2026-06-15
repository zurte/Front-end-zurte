import csv
import json

equipamentos_cadastrados = [
    {
        "patrimonio": 1001,
        "setor": "TI",
        "equipamento": "Notebook Dell Vostro",
        "prioridade": "Alta"
    },
    {
        "patrimonio": 1002,
        "setor": "Recepção",
        "equipamento": "Impressora HP Laserjet",
        "prioridade": "Média"
    },
    {
        "patrimonio": 1003,
        "setor": "Financeiro",
        "equipamento": "Monitor LG 24'",
        "prioridade": "Baixa"
    },
    {
        "patrimonio": 1004,
        "setor": "Suporte",
        "equipamento": "Headset Logitech",
        "prioridade": "Alta"
    }
]

def criar_txt():
    with open('Inventario de equipamento.txt','w',encoding="utf-8") as arquivo:
        arquivo.write('===Relatorio de Equipamentos===\n\n')

        for equip in equipamentos_cadastrados:
            linha = f"Patrimônio: {equip['patrimonio']} | Equipamento: {equip['equipamento']} | Setor: {equip['setor']} | Prioridade: {equip['prioridade']}\n"
            arquivo.write(linha)

    print("Relatório 'inventario_equipamentos.txt' gerado!")

def criar_csv():

    campos = ['patrimonio', 'setor', 'equipamento', 'prioridade']
    
    with open('Inventario de equipamento.csv','w',encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo,fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(equipamentos_cadastrados)

    print("Relatório 'inventario_equipamentos.csv' gerado!")

def ler_csv():
    try:
        with open('Inventario de equipamento.csv', 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            print("--- LENDO DADOS DO ARQUIVO CSV ---")
            for linha in leitor:
                print(f"Patrimônio: {linha['patrimonio']} | Equipamento: {linha['equipamento']} | Setor: {linha['setor']}")
                
    except FileNotFoundError:
        print("Erro: O arquivo CSV ainda não foi gerado pelo sistema.")

def criar_json():
    with open('Inventario de equipamento.json','w',encoding="utf-8") as arquivo:
        arquivo.write('===Relatorio de Equipamentos===\n\n')

        json.dump(equipamentos_cadastrados,arquivo,indent=5,ensure_ascii=False)

    print("Relatório 'inventario_equipamentos.json' gerado!")
