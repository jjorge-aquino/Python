import os
import PyPDF2
from unidecode import unidecode

def divide_pdf(input_pdf_path, output_folder, pages_per_file=500):
    # Extrai o nome do arquivo sem a extensão
    input_filename = os.path.splitext(os.path.basename(input_pdf_path))[0]

    # Converte caracteres acentuados para não acentuados
    input_filename = unidecode(input_filename)

    # Cria o diretório de saída se não existir
    os.makedirs(output_folder, exist_ok=True)

    with open(input_pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)

        # Contador para os arquivos de saída
        contador = 1

        for start_page in range(0, total_pages, pages_per_file):
            end_page = min(start_page + pages_per_file, total_pages)

            pdf_writer = PyPDF2.PdfWriter()
            for page_num in range(start_page, end_page):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            output_file_path = f"{output_folder}/{input_filename}_{contador}.pdf"
            with open(output_file_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"Arquivo {output_file_path} criado com sucesso!")
            
            contador += 1
def processar_pasta_input(input_folder, output_folder, pages_per_file=500):
    # Cria o diretório de saída se não existir
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(input_folder, filename)
            divide_pdf(input_pdf_path, output_folder, pages_per_file)

if __name__ == "__main__":
    input_pdf_path = f"D:/Siat/Cabedelo__IPTU_2024__Carnes_Definitivos_20240110183021"
    output_folder = f"D:/Siat/Cabedelo__IPTU_2024__Carnes_Definitivos_20240110183021_output"
    pages_per_file = 2600

    processar_pasta_input(input_pdf_path, output_folder, pages_per_file)
