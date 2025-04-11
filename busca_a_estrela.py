import grafo as gf


def a_estrela(grafo, vertice):
  local_atual = vertice
  caminho = []
  caminho.append(local_atual)
  while (local_atual != "Bucharest"):                                   # Enquanto não chegar em Bucharest
    menor_vertice = None
    menor_valor = float("inf")                                          # Inicializa com infinito
    for vizinho in grafo.neighbors(local_atual):                        # Verifica os vizinhos do vertice atual
      if vizinho in gf.dist:                                            # Verifica se o vizinho está no dicionário de distâncias heurísticas                
        peso = gf.dist[vizinho] + grafo[local_atual][vizinho]["weight"] # Soma a distância heuristica do vizinho com o peso da aresta (local_atual até vizinho)
        if(vizinho not in caminho):                                     # Evitar loop, não retroceder em uma cidade que já foi
            if (peso < menor_valor):                                    # Verifica se o vizinho tem um valor menor que o menor valor encontrado
              menor_valor = peso
              menor_vertice = vizinho
    local_atual = menor_vertice                                         # Atualiza o vertice atual para o menor vertice encontrado                
    caminho.append(local_atual)                                         # Adiciona o menor vertice encontrado ao caminho            

  return caminho