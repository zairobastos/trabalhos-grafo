import numpy as np
arvore_fluxo = [
    # 1  2   3   4   5   6
    [0, 10, 15, 20, 0,   0],  # 1
    [0,  0,  0,  0, 5,  10],  # 2
    [0,  0,  0,  0, 12,  0],  # 3
    [0,  0,  0,  0, 15,   5],  # 4
    [0,  0,  0,  0, 0,  20],  # 5
    [0,  0,  0,  0, 0,   0]   # 6
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
    return fluxo_maximo, matriz_fluxo


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
val_fluxo_maximo, fluxo = edmonds_krap(arvore_fluxo, s, t)
print("\nFluxo: ", fluxo)
print("arvore_fluxo: ", arvore_fluxo)
print(f"Rede residual:\n {np.subtract(arvore_fluxo,fluxo)}")
print("O valor do fluxo máximo é:", val_fluxo_maximo)
