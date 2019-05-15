import Grafo
import random
import pandas as pd
import numpy as np

class Busca:

  def __init__(self, grafo, size):
    if not isinstance(grafo, Grafo.Grafo):
      raise ValueError("O grafo não é uma instância de Grafo.")
    
    self._grafo = grafo
    self._size = size
    self.limpar()
  
  def limpar(self):
    self._grafo.limpaVertices()
    self._pontuacao = int(self._size**1.5)
    self._nOuro = int(self._size/2)
    self._movimento = list()
    self._ouroEncontrado = list()
  
  def buscaProfundidade(self, v):
    if self._pontuacao == 0:
     return "Morto"

    # para nao ficar escrevendo self._grafo toda hora
    g = self._grafo

    g.marcarVertice(v)

    if self.checkOuro(v):
      self.voltarInicio()

    for adjacente in g.adjacentes(v):
      if g.vertice(adjacente).marcado:
        continue

      self.realizaMovimentoIda(v, adjacente)
      self.buscaProfundidade(adjacente)

      # Quando volta da recursao ele volta pro nodo
      self.realizaMovimentoVolta(v, adjacente)
      
  
  def voltarInicio(self):
    # Se todos os vertices estao marcados ele nao visita mais na call recursiva
    self._grafo.marcarTodosVertices()
  
  def checkOuro(self, v):
    if self._grafo.vertice(v).dados["conteudo"] == 2:
      self._pontuacao += 5 * int(self._size**1.5)
      self._nOuro -= 1
      self._ouroEncontrado.append(str(self._grafo.vertice(v).dados["row"]) + "." + str(self._grafo.vertice(v).dados["col"]))

    return self._nOuro == 0
  
  def realizaMovimentoIda(self, vFrom, vTo):
    self._pontuacao -= 1

    if self._grafo.vertice(vTo).dados["row"] > self._grafo.vertice(vFrom).dados["row"]:
      self._movimento.append("B->" + str(self._grafo.vertice(vTo).dados["row"]) + "." + str(self._grafo.vertice(vTo).dados["col"]))
    elif self._grafo.vertice(vTo).dados["row"] < self._grafo.vertice(vFrom).dados["row"]:
      self._movimento.append("C->" + str(self._grafo.vertice(vTo).dados["row"]) + "." + str(self._grafo.vertice(vTo).dados["col"]))
      # self._movimento.append("C")
    elif self._grafo.vertice(vTo).dados["col"] > self._grafo.vertice(vFrom).dados["col"]:
      self._movimento.append("D->" + str(self._grafo.vertice(vTo).dados["row"]) + "." + str(self._grafo.vertice(vTo).dados["col"]))
      # self._movimento.append("D")
    elif self._grafo.vertice(vTo).dados["col"] < self._grafo.vertice(vFrom).dados["col"]:
      self._movimento.append("E->" + str(self._grafo.vertice(vTo).dados["row"]) + "." + str(self._grafo.vertice(vTo).dados["col"]))
      # self._movimento.append("E")


  def realizaMovimentoVolta(self, vFrom, vTo):
    if self._grafo.vertice(vTo).dados["row"] > self._grafo.vertice(vFrom).dados["row"]:
      self._movimento.append("C->" + str(self._grafo.vertice(vFrom).dados["row"]) + "." + str(self._grafo.vertice(vFrom).dados["col"]))
    elif self._grafo.vertice(vTo).dados["row"] < self._grafo.vertice(vFrom).dados["row"]:
      self._movimento.append("B->" + str(self._grafo.vertice(vFrom).dados["row"]) + "." + str(self._grafo.vertice(vFrom).dados["col"]))
      # self._movimento.append("C")
    elif self._grafo.vertice(vTo).dados["col"] > self._grafo.vertice(vFrom).dados["col"]:
      self._movimento.append("E->" + str(self._grafo.vertice(vFrom).dados["row"]) + "." + str(self._grafo.vertice(vFrom).dados["col"]))
      # self._movimento.append("D")
    elif self._grafo.vertice(vTo).dados["col"] < self._grafo.vertice(vFrom).dados["col"]:
      self._movimento.append("D->" + str(self._grafo.vertice(vFrom).dados["row"]) + "." + str(self._grafo.vertice(vFrom).dados["col"]))
      # self._movimento.append("E")

    self._pontuacao -= 1


  def buscaLargura(self, start_v):
    g = self._grafo
    
    queue = list()
    queue.append(start_v)
    g.visitarVertice(start_v)

    v = start_v
    vOld = v
    while queue:
      vOld = v
      v = queue.pop(0)
      self.realizaMovimentoIda(vOld, v)
      
      if self.checkOuro(v):
        return

      for w in g.adjacentes(v):
        if not g.vertice(w).visitado:
          g.visitarVertice(w)
          queue.append(w)
          self.realizaMovimentoIda(v, w)
          self.realizaMovimentoVolta(v, w)

