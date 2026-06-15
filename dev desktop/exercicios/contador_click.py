import tkinter as tk

janela = tk.Tk()
janela.title('Contador de Clicks')
janela.geometry('500x400')
janela.iconbitmap('dark-triangle.ico')

cont = tk.IntVar()
cont.set(0)


def click():
    cont.set(cont.get()+1) 

def zerar():
    cont.set(0)


lb_contador = tk.Label(janela, textvariable=cont)
lb_contador.place(relx=0.5,rely=0.4)

bt_click = tk.Button(janela, text='click', command=click)
bt_click.place(relx=0.4,rely=0.5)

bt_click = tk.Button(janela, text='zerar', command=zerar)
bt_click.place(relx=0.5,rely=0.5)

janela.mainloop()
