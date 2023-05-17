"""import PyPDF2

# Abrir os arquivos PDF
arquivo1 = open('ficha.pdf', 'rb')
arquivo2 = open('extrato.pdf', 'rb')

# Criar objetos PDF para os arquivos
pdf1 = PyPDF2.PdfReader(arquivo1)
pdf2 = PyPDF2.PdfReader(arquivo2)

# Criar um novo arquivo PDF para a saída
saida = PyPDF2.PdfWriter()

# Adicionar as páginas do primeiro arquivo
for pagina in range(len(pdf1.pages)):
    saida.add_page(pdf1.pages[pagina])

# Adicionar as páginas do segundo arquivo
for pagina in range(len(pdf2.pages)):
    saida.add_page(pdf2.pages[pagina])

# Salvar o arquivo de saída
arquivo_saida = open('arquivo_saida.pdf', 'wb')
saida.write(arquivo_saida)

# Fechar os arquivos
arquivo1.close()
arquivo2.close()
arquivo_saida.close()"""
import sys
import PyPDF2

def merge_pdfs(file1, file2, output_file):
    # Abrir os arquivos PDF
    arquivo1 = open(file1, 'rb')
    arquivo2 = open(file2, 'rb')

    # Criar objetos PDF para os arquivos
    pdf1 = PyPDF2.PdfReader(arquivo1)
    pdf2 = PyPDF2.PdfReader(arquivo2)

    # Criar um novo arquivo PDF para a saída
    saida = PyPDF2.PdfWriter()

    # Adicionar as páginas do primeiro arquivo
    for pagina in range(len(pdf1.pages)):
        saida.add_page(pdf1.pages[pagina])

    # Adicionar as páginas do segundo arquivo
    for pagina in range(len(pdf2.pages)):
        saida.add_page(pdf2.pages[pagina])

    # Salvar o arquivo de saída
    arquivo_saida = open(output_file, 'wb')
    saida.write(arquivo_saida)

    # Fechar os arquivos
    arquivo1.close()
    arquivo2.close()
    arquivo_saida.close()

# Receber os nomes dos arquivos PDF como argumentos de linha de comando
if len(sys.argv) == 4:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]

    merge_pdfs(file1, file2, output_file)
else:
    print("Por favor, forneça os nomes dos arquivos PDF de entrada e o nome do arquivo de saída.")
    print("Exemplo de uso: python merge_pdfs.py arquivo1.pdf arquivo2.pdf arquivo_saida.pdf")
