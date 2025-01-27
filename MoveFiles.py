import os
import shutil
import concurrent.futures
import subprocess

#pasta_origem = 'Z:/WORKNOTAS/ArquivosNFSeAssinadosBKP/CAB2'
#pasta_origem = r'\\bulls0011-vlan1351.fs.locaweb.com.br\TNUS$\WORKNOTAS\ArquivosNFSeAssinadosBKP\CAB'
pasta_origem = r'D:\Siat\xml'
#rar_path = 'C:\\Program Files (x86)\\winrar\\rar.exe'  # Caminho para o executável do WinRAR
rar_path = 'C:\\Program Files\\winrar\\rar.exe'

for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.endswith('.xml'):
        ano_mes = "20"+nome_arquivo.split('-')[4][:4]
        pasta_destino = os.path.join(pasta_origem, ano_mes)

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        shutil.move(os.path.join(pasta_origem, nome_arquivo), pasta_destino)

def compactar_pasta(pasta):
    if os.path.isdir(pasta):
        rar_file = pasta + '.rar'
        subprocess.run([rar_path, 'a', '-ep', '-m5', '-idq', '-ibck', rar_file, pasta])
        shutil.rmtree(pasta)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    pastas = [os.path.join(pasta_origem, d) for d in os.listdir(pasta_origem)]
    executor.map(compactar_pasta, pastas)