import tkinter as tk
from tkinter import messagebox
import CadastroController as ct

def criar_interface():
    win= tk.Tk()
    win.title('Cadastro')
    win.geometry('512x288')

    win.rowconfigure(0, weight=1)
    win.columnconfigure(0, weight=1)

    spc_y = 5
    spc_x = 5
    
    #frames    
    frm_1 = tk.Frame(win,bg='black')
    frm_1.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

    #Nome
    lb_nome = tk.Label(frm_1,text='Nome')
    lb_nome.grid(row=0,column=0,sticky='nsew',padx=spc_x,pady=spc_y)

    ent_nome = tk.Entry(frm_1)
    ent_nome.grid(row=0,column=1,sticky='nsew',padx=spc_x,pady=spc_y)

    #numero
    lb_nmr = tk.Label(frm_1,text='Número')
    lb_nmr.grid(row=1,column=0,sticky='nsew',padx=spc_x,pady=spc_y)

    ent_nmr= tk.Entry(frm_1)
    ent_nmr.grid(row=1,column=1,sticky='nsew',padx=spc_x,pady=spc_y)

    #botão salvar
    bt_salvar = tk.Button(frm_1,text='salvar', command=lambda:ct.salvar(ent_nome,ent_nmr))
    bt_salvar.grid(row=2,column=0,sticky='nsew',padx=spc_x,pady=spc_y)
    

    win.mainloop()


