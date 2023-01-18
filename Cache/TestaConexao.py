import jaydebeapi
from jpype import *
import os

# Adiciona o driver JDBC ao classpath
jarfile="C:/InterSystems/Cache16/dev/java/lib/JDK17/cachejdbc.jar"
os.environ['CLASSPATH'] = jarfile
# Configura a conexão
jdbc_url = "jdbc:Cache://www2.tinus.com.br:1972/CABO"
jdbc_driver = "com.intersys.jdbc.CacheDriver"
username = "jorge"
password = "canario123"

# Estabelece a conexão
try:
    conn = jaydebeapi.connect(jdbc_driver,jdbc_url,[username, password],jarfile)
    print("Conexão estabelecida com sucesso!")
    # Fecha a conexão
    conn.close()
except Exception as e:
    print("Falha ao estabelecer conexão: ", e)