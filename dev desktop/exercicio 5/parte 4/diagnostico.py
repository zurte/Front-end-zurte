import tkinter as tk
import threading
import queue
import time

win = tk.Tk()
win.title('Iniciar diagnóstico')
win.geometry('500x400')

fila = queue.Queue()

def criando_personagem():

    fila.put('escolhendo a aparencia do personagem...')
    time.sleep(2)

    fila.put('escolhendo a classe do personagem...')
    time.sleep(2)

    fila.put('escolhendo um nickname...')
    time.sleep(2)

    fila.put('personagem criado')

def checar_criacao():
    try:

        mensagem = fila.get_nowait()
        
        if mensagem == 'personagem criado':
            lb_status.config(text=mensagem)
            bt_criar.config(state='normal')

        else:
            lb_status.config(text=mensagem)

    except queue.Empty:

        pass

    win.after(100,checar_criacao)
    

def comecar():

    bt_criar.config(state='disabled')
    lb_status.config(text='iniciando...')

    thread = threading.Thread(target=criando_personagem)

    thread.start()

lb_status = tk.Label(win,text='aguardando')
lb_status.place(relx=0.5,rely=0.3)

bt_criar = tk.Button(win,text='criar',command=comecar)
bt_criar.place(relx=0.5,rely=0.5)

win.after(100,checar_criacao)

win.mainloop()
