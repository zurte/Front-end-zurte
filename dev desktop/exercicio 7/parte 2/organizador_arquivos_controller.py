from pathlib import Path
import shutil

def organizar_arquivos(pasta):

    pasta_baguncada = pasta

    for item in pasta_baguncada.iterdir():
        
        if item.is_file():

            extensao = item.suffix().upper().replace('.','')

            nova_pasta = f'{extensao}_arquivos'if extensao else 'NÂO TEM EXTENSÂO'

            destino = pasta_baguncada/nova_pasta

            destino.mkdir(parents=True,exist_ok=True)

            shutil.move(str(item),str(destino,item.name))

            print('foi')
