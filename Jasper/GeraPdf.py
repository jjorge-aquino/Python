import os
#from PyReportJasper import JasperPy
from pyreportjasper import PyReportJasper
# Cria uma instância de JasperPy
jasper = JasperPy()

# Define o caminho para o arquivo Jasper
jasper_file = 'caminho/para/arquivo.jasper'

# Define os parâmetros do relatório (se houver)
params = {'parametro1': 'valor1', 'parametro2': 'valor2'}

# Define a conexão com InterSystems Cache
connection = {
    'driver': 'intersystems',
    'host': 'hostname',
    'port': 'port',
    'username': 'username',
    'password': 'password',
    'namespace': 'namespace',
}

# Gera o relatório
output = jasper.process(jasper_file, output_file='output.pdf', format_list=["pdf"], parameters=params, db_connection=connection)

# Exibe o relatório gerado
print(output)
