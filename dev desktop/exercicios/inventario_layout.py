import tkinter as tk

janela = tk.Tk()
janela.title('Sistema de Inventario')
janela.geometry('500x400')
janela.iconbitmap('dark-triangle.ico')


#Criando frame
frame_1 = tk.Frame(janela, width=500, height=400, bg= 'black')
frame_1.grid(row=0,column=0)

#Criando label
espacamento_y = 10

#patrimonio
lb_patrimonio = tk.Label(frame_1,text='Patrimonio',height=1)
lb_patrimonio.grid(row=0,column=0,pady=espacamento_y)

ent_patrimonio = tk.Entry(frame_1, bg='#5c6287', width = 40)
ent_patrimonio.grid(row=0,column=1)

#tipo
lb_tipo = tk.Label(frame_1,text='tipo',height=1)
lb_tipo.grid(row=1,column=0,pady=espacamento_y) 

ent_tipo = tk.Entry(frame_1, bg='#5c6287', width = 40)
ent_tipo.grid(row=1,column=1)

#marca
lb_marca = tk.Label(frame_1,text='marca',height=1)
lb_marca.grid(row=2,column=0,pady=espacamento_y)

ent_marca = tk.Entry(frame_1, bg='#5c6287', width = 40)
ent_marca.grid(row=2,column=1)

#modelo
lb_modelo = tk.Label(frame_1,text='modelo',height=1)
lb_modelo.grid(row=3,column=0,pady=espacamento_y)

ent_modelo = tk.Entry(frame_1, bg='#5c6287', width = 40)
ent_modelo.grid(row=3,column=1)

#localizaçao
lb_localizacao = tk.Label(frame_1,text='localização',height=1)
lb_localizacao.grid(row=4,column=0,pady=espacamento_y)

ent_localizacao = tk.Entry(frame_1, bg='#5c6287', width = 40)
ent_localizacao.grid(row=4,column=1)

#observações
lb_obs = tk.Label(frame_1,text='observação',height=1)
lb_obs.grid(row=5,column=0,pady=espacamento_y)

ent_obs = tk.Entry(frame_1, bg='#5c6287', width = 40)
ent_obs.grid(row=5,column=1)

#botões
bt_salvar = tk.Button(frame_1,text='Salvar')
bt_salvar.grid(row=6,column=0)

bt_novo = tk.Button(frame_1,text='Novo')
bt_novo.grid(row=6,column=1)

bt_fecha = tk.Button(frame_1,text='Fechar')
bt_fecha.grid(row=6,column=2)

janela.mainloop()
