import urllib.request
import json

def consultar_cep(cep_dig):
    cep = cep_dig.strip().replace('-','').replace('.','')

    if len(cep) !=8 or not cep.isdigit():
        return {'error':True,'mensagem':'cep inválido'}

    url = f'https://viacep.com.br/ws/{cep}/json/'


    try:
        with urllib.request.urlopen(url) as resposta:

            dados = resposta.read().decode('utf-8')

            endereco = json.loads(dados)

        if 'error' in endereco:
            return {'error':True,'mensagem':'cep não encontrado'}

        endereco['error'] = False
        return endereco

    except Exception:
        
        return {"error": True, "mensagem": "Erro de conexão. Verifique sua internet."}
