
banco_equipamentos = {}

def salvar_equipamentos(patrimonio, tipo, setor, status):
    
    banco_equipamentos[patrimonio] = [tipo, setor, status]
    
    print(banco_equipamentos)
    
