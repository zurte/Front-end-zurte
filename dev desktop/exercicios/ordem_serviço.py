import tkinter as tk

janela = tk.Tk()
janela.title('Ordem de Serviço')
janela.geometry('500x400')
janela.iconbitmap('dark-triangle.ico')
def ajustar_frame(event):
    w = janela.winfo_width()
    h = janela.winfo_height()

    frame_1.config(width =w,height=h)

#frame
frame_1 = tk.Frame(janela)
frame_1.grid(row=0,column=0)
frame_1.grid_propagate(False)

janela.bind('<Configure>', ajustar_frame)

spc_y = 10

ls_prioridade = ['baixa','media','alta','muito alta']
ls_status = ['recebido','analise','em andamento','concluido','cancelado']
ls_equipamento = ['Desktop','notebook','Impressora','celular']

prioridade = tk.StringVar(frame_1)
prioridade.set('escolha o nivel de prioridade')

status = tk.StringVar(frame_1)
status.set('escolha os status da OS')

equipamento = tk.StringVar(frame_1)
equipamento.set('escolha qual o tipo de equipamento')

#numero de ordens de serviço
lb_nmr_os = tk.Label(frame_1, text='numero de ordem de serviço')
lb_nmr_os.grid(row=0,column=0,pady=spc_y)

ent_nmr_os = tk.Entry(frame_1, width=30, bg='#7d85db')
ent_nmr_os.grid(row=0,column=1)

#opções prioridade
lb_prioridade = tk.Label(frame_1, text='prioridade')
lb_prioridade.grid(row=1,column=0,pady=spc_y)

opm_prioridade = tk.OptionMenu(frame_1,prioridade,*ls_prioridade)
opm_prioridade.grid(row=1,column=1)

#staus de ordem de serviço
lb_status = tk.Label(frame_1, text='status')
lb_status.grid(row=2,column=0,pady=spc_y)

opm_status = tk.OptionMenu(frame_1,status,*ls_status)
opm_status.grid(row=2,column=1)

#tipo de equipamento
lb_equipamento = tk.Label(frame_1, text='equipamento')
lb_equipamento.grid(row=3,column=0,pady=spc_y)

opm_equipamento = tk.OptionMenu(frame_1,equipamento,*ls_equipamento)
opm_equipamento.grid(row=3,column=1)


janela.mainloop()
