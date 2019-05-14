import Grafo
import random
import pandas as pd
import numpy as np
from copy import deepcopy, copy

# Criando o grafo e arestas
file = pd.read_csv("entrada.txt", skiprows=1, delimiter='\t', header=None).applymap(str)

# matrixSize = int(file.readline(1).strip())

# print(file)


matrix = np.array(file)

# Cantos = (0,0), (0,n), (n,0), (n,n)
# Laterais = (col > 0 && col < n && (row == 0 || row == n)) || 
# (row > 0 && row < n && (col == 0 || col == n))

print(matrix)
print("\n\n")

# 0 = livre
# 1 = parede
# 2 = ouro
value = 0

def checkValue(row, col):
  if row >= matrix.shape[0] or row < 0:
    return False
  elif col >= matrix.shape[1] or col < 0:
    return False
  
  val = matrix[row][col]
  if val == "0":
    return True
  elif val == "1":
    return False
  else:
    return True

vertices = []
arestas = []
for row in range(matrix.shape[0]):
  for col in range(matrix.shape[1]):
    arestas = [] 
    if matrix[row][col] == "0":
      value = 0
    elif matrix[row][col] == "1":
      # Se for parede nem adiciona vertice
      value = 1
      continue
    else:
      value = 2

    if checkValue(row, col-1):
      arestas.append(str(row) + "." + str(col-1))
    if checkValue(row, col+1):
      arestas.append(str(row) + "." + str(col+1))
    if checkValue(row-1, col):
      arestas.append(str(row-1) + "." + str(col))
    if checkValue(row+1, col):
      arestas.append(str(row+1) + "." + str(col))

    vertices.append(
      Grafo.Vertice(str(row) + "." + str(col), arestas,
      {"conteudo":value}))

grafo = Grafo.Grafo(vertices)

print(grafo.adjacentes("6.5"))