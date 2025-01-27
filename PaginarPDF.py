import argparse
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def add_page_numbers_with_total(input_pdf, output_pdf):
    # Carrega o PDF original
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Número total de páginas
    total_pages = len(reader.pages)

    # Loop para cada página do PDF
    for page_num in range(total_pages):
        # Cria uma página em branco com numeração no formato "1/9"
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Escreve o número da página atual e o total de páginas
        page_text = f"Página {page_num + 1} de {total_pages}"
        
        # Calcula a largura da página e centraliza o texto
        text_width = can.stringWidth(page_text, "Helvetica", 12)  # Largura do texto
        page_width = letter[0]  # Largura da página
        x_position = (page_width - text_width) / 2  # Centraliza horizontalmente
        y_position = 10  # Posição vertical (mude conforme necessário)
        can.drawString(x_position, y_position, page_text)
        can.save()

        # Move para o início do buffer e cria uma nova página no PDF
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page = reader.pages[page_num]

        # Mescla a numeração com a página original
        page.merge_page(new_pdf.pages[0])
        writer.add_page(page)

    # Salva o PDF final com numeração de páginas
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# Configuração de entrada de argumentos
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paginar um arquivo PDF com número total de páginas")
    parser.add_argument("input_pdf", help="Caminho completo do arquivo PDF de entrada")
    parser.add_argument("output_pdf", help="Caminho completo do arquivo PDF de saída")
    args = parser.parse_args()
    
    add_page_numbers_with_total(args.input_pdf, args.output_pdf)
