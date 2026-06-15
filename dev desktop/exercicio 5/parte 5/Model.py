# Model.py

def salvar_relatorio_diagnostico(patrimonio, setor, resultado):
    """
    Simula a gravação do diagnóstico em um banco de dados ou arquivo.
    """
    relatorio = {
        "patrimonio": patrimonio,
        "setor": setor,
        "status_final": resultado
    }
    print(f"\n[MODEL] Relatório gravado com sucesso no sistema: {relatorio}")
    return True
