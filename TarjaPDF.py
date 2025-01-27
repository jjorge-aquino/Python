import argparse
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import red, white
import io

def add_diagonal_stamp(input_pdf, output_pdf, stamp_text):
    # Carrega o PDF original
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Loop para cada página do PDF
    for page_num in range(len(reader.pages)):
        # Cria um overlay com a tarja diagonal
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Define o tamanho da página
        page_width, page_height = letter

        # Rotaciona a canvas em 45 graus para posicionar a tarja na diagonal
        can.saveState()
        can.translate(page_width / 2, page_height / 2)
        can.rotate(45)  # Rotaciona 45 graus

        # Define a opacidade do fundo e cria o retângulo branco com borda e texto semi-transparentes
        can.setStrokeColor(red, alpha=0.3)  # Borda vermelha com 30% de opacidade
        can.setFillColor(red, alpha=0.3)  # Fundo branco com 30% de opacidade
        rect_width = page_width * 1.2  # Largura ajustada para evitar excesso nas bordas
        rect_height = 80  # Altura do retângulo ajustada
        can.rect(-rect_width / 2, -rect_height / 2, rect_width, rect_height, fill=True, stroke=True)

        # Adiciona o texto centralizado dentro do retângulo com transparência
        can.setFillColor(red, alpha=0.3)  # Texto em vermelho com 30% de opacidade
        can.setFont("Helvetica-Bold", 24)
        text_width = can.stringWidth(stamp_text, "Helvetica-Bold", 24)
        can.drawString(-text_width / 2, -10, stamp_text)  # Ajuste vertical para centralizar o texto

        can.restoreState()  # Restaura o estado da canvas após a rotação
        can.save()

        # Move para o início do buffer e cria uma nova página no PDF
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page = reader.pages[page_num]

        # Mescla a tarja com a página original
        page.merge_page(new_pdf.pages[0])
        writer.add_page(page)

    # Salva o PDF final com a tarja
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# Configuração de entrada de argumentos
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adicionar uma tarja diagonal com texto personalizado em um PDF")
    parser.add_argument("input_pdf", help="Caminho completo do arquivo PDF de entrada")
    parser.add_argument("output_pdf", help="Caminho completo do arquivo PDF de saída")
    parser.add_argument("stamp_text", help="Texto para a tarja (ex: 'Confidencial', 'Restrito')")
    args = parser.parse_args()
    
    add_diagonal_stamp(args.input_pdf, args.output_pdf, args.stamp_text)
