import os
import shutil
import subprocess
import logging

# Configuração de logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def organizar_arquivos(pasta_origem):
    '''
    Organiza arquivos XML dentro da pasta origem, criando subpastas com base em informações do nome do arquivo.
    Não percorre subpastas, apenas processa os arquivos na pasta raiz.
    
    Args:
        pasta_origem (str): Caminho da pasta onde os arquivos estão.
    '''
    logging.info(f'Organizando arquivos na pasta: {pasta_origem}')

    for nome_arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)

        if os.path.isfile(caminho_arquivo) and (nome_arquivo.endswith('.xml') or nome_arquivo.endswith('.txt')):
            logging.debug(f'Arquivo XML encontrado: {nome_arquivo}')
            
            try:
                # Extrai o valor do antepenúltimo campo do nome do arquivo
                campos = nome_arquivo.split('-')
                ano_mes = "20" + campos[-3][:4]  # Antepenúltimo campo
            except IndexError:
                logging.warning(f'Nome de arquivo inesperado, ignorando: {nome_arquivo}')
                continue

            pasta_destino = os.path.join(pasta_origem, ano_mes)
            os.makedirs(pasta_destino, exist_ok=True)
            logging.debug(f'Pasta criada: {pasta_destino}')

            shutil.move(caminho_arquivo, os.path.join(pasta_destino, nome_arquivo))
            logging.debug(f'Arquivo movido para: {pasta_destino}')
    
    logging.info(f'Organização de arquivos concluída na pasta: {pasta_origem}')


def compactar_pasta(pasta):
    if os.path.isdir(pasta):
        rar_path = 'C:\\Program Files (x86)\\winrar\\rar.exe'  # Caminho para o executável do WinRAR
        novo_caminho = pasta.replace(pasta_raiz, "Z:/WORKNOTAS/ArquivosNFSeAssinadosBKP/", 1)
        rar_file = novo_caminho + '.rar'
        logging.info(f'Compactando pasta: {pasta} para {rar_file}')
        subprocess.run([rar_path, 'a', '-ep', '-m5', '-idq', '-ibck', rar_file, pasta])
        # shutil.rmtree(pasta)
        logging.info(f'Compactação concluída: {pasta}')


def processar_diretorios(pasta_raiz):
    """
    Processa apenas as primeiras subpastas diretamente dentro da pasta raiz
    e organiza arquivos XML, incluindo a pasta 'xmlnotas' se ela existir.
    
    Args:
        pasta_raiz (str): Caminho da pasta raiz onde estão as subpastas.
    """
    logging.info(f'Processando diretórios na raiz: {pasta_raiz}')

    for nome_diretorio in os.listdir(pasta_raiz):
        pasta_origem = os.path.join(pasta_raiz, nome_diretorio)

        if os.path.isdir(pasta_origem):
            logging.debug(f'Pasta encontrada: {pasta_origem}')
            organizar_arquivos(pasta_origem)

            # Verifica se há uma pasta chamada 'XMLNotas' e organiza os arquivos nela
            xmlnotas_path = os.path.join(pasta_origem, 'XMLNotas')
            if os.path.isdir(xmlnotas_path):
                logging.debug(f'Pasta "XMLNotas" encontrada: {xmlnotas_path}')
                organizar_arquivos(xmlnotas_path)

            # (Opcional) Listar subpastas diretas na pasta_origem
            pastas = [
                os.path.join(pasta_origem, d)
                for d in os.listdir(pasta_origem)
                if os.path.isdir(os.path.join(pasta_origem, d))
            ]

            # Descomente a lógica abaixo, se precisar compactar as pastas
            '''
            for pasta in pastas:
                compactar_pasta(pasta)
            '''


# Caminho para a pasta raiz
pasta_raiz = 'D:/Prefeituras/ArquivosNFSeAssinados/'
#pasta_raiz = 'G:\\Backup\\worknotas\\'
processar_diretorios(pasta_raiz)
logging.info('Processamento completo.')
