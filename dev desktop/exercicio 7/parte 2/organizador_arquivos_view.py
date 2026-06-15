import tkinter as tk
from tkinter import filedialog

spc_y = 2

def selecionar_pasta():
    pasta_selecionada = tk.filedialog.askdirectory(title='Escolha a pasta destino')
    lb_caminho.config(text=pasta_selecionada)
    return pasta_selecionada

win = tk.Tk()
win.title('Organizador de Arquivos')
win.geometry('600x400')

frm = tk.Frame(win,bg='darkgray')
frm.place(relx = 0.0, rely = 0.0, relwidth=1.0, relheight = 1.0)

lb_caminho = tk.Label(frm,text='...')
lb_caminho.pack(pady=spc_y*20)

bt_selecionar = tk.Button(frm,text='Escolher Pasta destino',command=selecionar_pasta)
bt_selecionar.pack(pady=spc_y)

bt_analizar = tk.Button(frm,text='Analisar Pasta')
bt_analizar.pack(pady=spc_y)

bt_organizar = tk.Button(frm,text='Organizar Arquivos')
bt_organizar.pack(pady=spc_y)

win.mainloop()
