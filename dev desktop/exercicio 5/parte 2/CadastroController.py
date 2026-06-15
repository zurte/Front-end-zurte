def validar_dados(ent_nome, ent_nmr):
    import tkinter as tk
    from tkinter import messagebox
    
    valido = True
    
    if ent_nome.get().strip()== '':
        tk.messagebox.showwarning('Atenção','Preencha o campo Nome')
        valido = False

    elif not ent_nmr.get().strip().isdigit():
        tk.messagebox.showwarning('Atançao','Preencha o campo de numero com apenas numeros')
        valido= False

    return valido

def salvar(ent_nome,ent_nmr):
    import tkinter as tk
    from tkinter import messagebox
    
    if validar_dados(ent_nome,ent_nmr):
        tk.messagebox.showinfo('Sucesso','Cadastro finalizado')
