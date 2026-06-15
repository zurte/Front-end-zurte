import tkinter as tk

janela = tk.Tk()
janela.title('Triagem')
janela.geometry('500x400')
janela.iconbitmap('dark-triangle.ico')

lista_equipamentos = ['desktop', 'notebook', 'impresora', 'monitor']

lista_prioridade = ['baixa','media','alta']

frame_1 = tk.Frame(janela, width = 500, height = 400)
frame_1.place(relx = 0.0, rely = 0.0)

equipamento = tk.StringVar(frame_1)#peguei de site

equipamento.set("selecione um equipamento")#peguei de site

prioridade = tk.StringVar(frame_1)

prioridade.set('prioridade')

#label de equipamento
lb_equipamento = tk.Label(frame_1, text='Tipo de equipamento', height = 2)
lb_equipamento.place(relx=0.0,rely=0.1)

#menu suspenso de equipamentos
opm_equipamentos = tk.OptionMenu(frame_1,equipamento,*lista_equipamentos)
opm_equipamentos.config(bg='lightgray')
opm_equipamentos.place(relx = 0.24, rely = 0.1)

#label de prioridade
lb_prioridade = tk.Label(frame_1, text='Prioridade', height = 2)
lb_prioridade.place(relx=0.0,rely=0.25)

#menu suspenso de prioridade
opm_prioridade = tk.OptionMenu(frame_1,prioridade,*lista_prioridade)
opm_prioridade.config(bg='lightgray')
opm_prioridade.place(relx=0.13,rely=0.25)

#checkbox
check_ligar = tk.Checkbutton(frame_1,text='A maquina liga?' )
check_ligar.place(relx=0.0,rely=0.35)

check_carregador = tk.Checkbutton(frame_1,text='A maquina acompanha carregador?' )
check_carregador.place(relx=0.0,rely=0.4)

check_backup = tk.Checkbutton(frame_1,text='Cliente autorizou backup?')
check_backup.place(relx=0.0,rely=0.45)

check_senha = tk.Checkbutton(frame_1,text='Possui senha de acesso?')
check_senha.place(relx=0.0,rely=0.5)

#botões
bt_registrar = tk.Button(frame_1, text='Registrar Triagem')
bt_registrar.place(relx=0.0,rely=0.6)

janela.mainloop()
