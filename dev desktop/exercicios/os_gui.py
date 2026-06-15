import tkinter as tk

janela = tk.Tk()
janela.geometry('1024x576')
janela.title('Ordem de Serviço')
janela.iconbitmap('dark-triangle.ico')

cor_x = 0.35
bt_pad_x = 30

widget_color = '#69f5b4'
widget_color_2 = '#d6b0f7'

def atualizar_resolucao(event):
    w = janela.winfo_width()
    h = janela.winfo_height()

    #frame cliente
    frame_1.config(width=w/3,height=h/5)
    #frame equipamento
    frame_2.config(width=w/3,height=h/3)
    #frame checklist
    frame_3.config(width=w/3,height=h/3)
    #frame ações finais
    frame_4.config(width=w/3,height=h/16)

#box dados do cliente
frame_1 = tk.Frame(janela,bg=widget_color)
frame_1.place(relx=cor_x,rely=0.01)
frame_1.grid_propagate(False)

lb_nome = tk.Label(frame_1, text = 'nome do cliente', height=1, bg=widget_color)
lb_nome.grid(row=0,column=0, pady=10)

ent_nome = tk.Entry(frame_1,width=35,bg=widget_color_2)
ent_nome.grid(row=0,column=1, pady=20)

lb_telefone = tk.Label(frame_1, text = 'telefone', height=1, bg=widget_color)
lb_telefone.grid(row=1,column=0, pady=20)

ent_nome = tk.Entry(frame_1,width=35,bg=widget_color_2)
ent_nome.grid(row=1,column=1, pady=10)

#box equipamento
tipo_equipamento = ['DeskTop','NoteBook','Impressora','Celular']

tipo = tk.StringVar(janela)
tipo.set('escolha o tipo de equipamento')

frame_2 = tk.Frame(janela, bg=widget_color)
frame_2.place(relx=cor_x,rely=0.22)
frame_2.grid_propagate(False)

lb_tipo = tk.Label(frame_2,text='tipo de equipamento', bg=widget_color)
lb_tipo.grid(row=0,column=0,pady=10)

opm_tipo = tk.OptionMenu(frame_2, tipo, *tipo_equipamento)
opm_tipo.grid(row=0,column=1,pady=10)
opm_tipo.config(bg=widget_color,activebackground = widget_color_2,bd=0)

lb_marca = tk.Label(frame_2,text='marca', bg=widget_color)
lb_marca.grid(row=1,column=0,pady=10)

ent_marca = tk.Entry(frame_2,width=35,bg=widget_color_2)
ent_marca.grid(row=1,column=1,pady=10)

lb_modelo = tk.Label(frame_2,text='modelo', bg=widget_color)
lb_modelo.grid(row=2,column=0,pady=10)

ent_modelo = tk.Entry(frame_2,width=35,bg=widget_color_2)
ent_modelo.grid(row=2,column=1,pady=10)

lb_relatorio = tk.Label(frame_2,text='relatorio', bg=widget_color)
lb_relatorio.grid(row=3,column=0,pady=10)

ent_relatorio = tk.Entry(frame_2,width=35,bg=widget_color_2)
ent_relatorio.grid(row=3,column=1,pady=10)

#box checklist
frame_3 = tk.Frame(janela, bg=widget_color)
frame_3.place(relx=cor_x,rely=0.57)
frame_3.grid_propagate(False)

chk_liga = tk.Checkbutton(frame_3,text='equipamento liga',bg=widget_color)
chk_liga.grid(row=0,column=0,pady=10)

chk_carregador = tk.Checkbutton(frame_3,text='acompanha carregador',bg=widget_color)
chk_carregador.grid(row=1,column=0,pady=10)

chk_backup = tk.Checkbutton(frame_3,text='autorização para backup',bg=widget_color)
chk_backup.grid(row=2,column=0,pady=10)

chk_video = tk.Checkbutton(frame_3,text='aperelho da video',bg=widget_color)
chk_video.grid(row=3,column=0,pady=10)

#box botões
frame_4 = tk.Frame(janela, bg=widget_color)
frame_4.place(relx=cor_x,rely=0.92)
frame_4.grid_propagate(False)

bt_salvar = tk.Button(frame_4,text='salvar OS', bg=widget_color, activebackground = widget_color_2)
bt_salvar.grid(row=0,column=0,padx=bt_pad_x,pady=5)

bt_limpar = tk.Button(frame_4,text='limpar', bg=widget_color, activebackground = widget_color_2)
bt_limpar.grid(row=0,column=1,padx=bt_pad_x,pady=5)

bt_fechar = tk.Button(frame_4,text='fechar', bg=widget_color, activebackground = widget_color_2)
bt_fechar.grid(row=0,column=2,padx=bt_pad_x,pady=5)

#atualiza dimenções quado tela é redimencionada
janela.bind('<Configure>', atualizar_resolucao)

janela.mainloop()
