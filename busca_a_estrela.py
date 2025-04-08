import grafo as gf


def a_estrela(grafo, vertice):
  local_atual = vertice
  caminho = []
  caminho.append(local_atual)
  while (local_atual != "Bucharest"):
    menor_vertice = None
    menor_valor = float("inf")  # Inicializa com infinito
    for vizinho in grafo.neighbors(local_atual):
      if vizinho in gf.dist:
        peso = gf.dist[vizinho] + grafo[local_atual][vizinho]["weight"]
        if(vizinho not in caminho): # Evitar loop, não retroceder em uma cidade que já foi
            if (peso < menor_valor):
              menor_valor = peso
              menor_vertice = vizinho
    local_atual = menor_vertice
    caminho.append(local_atual)

  return caminho