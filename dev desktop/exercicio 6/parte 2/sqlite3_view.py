import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite_model as model

win=tk.Tk()
win.title('Banco de dados')
win.geometry('600x400')

spc_y = 5

def salvar():

    p_patr = int(ent_patr.get().strip())
    p_setor = combo_setor.get()
    p_equip = combo_equip.get()
    p_prio = combo_prio.get()

    model.criar_banco(p_patr,p_setor,p_equip,p_prio)

   
def ler():
    print(model.ler_registros())


frm = tk.Frame(win,bg='cyan')
frm.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

#Patrimonio
lb_patr = tk.Label(frm,text='patrimonio')
lb_patr.pack(pady=spc_y)

ent_patr = tk.Entry(frm)
ent_patr.pack(pady=spc_y)

#equipamento
lb_equip = tk.Label(frm,text='equipamento')
lb_equip.pack(pady=spc_y)

combo_equip = ttk.Combobox(frm,values=('desktop','notebook','impressora','celular'))
combo_equip.pack(pady=spc_y)

#setor
lb_setor = tk.Label(frm,text='setor')
lb_setor.pack(pady=spc_y)

combo_setor = ttk.Combobox(frm,values=('financeiro','laboratoria','discarte','manutenção'))
combo_setor.pack(pady=spc_y)

#prioridade
lb_prio = tk.Label(frm,text='prioridade')
lb_prio.pack(pady=spc_y)

combo_prio = ttk.Combobox(frm,values=('baixo','medio','alta','urgente'))
combo_prio.pack(pady=spc_y)

#botão
bt_salvar = tk.Button(frm,text='salvar',command=salvar)
bt_salvar.pack(pady=spc_y)

bt_exibir = tk.Button(frm,text='exibir',command=ler)
bt_exibir.pack(pady=spc_y)

win.mainloop()
