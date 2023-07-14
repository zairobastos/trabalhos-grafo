def busca_em_profundidade(grafo, no_atual, visitados, pilha):
    visitados[no_atual] = True
    pilha.append(no_atual)

    for vizinho in grafo[no_atual]:
        if vizinho in pilha:
            print(f"Existe um loop entre os vértices {vizinho} e {no_atual}.")
            return True
        else:
            if not visitados[vizinho]:
                if busca_em_profundidade(grafo, vizinho, visitados, pilha):
                    return True

    pilha.pop()

    return False


def verificaArvore(grafo):
    num_vertices = len(grafo)
    visitados = [False] * num_vertices

    primeira_chave = list(grafo.keys())[0]

    # verifica se tem vértice isolado
    for no in grafo:
        if no != primeira_chave and not any(no in vizinhos for vizinhos in grafo.values()):
            print(f"O vértice {no} é isolado na árvore")
            return True

    # verifica se tem laço na árvore
    for no in grafo:
        if no != primeira_chave and not visitados[no]:
            pilha = []
            if busca_em_profundidade(grafo, no, visitados, pilha):
                print("A árvore contém um loop")
                return True

    return False


def busca_caminho_em_profundidade(grafo, no_atual, visitados, pilha, chegada):
    visitados[no_atual] = True
    pilha.append(no_atual)

    if no_atual == chegada:
        return pilha.copy()

    for vizinho in grafo[no_atual]:
        if not visitados[vizinho]:
            caminho = busca_caminho_em_profundidade(
                grafo, vizinho, visitados, pilha, chegada)
            if caminho:
                return caminho

    pilha.pop()
    return None


def caminho_minimo(caminho_u, caminho_v):
    for i in range(len(caminho_u) - 1, -1, -1):
        for j in range(len(caminho_v) - 1, -1, -1):
            if caminho_u[i] == caminho_v[j]:
                return i, j, caminho_u[i]
    return None


def encontrar_caminho_minimizado(grafo):
    existe = verificaArvore(grafo)
    if not existe:
        u = int(input("Vértice (u): "))
        v = int(input("Vértice (v): "))

        vertices_arvore = list(grafo.keys())
        if u in vertices_arvore and v in vertices_arvore:
            print(f"\n\nOs vértices {u} e {v} estão presentes na árvore.")

            # Busca em profundidade da raiz até u
            visitados_u = [False] * len(grafo)
            pilha_u = []
            busca_caminho_em_profundidade(grafo, 0, visitados_u, pilha_u, u)
            caminho_u = pilha_u.copy()

            # Busca em profundidade da raiz até v
            visitados_v = [False] * len(grafo)
            pilha_v = []
            busca_caminho_em_profundidade(grafo, 0, visitados_v, pilha_v, v)
            caminho_v = pilha_v.copy()

            u2, v2, val = caminho_minimo(caminho_u, caminho_v)

            print(f"Caminho de {val} até {u}: {caminho_u[u2:]}")
            print(f"Caminho de {val} até {v}: {caminho_v[v2:]}")
        else:
            print(
                "Não é possível verificar o ancestral comum, pois um ou ambos os vértices não estão na árvore.")


arvore = {
    0: [1, 2],
    1: [3],
    2: [4, 5],
    3: [1],
    4: [6, 7],
    5: [],
    6: [],
    7: [],
}

"""
      0
     / \
    1   2
   /   / \
  3   4   5
     / \
    6   7 
"""

encontrar_caminho_minimizado(arvore)
