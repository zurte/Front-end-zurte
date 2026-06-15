import tkinter as tk

janela = tk.Tk()
janela.geometry('500x400')
janela.title('Triagem de paciente')

frame_1 = tk.Frame(janela, width=500, height=400, bg= 'black')
frame_1.place(relx=0.0,rely=0.0)

#campo para o nome do paciente
lb_paciente = tk.Label(frame_1, text='Nome do paciente',height=1)
lb_paciente.place(relx=0.0,rely=0.1)

et_paciente = tk.Entry(frame_1,width=30,bg='lightgray')
et_paciente.place(relx=0.22,rely=0.1)

#menu suspenso de tipo de atendimento
valor_tipo = tk.StringVar(janela)
valor_tipo.set('escolha o tipo de atendimento')

ls_atendimento = ['emergência', 'consultas de rotina','acompanhamentos especializados']

lb_tipo = tk.Label(frame_1, text='tipo de atendimento',height=1)
lb_tipo.place(relx=0.0,rely=0.2)

opm_tipo = tk.OptionMenu(frame_1, valor_tipo,*ls_atendimento)
opm_tipo.place(relx=0.22,rely=0.18)

#menu suspenso de setor destino
valor_setor = tk.StringVar(janela)
valor_setor.set('escolha o setor')

ls_setores = ['consultorio', 'sala de cirurgia','salada de medicação']

lb_setor = tk.Label(frame_1, text='setor destinado',height=1)
lb_setor.place(relx=0.0,rely=0.3)

opm_setor = tk.OptionMenu(frame_1, valor_setor,*ls_setores)
opm_setor.place(relx=0.18,rely=0.28)

#Checkbox
check_prioritario = tk.Checkbutton(frame_1,text='Paciente prioritario')
check_prioritario.place(relx=0.0,rely=0.4)
check_retorno = tk.Checkbutton(frame_1,text='retorno')
check_retorno.place(relx=0.0,rely=0.45)
check_plano = tk.Checkbutton(frame_1,text='Plano de saúde')
check_plano.place(relx=0.0,rely=0.5)
check_horario = tk.Checkbutton(frame_1,text='Horario marcada')
check_horario.place(relx=0.0,rely=0.55)

janela.mainloop()
