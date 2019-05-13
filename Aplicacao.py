import Grafo
import random
from copy import deepcopy, copy

# Criando o grafo e arestas
vertices = [
	Grafo.Vertice("INE5402", 
		["INE5404"], 
		{"codigo":"INE5402", "nome":"Programacao Orientada a objetos I", "creditos":6}),
	Grafo.Vertice("INE5404", 
		["INE5408", "INE5410", "INE5414"], 
		{"codigo":"INE5404", "nome":"Programacao Orientada a objetos II", "creditos":6}),
	Grafo.Vertice("INE5408", 
		["INE5417", "INE5413", "INE5415", "INE5416", "INE5412", "INE5423", "INE5420"], 
		{"codigo":"INE5408", "nome":"Estrutura de dados", "creditos":6}),
	Grafo.Vertice("INE5417", 
		["INE5419", "INE5427", "INE5453"], 
		{"codigo":"INE5417", "nome":"Engenharia de software I", "creditos":5}),
	Grafo.Vertice("INE5419", 
		[], 
		{"codigo":"INE5419", "nome":"Engenharia de software II", "creditos":4}),
	Grafo.Vertice("INE5427", 
		["INE5433"], 
		{"codigo":"INE5427", "nome":"Planejamento e gestao de projetos", "creditos":4}),
	Grafo.Vertice("INE5433", 
		["INE5434"], 
		{"codigo":"INE5433", "nome":"Trabalho de conclusao de curso I", "creditos":6}),
	Grafo.Vertice("INE5434", 
		[], 
		{"codigo":"INE5434", "nome":"Trabalho de conclusao de curso II", "creditos":6}),
	Grafo.Vertice("MTM5161", 
		["MTM7174", "INE5405"], 
		{"codigo":"MTM5161", "nome":"Calculo A", "creditos":4}),
	Grafo.Vertice("MTM7174", 
		["INE5409", "INE5420"], 
		{"codigo":"MTM7174", "nome":"Calculo B", "creditos":4}),
	Grafo.Vertice("INE5410", 
		["INE5412"], 
		{"codigo":"INE5410", "nome":"Programacao concorrente", "creditos":4}),
	Grafo.Vertice("INE5413", 
		["INE5430"], 
		{"codigo":"INE5413", "nome":"Grafos", "creditos":4}),
	Grafo.Vertice("INE5423", 
		["INE5432"], 
		{"codigo":"INE5423", "nome":"Banco de dados I", "creditos":4}),
	Grafo.Vertice("INE5453", 
		["INE5433"], 
		{"codigo":"INE5453", "nome":"Introducao ao trabalho de concusao de curso", "creditos":1}),
	Grafo.Vertice("INE5432", 
		[], 
		{"codigo":"INE5432", "nome":"Banco de dados II", "creditos":4}),
	Grafo.Vertice("INE5403", 
		["INE5413", "INE5415", "INE5429"], 
		{"codigo":"INE5403", "nome":"Matematica discreta para computacao", "creditos":6}),
	Grafo.Vertice("INE5405", 
		["INE5425", "INE5430"], 
		{"codigo":"INE5405", "nome":"Probabilidade e estatistica", "creditos":5}),
	Grafo.Vertice("INE5409", 
		[], 
		{"codigo":"INE5409", "nome":"Calculo Numerico", "creditos":4}),
	Grafo.Vertice("INE5415", 
		["INE5421"], 
		{"codigo":"INE5415", "nome":"Teoria da computacao", "creditos":4}),
	Grafo.Vertice("INE5420", 
		[], 
		{"codigo":"INE5420", "nome":"Computacao Grafica", "creditos":4}),
	Grafo.Vertice("INE5425", 
		[], 
		{"codigo":"INE5425", "nome":"Modelagem e simulacao", "creditos":4}),
	Grafo.Vertice("INE5429", 
		[], 
		{"codigo":"INE5429", "nome":"Seguranca em computacao", "creditos":4}),
	Grafo.Vertice("INE5401", 
		[], 
		{"codigo":"INE5401", "nome":"Introducao a computacao", "creditos":1}),
	Grafo.Vertice("MTM5512", 
		["MTM5245", "INE5409"], 
		{"codigo":"MTM5512", "nome":"Geometria Analitica", "creditos":4}),
	Grafo.Vertice("MTM5245", 
		["INE5420"], 
		{"codigo":"MTM5245", "nome":"Algebra Linear", "creditos":4}),
	Grafo.Vertice("INE5416", 
		["INE5430"], 
		{"codigo":"INE5416", "nome":"Paradigmas de programacao", "creditos":5}),
	Grafo.Vertice("INE5421", 
		["INE5426"], 
		{"codigo":"INE5421", "nome":"Linguagens formais e compiladores", "creditos":4}),
	Grafo.Vertice("INE5430", 
		[], 
		{"codigo":"INE5430", "nome":"Inteligencia artificial", "creditos":4}),
	Grafo.Vertice("INE5431", 
		[], 
		{"codigo":"INE5431", "nome":"Sistemas multimidia", "creditos":4}),
	Grafo.Vertice("EEL5105", 
		["INE5406"], 
		{"codigo":"EEL5105", "nome":"Circuitos e tecnicas digitais", "creditos":5}),
	Grafo.Vertice("INE5406", 
		["INE5411"], 
		{"codigo":"INE5406", "nome":"Sistemas digitais", "creditos":5}),
	Grafo.Vertice("INE5411", 
		["INE5412"], 
		{"codigo":"INE5411", "nome":"Organizacao de computadores I", "creditos":6}),
	Grafo.Vertice("INE5412", 
		["INE5418", "INE5424"], 
		{"codigo":"INE5412", "nome":"Sistemas operacionais I", "creditos":4}),
	Grafo.Vertice("INE5424", 
		[], 
		{"codigo":"INE5424", "nome":"Sistemas operacionais II", "creditos":4}),
	Grafo.Vertice("INE5418", 
		[], 
		{"codigo":"INE5418", "nome":"Computacao Distribuida", "creditos":4}),
	Grafo.Vertice("INE5426", 
		[], 
		{"codigo":"INE5426", "nome":"Construcao de compiladores", "creditos":4}),
	Grafo.Vertice("INE5428", 
		[], 
		{"codigo":"INE5428", "nome":"Informatica e sociedade", "creditos":4}),
	Grafo.Vertice("INE5407", 
		["INE5428"], 
		{"codigo":"INE5407", "nome":"Ciencia, tecnologia e sociedade", "creditos":3}),
	Grafo.Vertice("INE5414", 
		["INE5418", "INE5431", "INE5429", "INE5422"], 
		{"codigo":"INE5414", "nome":"Redes de computadores I", "creditos":4}),
	Grafo.Vertice("INE5422", 
		[], 
		{"codigo":"INE5422", "nome":"Redes de computadores II", "creditos":4})
]

