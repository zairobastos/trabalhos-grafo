arvore_fluxo = [
    #  s  v1  v2  v3  v4   t
    [0, 16, 13, 0,  0,  0],  # s
    [0, 0,  0,  12, 0,  0],  # v1
    [0, 4,  0,  0,  14, 0],  # v2
    [0, 0,  9,  0,  0,  20],  # v3
    [0, 0,  0,  7,  0,  4],  # v4
    [0, 0,  0,  0,  0,  0]   # t
]


def edmonds_krap(arvore_fluxo, s, t):
    vertices = len(arvore_fluxo)
    matriz_fluxo = [[0] * vertices for _ in range(vertices)]
    caminho = bfs(arvore_fluxo, matriz_fluxo, s, t)
    while caminho is not None:
        fluxo_aumentador = min(
            arvore_fluxo[u][v] - matriz_fluxo[u][v] for u, v in caminho)
        print(f"Caminho: {caminho} - Fluxo: {fluxo_aumentador}")
        for u, v in caminho:
            matriz_fluxo[u][v] += fluxo_aumentador
        caminho = bfs(arvore_fluxo, matriz_fluxo, s, t)
    fluxo_maximo = sum(matriz_fluxo[s][i] for i in range(vertices))
    return fluxo_maximo


def bfs(arvore_fluxo, matriz_fluxo, s, t):
    visitado = [s]
    caminhos = {s: []}
    if s == t:
        return caminhos[s]
    while visitado:
        u = visitado.pop(0)
        for v in range(len(arvore_fluxo)):
            if (arvore_fluxo[u][v] - matriz_fluxo[u][v] > 0) and v not in caminhos:
                caminhos[v] = caminhos[u] + [(u, v)]
                if v == t:
                    return caminhos[v]
                visitado.append(v)
    return None


s = 0
t = 5
val_fluxo_maximo = edmonds_krap(arvore_fluxo, s, t)
print("\nValor do fluxo máximo:", val_fluxo_maximo)
