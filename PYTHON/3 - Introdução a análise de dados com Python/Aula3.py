import pandas as pd
import matplotlib.pyplot as plt

# EXTRAÇÃO DB de Candidatos a cargos federais dos Estados Unidos registrados na Federal Election Commission
caminho_arquivo = r"C:\Users\chadt\OneDrive\Desktop\us_fec_campaign_finance_candidate.csv"

# LEITURA CAMINHO
df = pd.read_csv(caminho_arquivo)

# VISUALIZAÇÃO DE DADOS

# ESTRUTURA
print(df.info())

# EXIBINDO
print(df.head())

# RENOMEANDO COLUNA ESPECÍFICA
df.columns.values[2] = "Candidate"
print(df.head())

# CRIAR NOVA COLUNA (teste futuro)
#df["ColunaNova"]

# LOCALIZANDO ÍNDICE (necessário correção?)
print("Indíce 2:", df.loc[2], "Candidate")