grafo = Grafo.Grafo(vertices)

# Marcando disciplinas(vertices) cursados
grafo.marcarVertice("INE5402")
grafo.marcarVertice("INE5404")
grafo.marcarVertice("INE5408")
grafo.marcarVertice("INE5417")
grafo.marcarVertice("INE5419")
grafo.marcarVertice("INE5453")
grafo.marcarVertice("MTM5161")
grafo.marcarVertice("MTM7174")
grafo.marcarVertice("INE5410")
grafo.marcarVertice("INE5413")
grafo.marcarVertice("INE5423")
grafo.marcarVertice("INE5403")
grafo.marcarVertice("INE5405")
grafo.marcarVertice("INE5415")
grafo.marcarVertice("INE5429")
grafo.marcarVertice("INE5401")
grafo.marcarVertice("MTM5512")
grafo.marcarVertice("MTM5245")
grafo.marcarVertice("INE5416")
grafo.marcarVertice("INE5431")
grafo.marcarVertice("EEL5105")
grafo.marcarVertice("INE5406")
grafo.marcarVertice("INE5411")
grafo.marcarVertice("INE5412")
grafo.marcarVertice("INE5428")
grafo.marcarVertice("INE5407")
grafo.marcarVertice("INE5414")
grafo.marcarVertice("INE5422")

# Busca a ordem topologica do grafo (falso porque nao ira desmarcar os vertices marcados anteriormente)
ordemTop = grafo.ordemTopologica(False)

# Duplica o grafo para salvar o original
grafo.duplicarGrafo()

# Lista as chaves de busca do grafo (nome dos vertices)
vs = list(grafo.nomeVertices())

# Remove temporariamente os vertices do grafo que nao estao na ordem topologica (a.k.a. ja foram cursados)
for v in vs:
	if v not in ordemTop:
		grafo.removeVertice(v)

# Variaveis auxiliares
chMax = 30
chAtual = 0

# Listas que serao utilizadas para armazenar as informacoes
semestre = []
ano = []

# Busca a base do grafo
base = grafo.buscaBase()

while base:
	for v in base:
		chAtual += grafo.grafo[v].dados["creditos"]
		if chAtual < chMax:
			semestre.append(v)
		else:
			chAtual -= grafo.grafo[v].dados["creditos"]

	for v in semestre:
		grafo.removeVertice(v)
	base = grafo.buscaBase()

	ano.append(semestre)
	semestre = []
	chAtual = 0

# Restaura o grafo que foi salvo anteriormente
grafo.restaurarGrafo()

# Imprime na tela as informacoes
for semestre in ano:
	chAtual = 0
	for disc in semestre:
		print(grafo.grafo[disc].dados["nome"] + ": " + str(grafo.grafo[disc].dados["creditos"]))
		chAtual += grafo.grafo[disc].dados["creditos"]
	print("Total: " + str(chAtual) + " h/a")
	print("\n")
