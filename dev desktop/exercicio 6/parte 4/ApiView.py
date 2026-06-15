import tkinter as tk
from tkinter import messagebox

import ApiController as ct

spc_y = 5

def buscar():
    cep_user = ent_cep.get()

    resultado = ct.consultar_cep(cep_user)

    if resultado['erro']:
        tk.messagebox.showerror('Erro',resultado['mensagem'])
    else:
        lb_logradouro.config(text=f"Rua: {resultado.get('logradouro', '')}")
        lb_bairro.config(text=f"Bairro: {resultado.get('bairro', '')}")
        lb_cidade.config(text=f"Cidade: {resultado.get('localidade', '')}")
        lb_estado.config(text=f"Estado: {resultado.get('uf', '')}")

def limpar():
    lb_logradouro.config(text="Rua: ")
    lb_bairro.config(text='Bairro: ')
    lb_cidade.config(text='Cidade: ')
    lb_estado.config(text='Estada: ')
    
win = tk.Tk()
win.title('Usando API de CEP')
win.geometry('600x400')

frm = tk.Frame(win,bg='darkred')
frm.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

ent_cep = tk.Entry(frm)
ent_cep.pack(pady = spc_y)

bt_cons = tk.Button(frm,text='Consultar',command=buscar)
bt_cons.pack(pady = spc_y)

bt_limpar = tk.Button(frm,text='Limpar',command=limpar)
bt_limpar.pack(pady = spc_y)

lb_logradouro = tk.Label(frm,text='Rua: ')
lb_logradouro.pack(pady=spc_y)

lb_bairro = tk.Label(frm,text='Bairro: ')
lb_bairro.pack(pady=spc_y)

lb_cidade = tk.Label(frm,text='Cidade: ')
lb_cidade.pack(pady=spc_y)

lb_estado = tk.Label(frm,text='Estado: : ')
lb_estado.pack(pady=spc_y)

win.mainloop()
