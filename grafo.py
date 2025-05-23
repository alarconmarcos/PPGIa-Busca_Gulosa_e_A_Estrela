import networkx as nx

# Cria um objeto de grafo não direcionado
grafo = nx.Graph()

# Adiciona nós ao grafo
grafo.add_node("Arad")
grafo.add_node("Bucharest")
grafo.add_node("Craiova")
grafo.add_node("Drobeta")
grafo.add_node("Eforie")
grafo.add_node("Fagaras")
grafo.add_node("Giurgiu")
grafo.add_node("Hirsova")
grafo.add_node("Iasi")
grafo.add_node("Lugoj")
grafo.add_node("Mehadia")
grafo.add_node("Neamt")
grafo.add_node("Oradea")
grafo.add_node("Pitesti")
grafo.add_node("RimnicuVilcea")
grafo.add_node("Sibiu")
grafo.add_node("Timisoara")
grafo.add_node("Urziceni")
grafo.add_node("Vaslui")
grafo.add_node("Zerind")

# Adiciona arestas com valores ao grafo
grafo.add_edge("Arad", "Zerind", weight=75)
grafo.add_edge("Arad", "Timisoara", weight=118)
grafo.add_edge("Arad", "Sibiu", weight=140)

grafo.add_edge("Bucharest", "Urziceni", weight=85)
grafo.add_edge("Bucharest", "Fagaras", weight=211)
grafo.add_edge("Bucharest", "Pitesti", weight=101)
grafo.add_edge("Bucharest", "Giurgiu", weight=90)

grafo.add_edge("Craiova", "Pitesti", weight=138)
grafo.add_edge("Craiova", "RimnicuVilcea", weight=146)
grafo.add_edge("Craiova", "Drobeta", weight=120)

grafo.add_edge("Drobeta", "Mehadia", weight=75)
grafo.add_edge("Drobeta", "Craiova", weight=120)

grafo.add_edge("Eforie", "Hirsova", weight=86)

grafo.add_edge("Fagaras", "Sibiu", weight=99)
grafo.add_edge("Fagaras", "Bucharest", weight=211)

grafo.add_edge("Giurgiu", "Bucharest", weight=90)

grafo.add_edge("Hirsova", "Eforie", weight=86)
grafo.add_edge("Hirsova", "Urziceni", weight=98)

grafo.add_edge("Iasi", "Vaslui", weight=92)
grafo.add_edge("Iasi", "Neamt", weight=87)

grafo.add_edge("Lugoj", "Mehadia", weight=70)
grafo.add_edge("Lugoj", "Timisoara", weight=111)

grafo.add_edge("Mehadia", "Drobeta", weight=75)
grafo.add_edge("Mehadia", "Lugoj", weight=70)

grafo.add_edge("Neamt", "Iasi", weight=87)

grafo.add_edge("Oradea", "Zerind", weight=71)
grafo.add_edge("Oradea", "Sibiu", weight=151)

grafo.add_edge("Pitesti", "RimnicuVilcea", weight=97)
grafo.add_edge("Pitesti", "Craiova", weight=138)
grafo.add_edge("Pitesti", "Bucharest", weight=101)

grafo.add_edge("RimnicuVilcea", "Pitesti", weight=97)
grafo.add_edge("RimnicuVilcea", "Sibiu", weight=80)
grafo.add_edge("RimnicuVilcea", "Craiova", weight=146)

grafo.add_edge("Sibiu", "Fagaras", weight=99)
grafo.add_edge("Sibiu", "RimnicuVilcea", weight=80)
grafo.add_edge("Sibiu", "Arad", weight=140)
grafo.add_edge("Sibiu", "Oradea", weight=151)

grafo.add_edge("Timisoara", "Lugoj", weight=111)
grafo.add_edge("Timisoara", "Arad", weight=118)

grafo.add_edge("Urziceni", "Hirsova", weight=98)
grafo.add_edge("Urziceni", "Bucharest", weight=85)
grafo.add_edge("Urziceni", "Vaslui", weight=142)

grafo.add_edge("Vaslui", "Iasi", weight=92)
grafo.add_edge("Vaslui", "Urziceni", weight=142)

grafo.add_edge("Oradea", "Sibiu", weight=151)
grafo.add_edge("Oradea", "Zerind", weight=71)

grafo.add_edge("Zerind", "Oradea", weight=71)
grafo.add_edge("Zerind", "Arad", weight=75)

# Distâncias em linha reta (heurísticas) 
dist = {
  "Arad": 366,
  "Bucharest": 0,
  "Craiova": 160,
  "Drobeta": 242,
  "Eforie": 161,
  "Fagaras": 176,
  "Giurgiu": 77,
  "Hirsova": 151,
  "Iasi": 226,
  "Lugoj": 244,
  "Mehadia": 241,
  "Neamt": 234,
  "Oradea": 380,
  "Pitesti": 100,
  "RimnicuVilcea": 193,
  "Sibiu": 253,
  "Timisoara": 329,
  "Urziceni": 80,
  "Vaslui": 199,
  "Zerind": 374
}
