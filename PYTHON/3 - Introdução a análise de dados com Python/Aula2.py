import pandas as pd

# TRANSFORMANDO LISTA EM UMA SERIE
lista = [10, 20, 30, 40, 50]
series1 = pd.Series(data = lista)
print(series1)

# TRANSFORMANDO DICIONÁRIO EM SERIES
dici = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
series2 = pd.Series(data = dici)
print(series2)

# MÉTODOS PRONTOS SERIES
# MEDIA
print("MEDIA: \n")
media1 = series1.mean()
print(media1)
media2 = series2.mean()
print(media2)
print("SOMA: \n")
sum1 = series1.sum()
print(sum1)
sum2 = series2.sum()
print(sum2)
# MÁXIMO
print("MÁXIMO: \n")
max1 = series1.max()
print(max1)
max2 = series2.max()
print(max2)
# MÍNIMO
print("MÍNIMO: \n")
min1 = series1.min()
print(min1)
min2 = series2.min()
print(min2)

# CAMINHO DO ARQUIVO A SER ARMAZENADO
caminho_arquivo = r'C:\Users\chadt\Downloads\202601_NFe\202601_NFe_NotaFiscal.csv'
# LEITURA DO ARQUIVO CSV
df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1')
# IMPRIMINDO 10 PRIMEIRAS LINHAS ARQUIVO CSV
print(df.head(20))
# CONVERSÃO
df['VALOR_NF'] = (
    df['VALOR NOTA FISCAL']
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)
# IMPRIMINDO A MEDIA DOS VALORES DAS NOTAS FISCAIS 
media_nfs = df['VALOR_NF'].mean()
print(f"\nVALOR MÉDIO DAS NOTAS FISCAIS: R$ {media_nfs:,.2f}")