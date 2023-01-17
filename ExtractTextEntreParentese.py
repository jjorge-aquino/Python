import re

# abrindo o arquivo de entrada para leitura
with open('input.txt', 'r') as input_file:
    text = input_file.read()

# usando expressões regulares para encontrar o texto entre parênteses
#matches = re.findall(r'\(([^)]+)\)', text)

# usando expressões regulares para encontrar o texto entre parênteses sem duplicatas
matches = list(set(re.findall(r'\(([^)]+)\)', text)))

# abrindo o arquivo de saída para escrita
with open('output.txt', 'w') as output_file:
    # escrevendo cada ocorrência encontrada no arquivo de saída
    for match in matches:
        output_file.write(match + '\n')