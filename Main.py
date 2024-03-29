from Grafo import Grafo, Vertice, Aresta
import random
import pandas as pd
import numpy as np
from copy import deepcopy, copy
from Busca import Busca

# Criando o grafo e arestas
file = pd.read_csv(
    "entrada8.txt", skiprows=1, delimiter='\t', header=None).applymap(str)

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
# Salva os nodos que contem o ouro para a heuristica
ouro = list()


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
    if str(row) + "." + str(col) not in ouro:
      ouro.append(str(row) + "." + str(col))
    value = 2

  if not grafo.verticeExiste(str(row) + "." + str(col)):
    v = Vertice(
        str(row) + "." + str(col), {
            "conteudo": value,
            "row": row,
            "col": col,
            "linhaReta": dict()
        })
    grafo.adicionaVertice(v)
    return v
  else:
    return grafo.vertice(str(row) + "." + str(col))


for row in range(matrix.shape[0]):
  for col in range(matrix.shape[1]):
    v = adicionaVertice(row, col)
    if v == None:
      continue

    if checkValue(row, col - 1):
      if not grafo.verticeExiste(str(row) + "." + str(col - 1)):
        adicionaVertice(row, col - 1)
      ar = grafo.conecta(v.nome, str(row) + "." + str(col - 1))
      ar.setPeso(1)
    if checkValue(row, col + 1):
      if not grafo.verticeExiste(str(row) + "." + str(col + 1)):
        adicionaVertice(row, col + 1)
      ar = grafo.conecta(v.nome, str(row) + "." + str(col + 1))
      ar.setPeso(1)
    if checkValue(row - 1, col):
      if not grafo.verticeExiste(str(row - 1) + "." + str(col)):
        adicionaVertice(row - 1, col)
      ar = grafo.conecta(v.nome, str(row - 1) + "." + str(col))
      ar.setPeso(1)
    if checkValue(row + 1, col):
      if not grafo.verticeExiste(str(row + 1) + "." + str(col)):
        adicionaVertice(row + 1, col)
      ar = grafo.conecta(v.nome, str(row + 1) + "." + str(col))
      ar.setPeso(1)


def busca(busca, metodo):
  grafo.salvarGrafo()
  metodo("0.0")
  print(busca._movimento)
  print("Ouro encontrado:")
  print(busca._ouroEncontrado)
  print("Pontuacao:")
  print(busca._pontuacao)
  print("Numero de movimentos:")
  print(len(busca._movimento))
  grafo.restaurarGrafo()
  busca.limpar()
  busca.manh(ouro)


print("Ouro:")
print(ouro)
print("\n\n")
b = Busca(grafo, matrix.shape[0])
b.manh(ouro)
print("A*:")
busca(b, b.Astar)
print("\n\nBest-First:")
busca(b, b.bestFirst)
print("\n\nDFS:")
busca(b, b.BuscaProfundidade)
print("\n\nBFS:")
busca(b, b.buscaLargura)

