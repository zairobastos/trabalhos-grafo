class Grafo:
    def _init_(self, v):
        self.v = v
        self.vizinho = [[]]*v
        self.aresta = []

    def adicionarAresta(self, u: int, v: int, w: int):
        self.vizinho[u].append(v)
        self.vizinho[v].append(u)
        self.aresta.append((w, (u, v)))

    def dfs(self, vertice: int, visitados: list):
        visitados[vertice] = True
        for i in self.vizinho[vertice]:
            if not visitados[i]:
                self.dfs(i, visitados)

    def connected(self):
        visited = [False] * self.v
        self.dfs(0, visited)
        for i in range(1, self.v):
            if not visited[i]:
                return False
        return True

    def reverseDeleteMST(self):
        self.aresta.sort(key=lambda a: a[0])
        agm_peso = 0

        print("Arestas da Arvore Geradora Minima")
        for i in range(len(self.aresta) - 1, -1, -1):
            u = self.aresta[i][1][0]
            v = self.aresta[i][1][1]

            self.vizinho[u].remove(v)
            self.vizinho[v].remove(u)

            if self.connected() == False:
                self.vizinho[u].append(v)
                self.vizinho[v].append(u)

                print(f'{u} -- {v} = {self.aresta[i][0]}')
                agm_peso += self.aresta[i][0]
        print("Peso Total da AGM:", agm_peso)


if _name_ == "_main_":
    V = 9
    g = Grafo(V)

    g.adicionarAresta(0, 1, 4)
    g.adicionarAresta(0, 7, 8)
    g.adicionarAresta(1, 2, 8)
    g.adicionarAresta(1, 7, 11)
    g.adicionarAresta(2, 3, 7)
    g.adicionarAresta(2, 8, 2)
    g.adicionarAresta(2, 5, 4)
    g.adicionarAresta(3, 4, 9)
    g.adicionarAresta(3, 5, 14)
    g.adicionarAresta(4, 5, 10)
    g.adicionarAresta(5, 6, 2)
    g.adicionarAresta(6, 7, 1)
    g.adicionarAresta(6, 8, 6)
    g.adicionarAresta(7, 8, 7)

    g.reverseDeleteMST()
