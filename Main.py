from Grafo import Grafo, Vertice, Aresta
import random
import pandas as pd
import numpy as np
from copy import deepcopy, copy
import Busca

# Criando o grafo e arestas
file = pd.read_csv("entrada.txt", skiprows=1, delimiter='\t', header=None).applymap(str)

# matrixSize = int(file.readline(1).strip())

# print(file)


matrix = np.array(file)
print(matrix)
print("\n\n")


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


grafo = Grafo()

def adicionaVertice(row, col):
  # 0 = livre
  # 1 = parede
  # 2 = ouro
  value = 0

  if matrix[row][col] == "0":
    value = 0
  elif matrix[row][col] == "1":
    # Se for parede nem adiciona vertice
    value = 1
    return None
  else:
    value = 2
  
  if not grafo.verticeExiste(str(row) + "." + str(col)):
    v = Vertice(str(row) + "." + str(col), {"conteudo":value, "row":row, "col":col})
    grafo.adicionaVertice(v)
    return v
  else:
    return grafo.vertice(str(row) + "." + str(col))
  

for row in range(matrix.shape[0]):
  for col in range(matrix.shape[1]):
    v = adicionaVertice(row, col)
    if v == None:
      continue

    if checkValue(row, col-1):
      if not grafo.verticeExiste(str(row) + "." + str(col-1)):
        adicionaVertice(row, col-1)
      grafo.conecta(v.nome, str(row) + "." + str(col-1))
    if checkValue(row, col+1):
      if not grafo.verticeExiste(str(row) + "." + str(col+1)):
        adicionaVertice(row, col+1)
      grafo.conecta(v.nome, str(row) + "." + str(col+1))
    if checkValue(row-1, col):
      if not grafo.verticeExiste(str(row-1) + "." + str(col)):
        adicionaVertice(row-1, col)
      grafo.conecta(v.nome, str(row-1) + "." + str(col))
    if checkValue(row+1, col):
      if not grafo.verticeExiste(str(row+1) + "." + str(col)):
        adicionaVertice(row+1, col)
      grafo.conecta(v.nome, str(row+1) + "." + str(col))


# for v in grafo.grafo:
#   print(v)
#   print(grafo.adjacentes(v))

grafo.arvore()

for v in grafo.grafo:
  print(v)
  print(grafo.adjacentes(v))


# b = Busca.Busca(grafo, matrix.shape[0])
# # b.buscaProfundidade("0.0")
# b.buscaLargura("0.0")

# print(b._movimento)
# print(b._ouroEncontrado)
# print(b._pontuacao)
# print(len(b._movimento))

# b.limparGrafo()