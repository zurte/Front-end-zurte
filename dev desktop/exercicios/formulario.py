import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title('Formulario')
janela.geometry('500x400')

def validar_dados():

    correto = True
    
    if ent_nome.get().strip() == '':
        tk.messagebox.showwarning('atenção','prencha o campo NOME')

        correto = False

    elif ent_idade.get().isdigit() == False:
        tk.messagebox.showwarning('atenção','prencha o campo IDADE apenas com NÙMEROS')

        correto = False

    elif ent_patrimonio.get().strip() == '':
        tk.messagebox.showwarning('atenção','prencha o campo PATRIMONIO')

        correto = False

    if correto:
        idade = int(ent_idade.get())
        

        tk.messagebox.showinfo('sucesso','cadastro finalizado')

    

#Frame
frame_1 = tk.Frame(janela, bg='black')
frame_1.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)
frame_1.grid_propagate(False)

spc_y = 5
spc_x = 5
#nome
lb_nome = tk.Label(frame_1,text='Nome')
lb_nome.grid(row=0,column=0, pady = spc_y, padx=spc_x)

ent_nome = tk.Entry(frame_1)
ent_nome.grid(row=0,column=1, pady = spc_y, padx=spc_x)

#idade
lb_idade = tk.Label(frame_1,text='idade')
lb_idade.grid(row=1,column=0)

ent_idade = tk.Entry(frame_1)
ent_idade.grid(row=1,column=1, pady = spc_y, padx=spc_x)

#patrimonio
lb_patrimonio = tk.Label(frame_1,text='patrimonio')
lb_patrimonio.grid(row=2,column=0)

ent_patrimonio = tk.Entry(frame_1)
ent_patrimonio.grid(row=2,column=1, pady = spc_y, padx=spc_x)

#botões
bt_salvar = tk.Button(frame_1,text='salvar',command=validar_dados)
bt_salvar.grid(row=3,column=0)

janela.mainloop()
