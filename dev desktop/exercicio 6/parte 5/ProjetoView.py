import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ProjetoController as ct
import ProjetoModel as model

spc_y = 2

def salvar():
    p_patr = ent_patr.get().strip()
    p_equip = combo_equip.get().strip()
    p_def = ent_def.get().strip()
    p_cep = ent_cep.get()

    valido = ct.validar(p_patr,p_equip,p_def,p_cep)
    
    if valido['error']:
        tk.messagebox.showerror('Error',valido['mensagem'])
        
    else:
        patrimonio_final = int(p_patr.strip())
        
        endereco = valido['dados_endereco']
        
        lb_logradouro.config(text=f"Rua: {endereco.get('logradouro', '')}")
        lb_bairro.config(text=f"Bairro: {endereco.get('bairro', '')}")
        lb_cidade.config(text=f"Cidade: {endereco.get('localidade', '')}")
        lb_estado.config(text=f"Estado: {endereco.get('uf', '')}")
        if tk.messagebox.askyesno('Confirmação','Esse endereço está certo?'):
            model.criar_tabela(p_patr,p_equip,p_def,p_cep)
            
        else:
            lb_logradouro.config(text="Rua: ")
            lb_bairro.config(text="Bairro: ")
            lb_cidade.config(text="Cidade: ")
            lb_estado.config(text="Estado: ")

def criar_arquivo_csv():
    ct.criar_csv()

def criar_arquivo_json():
    ct.criar_json()
    
win = tk.Tk()
win.title('Integração com API')
win.geometry('600x400')
#frame
frm = tk.Frame(win,bg='darkblue')
frm.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=1.0)

#patrimonio
lb_patr = tk.Label(frm,text='Patrimônio')
lb_patr.pack(pady=spc_y)

ent_patr = tk.Entry(frm)
ent_patr.pack(pady=spc_y)

#equipamento
lb_equip = tk.Label(frm,text='Equipamento')
lb_equip.pack(pady=spc_y)

combo_equip = ttk.Combobox(frm,values=('desktop','notebook','impressora','celular'))
combo_equip.pack(pady=spc_y)

#defeito
lb_def = tk.Label(frm,text='Descrição')
lb_def.pack(pady=spc_y)

ent_def = tk.Entry(frm)
ent_def.pack(pady=spc_y)

#cep
lb_cep = tk.Label(frm,text='CEP')
lb_cep.pack(pady=spc_y)

ent_cep = tk.Entry(frm)
ent_cep.pack(pady=spc_y)

#labels de informação
lb_logradouro = tk.Label(frm,text='Rua: ')
lb_logradouro.pack(pady=spc_y)

lb_bairro = tk.Label(frm,text='Bairro: ')
lb_bairro.pack(pady=spc_y)

lb_cidade = tk.Label(frm,text='Cidade: ')
lb_cidade.pack(pady=spc_y)

lb_estado = tk.Label(frm,text='Estado: : ')
lb_estado.pack(pady=spc_y)

#botões
bt_salvar = tk.Button(frm,text='Salvar',command=salvar)
bt_salvar.pack(pady=spc_y)

bt_csv = tk.Button(frm,text='Criar arquivo csv',command=criar_arquivo_csv)
bt_csv.pack(pady=spc_y)

bt_json = tk.Button(frm,text='Criar arquivo json',command=criar_arquivo_json)
bt_json.pack(pady=spc_y)

win.mainloop()
