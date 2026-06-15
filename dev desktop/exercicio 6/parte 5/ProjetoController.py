import ViaCep 
import ProjetoModel as model
import csv
import json

def validar(patr,equip,defeito,cep):
    if patr == '' or not patr.isdigit():
        return {'error':True,'mensagem':'Patrimonio vazio'}
    elif equip == '':
         return {'error':True,'mensagem':'Equipamento não escolhido'}
    elif defeito == '':
         return {'error':True,'mensagem':'Defeito vazio'}
        
    resultado_cep = ViaCep.consultar_cep(cep)
    
    if resultado_cep['error']:
        return {'error': True, 'mensagem': resultado_cep['mensagem']}
        

    return {'error': False,'mensagem': 'Dados Validados!','dados_endereco': resultado_cep}

def criar_csv(): 
    try:
        valores = model.ler_dados()
        
        with open('Registros.csv','w',encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow(['patrimonio','equipamento','defeito','cep'])

            escritor.writerows(valores)
            
    except FileNotFoundError:
        print("Erro: O arquivo CSV ainda não foi gerado pelo sistema.")
        
    print("Relatório 'Registros.csv' gerado!")
    
def criar_json():
    with open('Registros.json','w',encoding="utf-8") as arquivo:
        arquivo.write('===Regsitros===\n\n')

        valores = model.ler_dados()

        json.dump(valores,arquivo,indent=5,ensure_ascii=False)

    print("Relatório 'Registros.json' gerado!")
