import tkinter as tk
from tkinter import ttk

def salvar():
    print('Dados salvos')

def limpar():
    print('Campos limpados')

janela = tk.Tk()
janela.title('Cadastro de Equipamentos')
janela.geometry('1024x576')

frm = tk.Frame(janela,width=1024,height=576, bg='black')
frm.place(relx=0.0,rely=0.0)

lb_1 = tk.Label(frm, text='Patrimonio',bg = 'purple',width=30, height=5, bd=3,relief=tk.RIDGE)
lb_1.place(relx = 0.03, rely = 0.4, anchor = 'w')

lb_2 = tk.Label(frm, text='Equipamento',bg = 'purple',width=30, height=5,  bd=3,relief=tk.RIDGE)
lb_2.place(relx = 0.4, rely = 0.4, anchor = 'w')

lb_3 = tk.Label(frm, text='Problema relatado',bg = 'purple',width=30, height=5,  bd=3,relief=tk.RIDGE)
lb_3.place(relx = 0.76, rely = 0.4, anchor = 'w')

entry_1 = tk.Entry(frm,width=35,bd=3,bg='darkgray')
entry_1.place(relx = 0.03, rely = 0.5)

entry_2 = tk.Entry(frm,width=35,bd=3,bg='darkgray')
entry_2.place(relx = 0.4, rely = 0.5)

entry_3 = tk.Entry(frm,width=35,bd=3,bg='darkgray')
entry_3.place(relx = 0.76, rely = 0.5)

botao_1 = tk.Button(frm, text='salvar',width=20,height=1,command=salvar)
botao_1.place(relx=0.03,rely=0.6)

botao_2 = tk.Button(frm, text='limpar',width=20,height=1,command=limpar)
botao_2.place(relx=0.2,rely=0.6)


janela.mainloop()
