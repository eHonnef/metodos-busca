import Grafo
import random
import pandas as pd
import numpy as np

class Busca:

  def __init__(self, grafo, size):
    if not isinstance(grafo, Grafo.Grafo):
      raise ValueError("O grafo não é uma instância de Grafo.")
    
    self._size = size
    self._grafo = grafo
    self._pontuacao = int(size**1.5)
    self._nOuro = int(size/2)
    self._movimento = list()
    self._ouroEncontrado = list()
  
  def buscaProfundidade(self, v):
    if self._pontuacao == 0:
     return "Morto"

    # para nao ficar escrevendo self._grafo toda hora
    g = self._grafo

    g.marcarVertice(v)
    if g.vertice(v).dados["conteudo"] == 2:
      self._pontuacao += 5 * int(self._size**1.5)
      self._nOuro -= 1
      self._ouroEncontrado.append(str(g.vertice(v).dados["row"]) + "." + str(g.vertice(v).dados["col"]))
    
    if self._nOuro == 0:
      self.voltarInicio(v)

    for adjacente in g.adjacentes(v):
      if g.vertice(adjacente).marcado:
        continue

      if g.vertice(adjacente).dados["row"] > g.vertice(v).dados["row"]:
        self._movimento.append("B->" + str(g.vertice(adjacente).dados["row"]) + "." + str(g.vertice(adjacente).dados["col"]))
      elif g.vertice(adjacente).dados["row"] < g.vertice(v).dados["row"]:
        self._movimento.append("C->" + str(g.vertice(adjacente).dados["row"]) + "." + str(g.vertice(adjacente).dados["col"]))
        # self._movimento.append("C")
      elif g.vertice(adjacente).dados["col"] > g.vertice(v).dados["col"]:
        self._movimento.append("D->" + str(g.vertice(adjacente).dados["row"]) + "." + str(g.vertice(adjacente).dados["col"]))
        # self._movimento.append("D")
      elif g.vertice(adjacente).dados["col"] < g.vertice(v).dados["col"]:
        self._movimento.append("E->" + str(g.vertice(adjacente).dados["row"]) + "." + str(g.vertice(adjacente).dados["col"]))
        # self._movimento.append("E")

      self._pontuacao -= 1
      self.buscaProfundidade(adjacente)

      # Quando volta da recursao ele volta pro nodo
      if g.vertice(adjacente).dados["row"] > g.vertice(v).dados["row"]:
        self._movimento.append("C->" + str(g.vertice(v).dados["row"]) + "." + str(g.vertice(v).dados["col"]))
      elif g.vertice(adjacente).dados["row"] < g.vertice(v).dados["row"]:
        self._movimento.append("B->" + str(g.vertice(v).dados["row"]) + "." + str(g.vertice(v).dados["col"]))
        # self._movimento.append("C")
      elif g.vertice(adjacente).dados["col"] > g.vertice(v).dados["col"]:
        self._movimento.append("E->" + str(g.vertice(v).dados["row"]) + "." + str(g.vertice(v).dados["col"]))
        # self._movimento.append("D")
      elif g.vertice(adjacente).dados["col"] < g.vertice(v).dados["col"]:
        self._movimento.append("D->" + str(g.vertice(v).dados["row"]) + "." + str(g.vertice(v).dados["col"]))
        # self._movimento.append("E")

      self._pontuacao -= 1
  
  def voltarInicio(self, v):
    # Se todos os vertices estao marcados ele nao visita mais na call recursiva
    self._grafo.marcarTodosVertices()
    # pass

  def buscaLargura(self):
    pass