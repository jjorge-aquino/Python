import pandas as pd
import chardet

pathcsv=r'C:\Users\estacao007\Desktop\JJERRO.txt'

'''with open(pathcsv, 'r') as file, open(pathcsv+'example_fixed.txt', 'w') as outfile:
    for line in file:
        outfile.write(line.replace('\r\n', '\n'))
'''
def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

data = pd.read_csv(pathcsv, delimiter="#",encoding='ISO-8859-1')
print(data)
