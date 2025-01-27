import pandas as pd

# Suponha que 'df' é o seu DataFrame
df = pd.read_csv(r'C:\Users\station007\Desktop\SISOBRA_IMPLANTADO.CSV', delimiter=';')

# Use a função pivot
pivot_df = df.pivot(columns='SISOBRA', values='NAMESPACE')

# Substitua os valores NaN por uma string vazia
pivot_df = pivot_df.fillna('')

# Salve o DataFrame pivotado como um novo arquivo CSV
pivot_df.to_csv(r'C:\Users\station007\Desktop\novo_arquivo.csv', index=False, sep=';')



