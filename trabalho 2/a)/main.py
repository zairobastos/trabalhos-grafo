vertices = ['A', 'B', 'C', 'D', 'E', 'F']
arestas = {
    'AB': 4,
    'AC': 2,
    'BC': 1,
    'BD': 5,
    'CD': 8,
    'CE': 10,
    'DE': 2,
    'DF': 6,
    'EF': 2,
}

print("Arestas e respectivos pesos no grafo:")
for chave, valor in arestas.items():
    print(f'{chave[0]} -- {chave[1]} = {valor}')

makeset = [[v, 0] for v in vertices]

print("\nMakeset Inicial:")
for row in makeset:
    print(f'{row[0]}: {row}')

T = []


def Find(x):
    pos = vertices.index(x)
    while x != makeset[pos][0]:
        x = makeset[pos][0]
        pos = vertices.index(x)
    return x


def Union(u, v):
    pos1 = vertices.index(u)
    pos2 = vertices.index(v)

    Pu = Find(u)
    Pv = Find(v)

    if makeset[pos1][1] > makeset[pos2][1]:
        makeset[pos2][0] = Pu
    else:
        makeset[pos1][0] = Pv
        if makeset[pos1][1] == makeset[pos2][1]:
            makeset[pos2][1] += 1


arestas_ordenadas = sorted(arestas.items(), key=lambda x: x[1])
print(f'\nArestas ordenadas em ordem crescente:')
for chave, valor in arestas_ordenadas:
    print(f'{chave[0]} -- {chave[1]} = {valor}')

for chave, valor in arestas_ordenadas:
    u, v = chave[0], chave[1]
    if len(T) < len(vertices) - 1:
        if Find(u) != Find(v):
            T.append(chave)
            Union(u, v)

            ciclo = False
            for v in vertices:
                if Find(u) == Find(v) and makeset[vertices.index(v)][1] >= 2:
                    ciclo = True
                    break
            if ciclo:
                print(
                    "\nO grafo contém um ciclo negativo. A execução foi interrompida!!!!")
                break

if not ciclo:
    print("\nMakeset Final:")
    c = 0
    for row in makeset:
        print(f'{vertices[c]}: {row}')
        c += 1

    print("\nArestas selecionadas:")
    peso = 0
    for row in T:
        print(f'{row[0]} -- {row[1]} = {arestas[row]}')
        peso += arestas[row]

    print(f'\nÁrvore Geradora Mínima: {peso}')

    def dfs(grafo, verticeOrigem, verticeDestino, visitados, distancia, caminho):
        if verticeOrigem == verticeDestino:
            return distancia, caminho + [verticeOrigem]

        visitados.append(verticeOrigem)
        min_distancia = float('inf')
        min_caminho = []

        for vizinho, comprimento in grafo[verticeOrigem]:
            if vizinho not in visitados:
                distancia_vizinho, caminho_vizinho = dfs(
                    grafo, vizinho, verticeDestino, visitados, distancia + comprimento, caminho + [verticeOrigem])
                if distancia_vizinho < min_distancia:
                    min_distancia = distancia_vizinho
                    min_caminho = caminho_vizinho

        visitados.remove(verticeOrigem)
        return min_distancia, min_caminho

    grafo = {}
    for vertice in T:
        u, v = vertice[0], vertice[1]
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append((v, arestas[vertice]))
        grafo[v].append((u, arestas[vertice]))

    verticeOrigem = 'B'
    verticeDestino = 'F'

    visitados = []
    min_distancia, min_caminho = dfs(
        grafo, verticeOrigem, verticeDestino, visitados, 0, [])

    print(
        f"\nMenor distância na árvore geradora mínima entre {verticeOrigem} e {verticeDestino}: {min_distancia}")
    print(f"Caminho: {' -> '.join(min_caminho)}")
