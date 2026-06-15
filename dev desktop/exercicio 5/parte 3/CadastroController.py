import CadastroModel as model

def validar_dados(patrimonio, tipo, setor, status):

    valido = True
    if patrimonio == '':
        valido = False
        return 'Preencha o campo de patrimonio',valido
        
    elif patrimonio.isdigit() == False:
        valido = False
        return 'Preencha patrimonio apenas com números',valido
        
    elif tipo == 'escolha o tipo de equipamento':
        valido = False
        return 'Escolha o tipo de equipamento',valido
        
    elif setor == 'escolha o setor':
        valido = False
        return 'Escolha o setor',valido
        
    elif status == 'escolha o status do cadastro':
        valido = False
        return 'Escolha o status',valido
        
    return 'pronto',valido

def salvar_dados(patrimonio, tipo, setor, status):
    mensagem,resultado = validar_dados(patrimonio, tipo, setor, status)
    
    if resultado == True:
        model.salvar_equipamentos(patrimonio, tipo, setor, status)
        return 'dados salvos',True
        
    return mensagem,resultado
