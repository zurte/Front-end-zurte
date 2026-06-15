import tkinter as tk
from tkinter import ttk


win = tk.Tk()
win.title('Percistencia')
win.geometry('600x400')

spc_y = 5

classes = ['guerreiro','mago','assassino','arqueiro']
memoria_persistente = {}

def salvar():
    nome = ent_nome.get()
    classe = combo_classe.get()
    genero = combo_genero.get()

    if not (nome.strip() == '' and classe == '' and genero == ''):
        memoria_persistente[nome] = (genero,classe)

    print(memoria_persistente)

frm = tk.Frame(win,bg='black')
frm.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

#Nome de personagem
lb_nome = tk.Label(frm,text='Escolha um nickname:')
lb_nome.pack(pady=spc_y)

ent_nome = tk.Entry(frm)
ent_nome.pack(pady=spc_y)

#classe do personagem
lb_classe = tk.Label(frm,text='escolha uma classe:')
lb_classe.pack(pady=spc_y)

combo_classe = ttk.Combobox(frm,values=classes)
combo_classe.pack(pady=spc_y)

#genero do personagem
lb_genero = tk.Label(frm,text='escolha um genero:')
lb_genero.pack(pady=spc_y)

combo_genero = ttk.Combobox(frm,values=('Masculino','Feminino'))
combo_genero.pack(pady=spc_y)

#botão
bt_salvar = tk.Button(frm,text='criar',command=salvar)
bt_salvar.pack(pady=spc_y)


win.mainloop()
