# View.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import queue
import Controller as ct

# Inicialização da janela principal
win = tk.Tk()
win.title("Diagnóstico Técnico")
win.geometry("450x350")

# Fila segura de comunicação global entre a Thread e a Interface
fila_interface = queue.Queue()

# --- MONITOR DA FILA (O coração do dinamismo da tela) ---
def checar_fila():
    try:
        # Tenta capturar dados imediatamente sem esperar
        mensagem = fila_interface.get_nowait()
        
        if mensagem.startswith("SUCESSO:"):
            # O Diagnóstico acabou bem
            texto_limpo = mensagem.replace("SUCESSO: ", "")
            lb_status.config(text=texto_limpo, fg="green")
            bt_iniciar.config(state="normal") # Devolve o botão ao usuário
            
        elif mensagem.startswith("ERRO:"):
            # Ocorreu um problema na Thread
            texto_limpo = mensagem.replace("ERRO: ", "")
            lb_status.config(text=texto_limpo, fg="red")
            bt_iniciar.config(state="normal")
            
        else:
            # Mensagens de etapas intermediárias
            lb_status.config(text=mensagem, fg="blue")
            
    except queue.Empty:
        # Se a fila estiver vazia temporariamente, ignora sem quebrar o app
        pass

    # Agenda a própria função para rodar de novo em 100 milissegundos
    win.after(100, checar_fila)

# --- AÇÃO DO BOTÃO ---
def acao_iniciar():
    # Coleta strings limpas da tela
    patrimonio_digitado = ent_patrimonio.get()
    setor_selecionado = combo_setor.get()
    
    # Pergunta ao controller se os campos estão corretos
    msg, valido = ct.validar_campos(patrimonio_digitado, setor_selecionado)
    
    if not valido:
        messagebox.showwarning("Atenção", msg)
        return
        
    # Se os campos forem válidos, bloqueia o botão e muda o status inicial
    bt_iniciar.config(state="disabled")
    lb_status.config(text="Preparando ambiente...", fg="orange")
    
    # Passa as strings e a FILA para o controller dar partida na Thread
    ct.iniciar_diagnostico(patrimonio_digitado, setor_selecionado, fila_interface)

# --- INTERFACE GRÁFICA (WIDGETS) ---

# Título
lb_titulo = tk.Label(win, text="Ferramenta de Diagnóstico Técnico", font=("Arial", 12, "bold"))
lb_titulo.pack(pady=15)

# Campo de Patrimônio
lb_patrimonio = tk.Label(win, text="Nº de Patrimônio:")
lb_patrimonio.pack()
ent_patrimonio = tk.Entry(win, width=30)
ent_patrimonio.pack(pady=5)

# Campo de Setor (Combobox)
lb_setor = tk.Label(win, text="Setor do Equipamento:")
lb_setor.pack()
combo_setor = ttk.Combobox(win, values=["Laboratório de T.I", "Administrativo", "Financeiro", "Diretoria"], width=27)
combo_setor.set("Escolha o setor")
combo_setor.pack(pady=5)

# Botão de Ação
bt_iniciar = tk.Button(win, text="Iniciar Diagnóstico", command=acao_iniciar, bg="#e1e1e1", font=("Arial", 10, "bold"))
bt_iniciar.pack(pady=20)

# Área de Status Dinâmico
lb_borda_status = tk.LabelFrame(win, text=" Status do Processamento ", padx=10, pady=10)
lb_borda_status.pack(fill="x", padx=20, pady=10)

lb_status = tk.Label(lb_borda_status, text="Aguardando início...", font=("Arial", 10, "italic"), fg="gray")
lb_status.pack()

# ATIVAÇÃO DO CRONÔMETRO: Liga a vigilância da fila assim que a View carrega
win.after(100, checar_fila)
