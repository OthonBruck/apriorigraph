import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

dados = pd.read_csv('anxiety.csv', header = None)
transacoes = []
for i in range(0, dados.shape[0]):
  transacoes.append([str(dados.values[i,j]) for j in range(0, dados.shape[1])])

# Suporte = Número de transações de um item X / total de numero de transações

# Confidence = Número de transações contendo item X e Y / Numero de transações contendo X

# Lift = Confidence / Suporte

regras = apriori(transactions = transacoes, min_support = 0.003, min_confidence = 0.2, min_lift = 1.5, min_length = 2, max_length = 2)
results = list(regras)

def inspecionar(results):   
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    suporte    = [result[1] for result in results]
    confianca = [result[2][0][2] for result in results]   
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, suporte, confianca, lifts))
resultadoDataFrame = pd.DataFrame(inspecionar(results), columns = ['Sintoma presente', 'Sintoma que pode ocorrer/desenvolver', 'Suporte', 'Confiança', 'Lift'])

print(results)

# writer = pd.ExcelWriter("ansiedade.xlsx", engine="xlsxwriter")

# resultsinDataFrame.to_excel(writer, sheet_name="Sheet3", startrow=0, header=resultsinDataFrame.columns, index=False)
# writer.close()

print(resultadoDataFrame.nlargest(n=10, columns="Lift"))
