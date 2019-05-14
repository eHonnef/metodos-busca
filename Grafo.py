import random

# Classe grafo
class Grafo:
	# Em python, dicionarios sao naturalmente uma hash table
	# Dicionario que contem uma lista de objetos do tipo Vertice
	grafo = {}

	# Estrutura auxiliar que serve para salvar o grafo
	_grafo_ = {}

	# Construtor da classe Grafo
	# Parameto vertices deve ser uma lista de objetos da classe Vertice
	def __init__(self, vertices):
		for v in vertices:
			if v.nome not in self.grafo:
				self.grafo[v.nome] = v
			else:
				raise ValueError("Ha um vertice duplicado no grafo, por favor, mude o nome deste vertice: " + v.nome)

	# Retorna o grau de entrada de um vertice
	# Parametro vertice: Eh o vertice que se deseja saber o grau de entrada
	def grauEntrada(self, vertice):
		entrada = 0
		for v in self.grafo:
			if vertice in self.adjacentes(v):
				entrada += 1
		return entrada

	# Retorna o grau de entrada de um vertice de um grafo dado
	# Parametro vertice: Eh o vertice que se deseja saber o grau de entrada
	# Parametro graph: Eh o grafo que sera utilizado para a busca
	def grauEntradaG(self, graph, vertice):
		entrada = 0
		for v in graph:
			if vertice in self.adjacentesG(graph, v):
				entrada += 1
		return entrada

	# Adiciona um vertice no grafo
	# Parametro vertice: Eh um objeto do tipo Vertice
	def adicionaVertice(self, vertice):
		if (not isinstance(vertice, Vertice)) or (vertice.nome in self.grafo):
			return False

		self.grafo[vertice.nome] = vertice
		return True

	# Duplica o grafo (python usa ponteiros e referencias, eh complicado copiar objetos)
	def duplicarGrafo(self):
		self._grafo_ = self.grafo.copy()

	# Restaura o grafo
	def restaurarGrafo(self):
		self.grafo = self._grafo_.copy()

	# Remove um vertice do grafo junto com suas conexoes
	# Parametro nome: Eh o nome do vertice
	def removeVertice(self, nome):
		if nome not in self.grafo:
			return False

		del self.grafo[nome]

		for v in self.grafo:
			if nome in self.grafo[v].arestas: self.grafo[v].arestas.remove(nome)

		return True

	# Conecta dois vertices dado os nomes
	# Parametro v1: eh o nome do vertice 1
	# Parametro v2: eh o nome do vertice 2
	def conecta(self, v1, v2):
		if (v1 not in self.grafo) or (v2 not in self.grafo):
			return False

		if v1 not in self.grafo[v2].arestas: self.grafo[v2].arestas.append(v1)
		if v2 not in self.grafo[v1].arestas: self.grafo[v1].arestas.append(v2)

		return True

	# Desconecta dois vertices dado os nomes
	# Parametro v1: eh o nome do vertice 1
	# Parametro v2: eh o nome do vertice 2
	def desconecta(self, v1, v2):
		if (v1 not in self.grafo) or (v2 not in self.grafo):
			return False

		if v1 in self.grafo[v2].arestas: self.grafo[v2].arestas.remove(v1)
		if v2 in self.grafo[v1].arestas: self.grafo[v1].arestas.remove(v2)

		return True

	def marcarVertice(self, vertice):
		self.grafo[vertice].marcado = True

	# Retorna a ordem do grafo (numero de vertices)
	def ordem(self):
		return len(self.grafo)

	# Retorna uma lista contendo o nome dos vertices do grafo
	def nomeVertices(self):
		return list(self.grafo.keys())

	# Retorna uma lista contendo os objetos do tipo Vertice
	def vertices(self):
		return list(self.grafo.values())

	# Retorna o objeto vertice dado o nome do vertice
	# Parametro nome: eh o nome do objeto Vertice que se deseja
	def umVertice(self, nome):
		return self.grafo[nome]

	# Retorna um objeto vertice aleatorio
	def verticeAleatorio(self):
		return self.grafo[random.choice(list(self.grafo.keys()))]

	# Retorna uma lista dos adjacentes do vertice
	# Parametro nome: eh o nome do vertice que se desejam os adjacentes
	def adjacentes(self, nome):
		return self.grafo[nome].arestas

	# Retorna uma lista dos adjacentes do vertice de um grafo
	# Parametro nome: eh o nome do vertice que se desejam os adjacentes
	# Parametro graph: eh o grafo que sera utilizado na busca
	def adjacentesG(self, graph, nome):
		return graph[nome].arestas

	# Retorna o grau do vertice
	# Parametro nome: eh o nome do vertice que se deseja o grau
	def grau(self, nome):
		return len(self.grafo[nome].arestas)

	# Verifica se o grafo eh regular
	def regular(self):
		grau = -1
		for v in self.grafo:
			if grau < 0:
				grau = len(self.grafo[v].arestas)

			if grau != len(self.grafo[v].arestas):
				return False
		return True

	# Verifica se o grafo eh completo
	def completo(self):
		for v in self.grafo:
			if set(self.grafo[v].arestas) != set(self.grafo.keys()):
				return False
		return True

	# Retorna o fecho transitivo de um vertice
	# Parametro nome: eh o nome do vertice que se deseja encontrar o fecho transitivo
	# Parametro visitados (default [], lista vazia): opcional, eh uma lista de vertices que ja foram utilizados, serve para o tracking de informacoes da recursao
	def fechoTransitivo(self, nome, visitados = []):
		visitados.append(nome)
		for vAdj in self.adjacentes(nome):
			if vAdj not in visitados:
				self.fechoTransitivo(vAdj, visitados)
		return visitados

	# Verifica se o grafo eh conexo ou nao
	def conexo(self):
		return set(self.fechoTransitivo(self.verticeAleatorio().nome)) == set(self.grafo.keys())

	# Verifica se ha algum ciclo no grafo
	def buscaCiclo(self):
		for v in self.grafo:
			if self.haCicloCom(v):
				return True
		return False

	# Verifica se ha ciclos que o vertice "nome" faz parte
	# Parametro nome: eh o nome do vertice inicial
	# Parametro vAnt (default ""): opcional, eh o vertice anterior da busca, serve para o tracking da recursao
	# Parametro visitados (default [], lista vazia): opcional, eh uma lista de vertices que ja foram utilizados, serve para o tracking de informacoes da recursao
	def haCicloCom(self, nome, vAnt = "", visitados = []):
		if nome in visitados:
			return True

		visitados.append(nome)
		for vAdj in self.adjacentes(nome):
			if vAdj != vAnt and vAdj != nome:
				if self.haCicloCom(vAdj, nome, visitados):
					return True
		visitados.remove(nome)
		return False

	# Verifica se o grafo eh uma arvore
	def arvore(self):
		return self.conexo() and not self.buscaCiclo()

	# Limpa as marcacoes no vertice, define os atributos marcado e visitado do vertice como falso
	def limpaVertices(self):
		for v in self.grafo:
			self.grafo[v].visitado = False
			self.grafo[v].marcado = False

	# Retorna uma lista com a ordem topologica do grafo
	# Parametro limpar(default True): opcional, se verdadeiro limpa as marcacoes dos vertices (coloca visitado e marcado como falso)
	def ordemTopologica(self, limpar = True):
		if limpar:
			self.limpaVertices()
		nao_marcados = [x for x in self.grafo]
		ordem = []
		while nao_marcados:
			vertice = random.choice(nao_marcados)
			nao_marcados.remove(vertice)
			self.visitar(vertice, ordem)
		
		self.limpaVertices()
		return ordem

	# Funcao auxiliar para a ordem topologica, faz a busca em profundidade e ja verifica se possui ciclo
	# Parametro v: eh o vertice que se deseja visitar
	# Parametro ordem: eh a lista que contem os vertices ordenados, serve para o tracking da recursao
	def visitar(self, v, ordem):
		if self.grafo[v].marcado:
			return

		if self.grafo[v].visitado:
			raise ValueError("Grafo ciclico")

		self.grafo[v].visitado = True
		for vAdj in self.adjacentes(v):
			self.visitar(vAdj, ordem)

		self.grafo[v].marcado = True
		self.grafo[v].visitado = False
		ordem.insert(0, v)

	# Funcao que busca a base de um grafo
	# Parametro graph: opcional, eh o grafo que se deseja fazer a busca
	def buscaBase(self, graph = grafo):
		if self.buscaCiclo():
			return []
		return [v for v in graph if not self.grauEntradaG(graph, v)]
	
	def buscaProfundidade(self):
		pass
	
	def buscaLargura(self):
		pass

#######################################################################################
# Classe vertice
class Vertice:
	# Construtor da classe Vertice
	# Parametro nome eh o identificador do vertice
	# Parametro arestas eh uma lista de conexoes do vertice (pode ser vazio)
	# Parametro dados eh um dicionario contendo os dados que o vertice representa (pode ser vazio)
	def __init__(self, nome, arestas, dados):
		if nome == "":
			raise ValueError("Nome esta em branco, por favor de um nome para o coitado")

		self.nome = str(nome)
		self.arestas = list(arestas)
		self.dados = dict(dados)
		self.visitado = False
		self.marcado = False
#######################################################################################
