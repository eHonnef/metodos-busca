import Grafo
import random
import pandas as pd
from copy import deepcopy, copy

# Criando o grafo e arestas
file = pd.read_csv("entrada.txt", skiprows=1, delimiter='\t', header=None)

# matrixSize = int(file.readline(1).strip())

print(file)

"""
for row in range(matrixSize):
  for col in range(matrixSize):
    if row > 0:
      print(row)
"""