# Controller.py
import threading
import time
import Model

def validar_campos(patrimonio, setor):
    """Garante que nenhum campo foi enviado vazio ou padrão"""
    if patrimonio.strip() == "":
        return "Erro: O campo Patrimônio precisa ser preenchido.", False
    if not patrimonio.strip().isdigit():
        return "Erro: O Patrimônio deve conter apenas números.", False
    if setor.lower().strip() == "escolha o setor":
        return "Erro: Selecione um setor válido.", False
    return "Campos válidos!", True

def tarefa_diagnostico(patrimonio, setor, fila_comunicacao):
    """
    Função que roda inteiramente na Thread Secundária.
    Ela coloca strings na fila para atualizar a View aos poucos.
    """
    try:
        fila_comunicacao.put("Iniciando varredura de hardware...")
        time.sleep(2)
        
        fila_comunicacao.put("Analisando integridade dos arquivos locais...")
        time.sleep(2)
        
        fila_comunicacao.put("Testando conexão com os servidores do setor...")
        time.sleep(2)
        
        # Se chegou aqui, deu tudo certo
        resultado_final = "Equipamento Saudável / Pronto para Uso"
        
        # Envia o resultado final para salvar no Model
        Model.salvar_relatorio_diagnostico(patrimonio, setor, resultado_final)
        
        # Alerta a View que o processo acabou com Sucesso
        fila_comunicacao.put(f"SUCESSO: {resultado_final}")
        
    except Exception as e:
        fila_comunicacao.put(f"ERRO: Falha crítica no diagnóstico: {str(e)}")

def iniciar_diagnostico(patrimonio, setor, fila_comunicacao):
    """Abre um novo processo (Thread) para não congelar a janela principal"""
    # Dispara o 'trabalhador' em segundo plano
    thread_trabalho = threading.Thread(
        target=tarefa_diagnostico, 
        args=(patrimonio, setor, fila_comunicacao)
    )
    thread_trabalho.start()
