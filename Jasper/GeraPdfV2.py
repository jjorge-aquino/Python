import os
from platform import python_version
from pyreportjasper import PyReportJasper

def advanced_example_using_database():
   REPORTS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'reports')
   input_file = os.path.join(REPORTS_DIR, 'hello_world.jrxml')
   output_file = os.path.join(REPORTS_DIR, 'hello_world')
   print(input_file)
   # Define a conexão com InterSystems Cache
   connection_string = 'jdbc:Cache://localhost:57772/namespace'
   '''conn = {
     'driver': 'postgres',
     'username': 'DB_USERNAME',
     'password': 'DB_PASSWORD',
     'host': 'DB_HOST',
     'database': 'DB_DATABASE',
     'schema': 'DB_SCHEMA',
     'port': '5432'
     'jdbc_dir': 'lib/cachejdbc.jar'
   }'''
   pyreportjasper = PyReportJasper()
   pyreportjasper.config(
     input_file,
     output_file,
     connection_string=connection_string,
     output_formats=["pdf", "rtf"],
     parameters={'python_version': python_version()},
     locale='en_US'
   )
   pyreportjasper.process_report()