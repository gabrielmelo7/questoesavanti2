import pandas as pd
data = pd.read_csv("C:/Users/gabme/OneDrive/Documentos/teste.csv")
c = int(input("Quantas linhas deseja ler?\n"))
print(data.head(c)) 