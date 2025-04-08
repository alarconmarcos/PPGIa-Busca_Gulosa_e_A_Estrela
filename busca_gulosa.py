import grafo as gf

def gulosa(grafo, vertice):
  local_atual = vertice
  caminho = []
  caminho.append(local_atual)
  while (local_atual != "Bucharest"):
    menor_vertice = None
    menor_valor = float("inf")  # Inicializa com infinito
    for vizinho in grafo.neighbors(local_atual):
      if vizinho in gf.my_dict:
        if(vizinho not in caminho):
            if (gf.my_dict[vizinho] < menor_valor):
              menor_valor = gf.my_dict[vizinho]
              menor_vertice = vizinho
    local_atual = menor_vertice
    caminho.append(local_atual)

  return caminho
