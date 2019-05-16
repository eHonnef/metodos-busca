import random

# Classe grafo (direcional)
class Grafo:
	# Em python, dicionarios sao naturalmente uma hash table
	# Dicionario que contem uma lista de objetos do tipo Vertice
	grafo = {}

	# Estrutura auxiliar que serve para salvar o grafo
	_grafo_ = {}
	_arestas_ = []

	# Construtor da classe Grafo
	# Parameto vertices deve ser uma lista de objetos da classe Vertice
	def __init__(self):
		self.arestas = []

	def verticeExiste(self, v):
		return v in self.grafo

	# Retorna o grau de entrada de um vertice
	# Parametro vertice: Eh o vertice que se deseja saber o grau de entrada
	def grauEntrada(self, vertice):
		entrada = 0
		for v in self.grafo:
			if vertice in self.adjacentes(v):
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
	def salvarGrafo(self):
		self._arestas_ = self.arestas.copy()
		self._grafo_ = self.grafo.copy()

	# Restaura o grafo
	def restaurarGrafo(self):
		self.arestas = self._arestas_.copy()
		self.grafo = self._grafo_.copy()
		for a in self.arestas:
			self.conecta(a.vs[0], a.vs[1])

	# Remove um vertice do grafo junto com suas conexoes
	# Parametro vertice: Eh o nome do vertice
	def removeVertice(self, vertice):
		if vertice not in self.grafo:
			return False

		for a in self.arestas:
			if vertice in a.vs: self.arestas.remove(a)
		
		for v in self.grafo:
			if vertice in self.grafo[v].adjacentes: self.grafo[v].adjacentes.remove(vertice)

		del self.grafo[vertice]
		return True

	# Conecta dois vertices dado os nomes
	# Parametro v0: eh o nome do vertice 1
	# Parametro v1: eh o nome do vertice 2
	def conecta(self, v0, v1):
		add = True
		ar = 0
		for a in self.arestas:
			if v0 in a.vs and v1 in a.vs:
				add = False
				ar = a
				break

		if add:
			ar = Aresta(v0, v1)
			self.arestas.append(Aresta(v0, v1))

		if v1 not in self.grafo[v0].adjacentes:
			self.grafo[v0].adjacentes.append(v1)
		
		if v0 not in self.grafo[v1].adjacentes:
			self.grafo[v1].adjacentes.append(v0)

		return ar

	def getAresta(self, v0, v1):
		for a in self.arestas:
			if v0 in a.vs and v1 in a.vs:
				return a
		
		return None

	# Desconecta dois vertices dado os nomes
	# Parametro v1: eh o nome do vertice 1
	# Parametro v2: eh o nome do vertice 2
	def desconecta(self, v0, v1):
		if (v0 not in self.grafo) or (v1 not in self.grafo):
			return False

		for a in self.arestas:
			if v0 in a.vs and v1 in a.vs:
				self.grafo[v0].adjacentes.remove(v1)
				self.grafo[v1].adjacentes.remove(v0)
				self.arestas.remove(a)
				return True

		return False

	def marcarVertice(self, vertice):
		self.grafo[vertice].marcado = True
	
	def visitarVertice(self, v):
		self.grafo[v].visitado = True

	def marcarTodosVertices(self):
		for v in self.grafo:
			self.grafo[v].visitado = True
			self.grafo[v].marcado = True

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
	def vertice(self, nome):
		return self.grafo[nome]

	# Retorna um objeto vertice aleatorio
	def verticeAleatorio(self):
		return self.grafo[random.choice(list(self.grafo.keys()))]

	# Retorna uma lista contendo o nome dos vertices adjacentes do vertice dado
	# Parametro nome: eh o nome do vertice que se desejam os adjacentes
	def adjacentes(self, nome):
		return self.grafo[nome].adjacentes

	# Retorna o grau do vertice
	# Parametro nome: eh o nome do vertice que se deseja o grau
	def grau(self, nome):
		return len(self.grafo[nome].adjacentes)

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
			if not self.grafo[v].visitado:
				if self._buscaCiclo(v):
					self.limpaVertices()
					return True
		
		self.limpaVertices()
		return False

	def _buscaCiclo(self, v, parent = ""):
		self.grafo[v].visitado = True

		for adj in self.adjacentes(v):
			if not self.grafo[adj].visitado:
				if self._buscaCiclo(adj, v):
					return True
			elif parent != adj:
				return True
		
		return False
	
	def _minDist(self, dist, Q):
		mini = len(self.grafo) * 200
		vertex = ""
		for v in Q:
			if dist[v] < mini:
				mini = dist[v]
				vertex = v
		return vertex

	# Buscar caminho usando bfs
	def shortestPath(self, source, dest):
		if source == dest:
			return []

		self.limpaVertices()
		path = self._shortestPath(source, dest)
		self.limpaVertices()
		rtn = [dest]
		p = path[dest]
		rtn.append(p)
		q = ""

		while path:
			#GAMBIARRA
			try:
				q = p
				rtn.append(path[p])
				p = path[p]
				del path[q]
			except:
				break

		rtn.reverse()
		return rtn

	def _shortestPath(self, source, dest):
		S = [source]
		path = {}
		self.grafo[source].visitado = True
		while S:
			v = S[0]
			S.remove(v)

			if v == dest:
				return path
			
			for adj in self.adjacentes(v):
				if not self.grafo[adj].visitado:
					self.grafo[adj].visitado = True
					S.append(adj)
					path[adj] = v


	# Verifica se o grafo eh uma arvore
	def isArvore(self):
		return self.conexo() and not self.buscaCiclo()
	
	# Transforma o grafo em uma MST usando kruskal
	def _desconetaTodos(self):
		for v in self.grafo:
			self.grafo[v].adjacentes.clear()
		self.arestas.clear()

	def arvore(self):
		self.salvarGrafo()
		ar = list(self.arestas)
		self._desconetaTodos()

		for a in ar:
			self.conecta(a.vs[0], a.vs[1])
			if self.buscaCiclo():
				self.desconecta(a.vs[0], a.vs[1])
	
	def maxDepth(self, root):
		if not self.isArvore():
			return -1
		
		self.salvarGrafo()
		folhas = []
		d = 0

		while len(self.grafo) > 0:
			self._maxDepth(root, root, folhas)
			if not folhas:
				break

			for f in folhas:
				self.removeVertice(f)
			d += 1
			
			self.limpaVertices()
			folhas.clear()
		
		self.restaurarGrafo()
		return d
	
	def _maxDepth(self, root, v, folhas = []):
		self.grafo[v].visitado = True
		if len(self.adjacentes(v)) < 2 and v != root:
			folhas.append(v)
		
		for adj in self.adjacentes(v):
			if not self.grafo[adj].visitado:
				self._maxDepth(root, adj, folhas)

	# Limpa as marcacoes no vertice, define os atributos marcado e visitado do vertice como falso
	def limpaVertices(self):
		for v in self.grafo:
			self.grafo[v].visitado = False
			self.grafo[v].marcado = False

#######################################################################################
# Classe vertice
class Vertice:
	# Construtor da classe Vertice
	# Parametro nome eh o identificador do vertice
	# Parametro arestas eh uma lista de conexoes do vertice (pode ser vazio)
	# Parametro dados eh um dicionario contendo os dados que o vertice representa (pode ser vazio)
	def __init__(self, nome, dados):
		if nome == "":
			raise ValueError("Nome esta em branco, por favor de um nome para o coitado")

		self.nome = str(nome)
		self.adjacentes = list()
		self.dados = dict(dados)
		self.visitado = False
		self.marcado = False

#######################################################################################
# Classe aresta
class Aresta:
	def __init__(self, v0, v1):
		self.vs = [v0, v1]
	
	def setPeso(self, valor):
		self.peso = valor
#######################################################################################