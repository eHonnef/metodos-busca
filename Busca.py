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

  def voltarInicio(self):
    # Se todos os vertices estao marcados ele nao visita mais na call recursiva
    self._grafo.marcarTodosVertices()
  
  def checkOuro(self, v):
    if self._grafo.vertice(v).dados["conteudo"] == 2:
      self._pontuacao += 5 * int(self._size**1.5)
      self._nOuro -= 1
      self._ouroEncontrado.append(v)
      self._movimento.append("PO->" + v)

      for w in self._grafo.nomeVertices():
        if v in self._grafo.vertice(w).dados["linhaReta"]:
          del self._grafo.vertice(w).dados["linhaReta"][v]

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

  def BuscaProfundidade(self, v):
    self._buscaProfundidade(v)
    self._grafo.limpaVertices()

  def buscaProfundidade(self, limite):
    self._buscaProfundidade("0.0", limite = limite)
    self._grafo.limpaVertices()
  
  # -1 significa que é sem limite
  def _buscaProfundidade(self, v, limite = -1, d = 1):
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

      if limite == -1 or d <= limite:
        d += 1
        self.realizaMovimentoIda(v, adjacente)
        self._buscaProfundidade(adjacente, limite, d)
        d -= 1

        # Quando volta da recursao ele volta pro nodo
        self.realizaMovimentoVolta(v, adjacente)

  def buscaLargura(self, start_v):
    g = self._grafo
    
    queue = list()
    queue.append(start_v)
    g.visitarVertice(start_v)

    v = start_v
    vOld = v

    g.vertice(start_v).visitado = True
    while queue:
      if self._pontuacao == 0:
        return "Morto"

      vOld = v
      v = queue.pop(0)
      self.realizaMovimentoIda(vOld, v)
      
      if self.checkOuro(v):
        s = g.shortestPath(v, "0.0")
        a = v
        for u in s:
          self.realizaMovimentoVolta(u, a)
          a = u
        return

      for w in g.adjacentes(v):
        if not g.vertice(w).visitado:
          g.visitarVertice(w)
          queue.append(w)
          self.realizaMovimentoIda(v, w)
          self.realizaMovimentoVolta(v, w)

  def linhaReta(self, ouro):
    g = self._grafo
    for v in g.vertices():
      for o in ouro:
        v.dados["linhaReta"][o] = len(g.shortestPath(v.nome, o)) - 1


  def bestFirst(self, v):
    if self._pontuacao == 0:
      return "Morto"

    g = self._grafo

    if not self.checkOuro(v):
      adjacentes = [v for v in g.adjacentes(v)]
      w = ""
      minimal = g.ordem()
      for adj in adjacentes:
        if minimal > min(g.vertice(adj).dados["linhaReta"].values()):
          minimal = min(g.vertice(adj).dados["linhaReta"].values())
          w = adj
      
      self.realizaMovimentoIda(v, w)
      self.bestFirst(w)
    else:
      s = g.shortestPath(v, "0.0")
      a = v
      for u in s:
        self.realizaMovimentoVolta(u, a)
        a = u


  def Astar(self):
    # considerar todas as distancias na soma
    pass
