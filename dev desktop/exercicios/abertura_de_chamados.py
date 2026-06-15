import tkinter as tk
from tkinter import messagebox,filedialog

spc_x = 5
spc_y = 5

def validar_dados():

    valido = True
    
    if ent_nome.get().strip() == '':
        tk.messagebox.showwarning('atenção','Insira um NOME')

        valido = False
        
    elif ent_ptrm.get().strip() == '':
        tk.messagebox.showwarning('atenção','Insira um PATRIMONIO')

        valido = False
        
    elif texto_base.get() == 'Escolha a Prioridade':
        tk.messagebox.showwarning('atenção','Escolha uma PRIORIDADE')

        valido = False
        
    elif ent_descr.get().strip() == '':
        tk.messagebox.showwarning('atenção','Insira uma DESCRIÇÃO')

        valido = False

    return valido

def salvar(event):

    if validar_dados():
        tk.messagebox.showinfo('Boaaa','Chamado salvo')

def limpar_dados():

    if tk.messagebox.askyesno('Certeza?','Quer mesmo limpar tudo?'):

       ent_nome.delete(0,tk.END)
       ent_ptrm.delete(0,tk.END)
       ent_descr.delete(0,tk.END)

       texto_base.set('Escolha a Prioridade')

def selecionar_anexo():

    anx.set(tk.filedialog.askopenfilename(title='Escolha um Arquivo'))

win = tk.Tk()
win.title('Chamados')
win.geometry('512x288')
win.bind('<Control-s>',salvar)

ls_prio = ['baixa','média','alta']

texto_base = tk.StringVar(win)
texto_base.set('Escolha a Prioridade')

anx = tk.StringVar(win)
anx.set('anexar arquivo')

frm_1 = tk.Frame(win,bg='cyan')
frm_1.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

#Labels
lb_nome = tk.Label(frm_1,text='Nome')
lb_nome.grid(row=0,column=0,padx=spc_x,pady=spc_y)

lb_ptrm = tk.Label(frm_1,text='Patrimonio')
lb_ptrm.grid(row=1,column=0,padx=spc_x,pady=spc_y)

lb_prio = tk.Label(frm_1,text='Prioridade')
lb_prio.grid(row=2,column=0,padx=spc_x,pady=spc_y)

lb_descr = tk.Label(frm_1,text='Descrição de Problema')
lb_descr.grid(row=3,column=0,padx=spc_x,pady=spc_y)

lb_anx = tk.Label(frm_1,textvariable=anx)
lb_anx.grid(row=5,column=0,padx=spc_x,pady=spc_y)

#Entrys
ent_nome = tk.Entry(frm_1,width=30)
ent_nome.grid(row=0,column=1,padx=spc_x,pady=spc_y)

ent_ptrm = tk.Entry(frm_1,width=30)
ent_ptrm.grid(row=1,column=1,padx=spc_x,pady=spc_y)

ent_descr = tk.Entry(frm_1,width=30)
ent_descr.grid(row=3,column=1,padx=spc_x,pady=spc_y)

#Menu Suspenso
opm_prio = tk.OptionMenu(frm_1, texto_base, *ls_prio)
opm_prio.grid(row=2,column=1)

#botões
bt_salvar = tk.Button(frm_1,text='salvar',command=salvar)
bt_salvar.grid(row=4,column=0,padx=spc_x,pady=spc_y)

bt_limpar = tk.Button(frm_1,text='limpar',command=limpar_dados)
bt_limpar.grid(row=4,column=1,padx=spc_x,pady=spc_y)

bt_anexo = tk.Button(frm_1,text='seleciona anexo',command=selecionar_anexo)
bt_anexo.grid(row=5,column=1,padx=spc_x,pady=spc_y)


win.mainloop()
