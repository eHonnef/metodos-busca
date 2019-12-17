# Métodos de busca

Métodos de busca para disciplina INE5430@UFSC.  
Instale os pacotes necessários usando `pip install -r requirements.txt`.  
Inclui uma estrutura de grafos `Grafo.py` e uma aplicação em grafos `Aplicacao.py`.  

## Enunciado

Vamos programar agentes baseados em buscas para capturar ouro em uma mina. Cada agente consegue se movimentar pela mina, mas isso gasta sua bateria que é muito cara e não é recarregável. Os movimentos do agente são ir para a esquerda (E), ir para a direita (D), ir para cima (C), ir para baixo (B). O agente pode também pegar o ouro (PO). O objetivo principal de cada agente é maximizar a quantidade de ouro capturado e minimizar as perdas de energia de sua bateria.  
A mina será considerada na entrada dos dados. Ela será representada por uma matriz M, com n linhas e n colunas.  
Cada posição (i; j) da mina pode significar:

- uma posição com obstáculo, se M[i][j] = 1;
- um posição com ouro, se M[i][j] = *;
- uma posição livre, se M[i][j] = 0.  


Exemplo de entrada:

          8
          0 0 0 0 1 0 0 *
          1 1 1 0 1 0 1 1
          0 0 0 0 1 0 1 0
          * 0 1 1 1 0 0 0
          0 0 0 0 0 0 0 0
          1 1 1 0 1 1 1 0
          0 0 1 0 0 * 1 0
          0 0 0 0 0 0 1 *


Nesta mina, há uma expectativa de n=2 posições (não necessariamente alcançáveis) com ouro. A bateria do agente começa com n^1.5 pontos. Se um agente consegue se movimentar de uma posição para outra, então consideramos que houve uma perda de 1 ponto na sua bateria. Cada ouro capturado significa uma possível compra de cinco baterias novas (com n^1.5 pontos) para o agente. É claro que o agente fica impossibilitado de se movimentar quando a bateria acaba.

## Métodos implementados

- DFS - Deep first search ou busca em profundidade;
- BFS - Breadth first search ou busca em largura;
- Best-first;
- A* - A star;

## Heurísticas usadas

### Best-First

A heurística usada foi a menor distância manhattan do nó atual (A) até o nodo contendo o ouro mais próximo (N).

### A*

Para A* foi usada a mesma heurística do best-first, porém se a distância até o ouro mais próximo para o nó A e nó B é igual, então ele escolhe o nó com a menor distância relativa aos outros nós contendo ouro. Essa distância é obtida somando todas as distâncias até os nós contendo ouro.  
Por exemplo, considere o seguinte grafo, sendo que os nodos O contém ouro:

                A
              /   \
             B--O1--C--------D---------O2

As distâncias manhattan calculadas são:  
A = [2, 3]  
B = [1, 4]  
C = [1, 2]  
D = [2, 1]  
O1 = [0, 3]  
O2 = [3, 0]  

Quando a busca chega no nó A, o best-first seleciona qualquer um dos dois (depende da ordem de criação do grafo), porém o A* escolherá o C pois a distância até O1 é igual para B e C mas a soma das distâncias (3 para C e 5 para B) fará com que C seja escolhido.

## Resultados obtidos

Os valores na tabela representam, respectivamente [pontuação/número de passos]

| Entrada | DFS        | BFS        | Best-First   | A*        |
|---------|------------|------------|--------------|-----------|
|8x8      |394 / 72    |315 / 149   |403 / 62      |403 / 62   |
|16x16    |2326 / 306  |2075 / 555  |2527 / 104    |2527 / 104 |
|32x32    |13341 / 1336|12532 / 2143|14388 / 288   |14342 / 334|
|64x64    |-           |-           |81865 / 598   |81831 / 632|

Os métodos DFS e BFS não terminaram sua execução na matriz 64x64 pois atingem o limite da recursão para a linguagem, isso se deve a suas complexidades naturais O(b^m) e O(b^d), sendo, respectivamente DFS e BFS, e b sendo o fator de branching, d e m sendo a profundidade máxima.
