import tkinter as tk

janela = tk.Tk()
janela.title('Cadastro de quipamentos')
janela.geometry('500x500')
janela.iconbitmap('dark-triangle.ico')


frame_1 = tk.Frame(janela, width = 500, height = 500)
frame_1.place(relx=0.0,rely=0.0)

titulo = tk.Label(frame_1, text = 'Cadastro de quipamento',width=75, height=2, bd=3,relief=tk.SUNKEN)
titulo.place(relx=0.0,rely=0.0)

#Criando campo de patrimonio
lb_patrimonio = tk.Label(frame_1,text = 'Patrimonio' ,width = 20, height = 1, bd=3,relief=tk.SUNKEN)
lb_patrimonio.place(relx = 0.0,rely = 0.1)

et_patrimonio = tk.Entry(frame_1,bg='lightgray',bd=3,width = 50,relief=tk.SUNKEN)
et_patrimonio.place(relx=0.3,rely=0.1)

#Criando campo de equipamento
lb_equipamento = tk.Label(frame_1,text = 'Equipamento' ,width = 20, height = 1, bd=3,relief=tk.SUNKEN)
lb_equipamento.place(relx = 0.0,rely = 0.2)

et_equipamento = tk.Entry(frame_1,bg='lightgray',bd=3,width = 50,relief=tk.SUNKEN)
et_equipamento.place(relx=0.3,rely=0.2)

#Criando campo de setor
lb_setor = tk.Label(frame_1,text = 'Setor' ,width = 20, height = 1, bd=3,relief=tk.SUNKEN)
lb_setor.place(relx = 0.0,rely = 0.3)

et_setor = tk.Entry(frame_1,bg='lightgray',bd=3,width = 50,relief=tk.SUNKEN)
et_setor.place(relx=0.3,rely=0.3)

#Criando campo de descrição de problema
lb_problema = tk.Label(frame_1,text = 'Problema' ,width = 20, height = 2, bd=3,relief=tk.SUNKEN)
lb_problema.place(relx = 0.0,rely = 0.4)

et_problema = tk.Entry(frame_1,bg='lightgray',bd=3,width = 50,relief=tk.SUNKEN)
et_problema.place(relx=0.3,rely=0.4)

#Criando botões
bt_salvar = tk.Button(janela, text = 'salvar', width = 20, bg='lightgray')
bt_salvar.place(relx=0.0, rely = 0.5)

bt_limpar = tk.Button(janela, text = 'limpar', width = 20, bg='lightgray')
bt_limpar.place(relx=0.3, rely = 0.5)
