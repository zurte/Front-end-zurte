import tkinter as tk
import arquivosController as ct

spc_y = 20

win=tk.Tk()
win.title('Salvando arquivos')
win.geometry('600x400')

frm = tk.Frame(win,bg='cyan')
frm.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

bt_txt = tk.Button(frm,text='gerar txt',command=ct.criar_txt).pack(pady=spc_y)
bt_csv = tk.Button(frm,text='gerar csv',command=ct.criar_csv).pack(pady=spc_y)
bt_json = tk.Button(frm,text='gerar json',command=ct.criar_json).pack(pady=spc_y)
bt_ler_csv = tk.Button(frm,text='ler csv',command=ct.ler_csv).pack(pady=spc_y)

win.mainloop()
