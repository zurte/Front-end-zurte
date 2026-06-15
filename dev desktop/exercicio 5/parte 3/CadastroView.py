import tkinter as tk
from tkinter import messagebox
import CadastroController as ct

def criar_view():
    win = tk.Tk()
    win.title('Cadastro de Equipamentos')
    win.geometry('500x400')

    porct_x = 0.2

    tipo_equip = tk.StringVar()
    setor = tk.StringVar()
    status = tk.StringVar()

    tipo_equip.set('escolha o tipo de equipamento')
    setor.set('escolha o setor')
    status.set('escolha o status do cadastro')

    ls_equip = ['DeskTop','NoteBook','Impressora','Celular']
    ls_setor = ['Laboratorio de T.i','Administrativo','Financeiro']
    ls_status = ['recebido','esperando peça','em andamento','concluido']

    def click_salvar():
        ptrm = ent_ptrm.get().strip()
        tipo_equipamento = tipo_equip.get()
        p_setor = setor.get()
        p_status = status.get()

        mensagem,resultado = ct.salvar_dados(ptrm,tipo_equipamento,p_setor,p_status)

        if resultado:
            tk.messagebox.showinfo('Sucesso','Dados salvos com sucesso')

        else:
            tk.messagebox.showwarning('ATENÇÃO',mensagem)
    
    #frame
    frm_1 = tk.Frame(win)
    frm_1.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

    #Label
    lb_ptrm = tk.Label(frm_1,text='Patrimonio')
    lb_ptrm.place(relx=porct_x,rely=0.1)

    lb_tipo_equip = tk.Label(frm_1,text='Tipo de Equipamento')
    lb_tipo_equip.place(relx=porct_x,rely=0.3)

    lb_setor = tk.Label(frm_1,text='Setor')
    lb_setor.place(relx=porct_x,rely=0.5)

    lb_status = tk.Label(frm_1,text='Status')
    lb_status.place(relx=porct_x,rely=0.7)

    #Entry
    ent_ptrm = tk.Entry(frm_1,width=30)
    ent_ptrm.place(relx=(porct_x+0.2),rely=0.1)

    #OptionMenu
    opm_tipo_equip = tk.OptionMenu(frm_1,tipo_equip,*ls_equip)
    opm_tipo_equip.place(relx=(porct_x+0.3),rely=0.3)

    opm_setor = tk.OptionMenu(frm_1,setor,*ls_setor)
    opm_setor.place(relx=(porct_x+0.2),rely=0.5)

    opm_status = tk.OptionMenu(frm_1,status,*ls_status)
    opm_status.place(relx=(porct_x+0.2),rely=0.7)

    #Botões
    bt_salvar = tk.Button(frm_1,text='Salvar',command =click_salvar)
    bt_salvar.place(relx=porct_x,rely=0.9)
    
    win.mainloop()

if __name__ == '__main__':
    criar_view()
    
