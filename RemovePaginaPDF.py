import PyPDF2

def remove_pages(input_pdf, output_pdf, pages_to_remove):
    """
    Remove páginas específicas de um PDF.

    :param input_pdf: Caminho do PDF de entrada.
    :param output_pdf: Caminho do PDF de saída.
    :param pages_to_remove: Lista de números das páginas a serem removidas (base 1).
    """
    try:
        # Abrir o arquivo PDF de entrada
        with open(input_pdf, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)
            writer = PyPDF2.PdfWriter()

            # Adicionar páginas que não estão na lista de remoção
            for i, page in enumerate(reader.pages, start=1):
                if i not in pages_to_remove:
                    writer.add_page(page)

            # Escrever o novo PDF
            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)

        print(f"As páginas {pages_to_remove} foram removidas com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Configuração de exemplo
input_pdf_path = r"C:\Users\station007\Desktop\Lucena - IPTU 2025 - PIX Todas Parcelas - Fora do Município 2.1.pdf"
output_pdf_path = r"C:\Users\station007\Desktop\Lucena - IPTU 2025 - PIX Todas Parcelas - Fora do Município 2_modificado.pdf"
pages_to_remove = [1, 2]  # Páginas a serem removidas (base 1)

remove_pages(input_pdf_path, output_pdf_path, pages_to_remove)
