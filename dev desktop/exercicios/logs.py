import tkinter as tk

from tkinter import messagebox,filedialog

win = tk.Tk()
win.title('Arquivo de log')
win.geometry('384x216')

caminho = tk.StringVar()

def selecionar_caminho():

    caminho.set(tk.filedialog.askopenfilename(title='escolha um arquivo'))

    if caminho.get() == '':
        tk.messagebox.showinfo('Calcelado','Operação cancelada')
        print('cancelou')

def limpar():
    limpar = tk.messagebox.askyesno('Limpar campos','Deseja limpar campo de caminho?')

    if limpar:
        caminho.set('')



spc_y = 5
spc_x = 5

frm_1 = tk.Frame(win)
frm_1.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

lb_cmn = tk.Label(frm_1,textvariable=caminho)
lb_cmn.grid(row=0,column=0, padx=spc_x, pady=spc_y)

bt_arquivo = tk.Button(frm_1,text='selecionar pasta/arquivo',command=selecionar_caminho)
bt_arquivo.grid(row=0,column=1)

bt_limpar = tk.Button(frm_1,text='limpar caminho',command=limpar)
bt_limpar.grid(row=1,column=0)

win.mainloop()
