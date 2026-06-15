import tkinter as tk
    

janela = tk.Tk()
janela.title('Painel de Eventos')
janela.geometry('500x400')

k = tk.StringVar(janela)
x = tk.IntVar(janela)
y = tk.IntVar(janela)
s = tk.StringVar(janela)

def registrar_tecla(event):

    k.set(event.keysym)

    print(f'{k}')

def coordenadas_mouse(event):

    x.set(event.x)
    y.set(event.y)

    print(f'X:{x}/Y:{y}')

def salvar(event):

    s.set('Salvo')
    

janela.bind('<Key>',registrar_tecla)
janela.bind('<Motion>',coordenadas_mouse)
janela.bind('<Control-s>',salvar)


#Frames
frame_1 = tk.Frame(janela,width=500,height=400)
frame_1.place(relx=0.0,rely=0.0)
frame_1.grid_propagate(False)

#labels
lb_tecla_text = tk.Label(frame_1,text='Tecla:')
lb_tecla_text.grid(row=0,column=0)

lb_tecla = tk.Label(frame_1,textvariable=k,width=5,height=1)
lb_tecla.grid(row=0,column=1)

lb_X = tk.Label(frame_1,text='X:')
lb_X.grid(row=1,column=0)

lb_mouse_x = tk.Label(frame_1,textvariable=x,width=5,height=1)
lb_mouse_x.grid(row=1,column=1)

lb_Y = tk.Label(frame_1,text='Y:')
lb_Y.grid(row=2,column=0)

lb_mouse_x = tk.Label(frame_1,textvariable=y,width=5,height=1)
lb_mouse_x.grid(row=2,column=1)

lb_salvo_text = tk.Label(frame_1,text='control-s',width=5,height=1)
lb_salvo_text.grid(row=3,column=0)

lb_salvo = tk.Label(frame_1,textvariable=s,width=5,height=1)
lb_salvo.grid(row=3,column=1)

janela.mainloop()
