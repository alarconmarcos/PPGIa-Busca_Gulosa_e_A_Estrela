import grafo as busca
import busca_gulosa as gs
import busca_a_estrela as star
import matplotlib.pyplot as plt



def Lista_Cidades():
        print("=" * 100+"\n")
        print("Lista de Cidades:")
        print("\n")
        print("Arad, Bucharest, Craiova, Drobeta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia,")
        print("Neamt, Oradea, Pitesti, RimnicuVilcea, Sibiu, Timisoara, Urziceni, Vaslui e Zerind")
        print("\n"+"=" * 100+"\n")

    

while True:

    print("\n"+"=" * 50+"\n")
    print("Escolha uma opção:\n")
    print("1. Busca Gulosa")
    print("2. Busca A*")
    print("3. Exibir gráfico")
    print("0. Sair")
    print("\n"+"=" * 50+"\n")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        
        Lista_Cidades()
        
        # Executa o algoritmo guloso
        cidade_origem = input("Digite a cidade de origem: ")
        
        resultado1 = gs.gulosa(busca.grafo, cidade_origem)

        print("\n"+"=" * 50)
        print(" " * 15+"Algoritmo Busca Gulosa")
        print("=" * 50 +"\n")

        distancia_total_gulosa = 0 # Inicializa a distância total

        for i in range(len(resultado1) - 1): # Itera até o penúltimo elemento
            cidade_atual = resultado1[i]
            proxima_cidade = resultado1[i + 1]
  
            # Verifica se a aresta existe no grafo
            if busca.grafo.has_edge(cidade_atual, proxima_cidade):
                distancia = busca.grafo[cidade_atual][proxima_cidade]['weight']
                distancia_total_gulosa += distancia # Adiciona a distância à distância total
                print(cidade_atual + " -> " + proxima_cidade + " : " + str(distancia)+ " Km")  # Imprime a distância entre as cidades
            else:
                print(f"Não há aresta entre {cidade_atual} e {proxima_cidade}")

        print("\nDistância total: " + str(distancia_total_gulosa) + " Km")  # Imprime a distância total
            
    elif opcao == '2':

        Lista_Cidades()
        
        cidade_origem = input("Digite a cidade de origem: ")

        resultado2 = star.a_estrela(busca.grafo, cidade_origem)

        print("\n"+"=" * 50)
        print(" " * 20+"Algoritmo A*")
        print("=" * 50 +"\n")
    

        distancia_total_astar = 0  # Inicializa a distância total

        for i in range(len(resultado2) - 1):  # Itera até o penúltimo elemento
            cidade_atual = resultado2[i]
            proxima_cidade = resultado2[i + 1]

            # Verifica se a aresta existe no grafo
            if busca.grafo.has_edge(cidade_atual, proxima_cidade):
                distancia = busca.grafo[cidade_atual][proxima_cidade]['weight']
                distancia_total_astar += distancia  # Adiciona a distância à distância total
                print(cidade_atual + " -> " + proxima_cidade + " : " + str(distancia)+ " Km")  # Imprime a distância entre as cidades
            else:
                print(f"Não há aresta entre {cidade_atual} e {proxima_cidade}")

        print("\nDistância total: " + str(distancia_total_astar) + " Km")  # Imprime a distância total

    elif opcao == '3':
        
        plt.figure(figsize=(12, 9))

        # Layout fixo baseado no mapa original
        pos = {
            "Oradea": (260, 110),
            "Zerind": (220, 160),
            "Arad": (200, 220),
            "Timisoara": (200, 300),
            "Lugoj": (260, 340),
            "Mehadia": (270, 400),
            "Drobeta": (270, 470),
            "Sibiu": (300, 190),
            "RimnicuVilcea": (370, 260),
            "Fagaras": (390, 150),
            "Craiova": (370, 370),
            "Pitesti": (450, 300),
            "Bucharest": (520, 360),
            "Giurgiu": (520, 420),
            "Urziceni": (600, 300),
            "Hirsova": (680, 300),
            "Eforie": (740, 340),
            "Vaslui": (620, 200),
            "Iasi": (600, 130),
            "Neamt": (560, 90)
        }

        # Rótulos das arestas
        labels = busca.nx.get_edge_attributes(busca.grafo, 'weight')

        # Desenha os elementos do grafo
        busca.nx.draw_networkx_nodes(busca.grafo, pos, node_size=500, node_color='lightblue')
        busca.nx.draw_networkx_edges(busca.grafo, pos)
        busca.nx.draw_networkx_labels(busca.grafo, pos, font_size=8, font_family='sans-serif')
        busca.nx.draw_networkx_edge_labels(busca.grafo, pos, edge_labels=labels, font_size=7)

        plt.title("Grafo de Cidades da Romênia")
       # plt.axis('off')

        # Se o resultado1 ou resultado2 estiverem disponíveis, exiba o caminho correspondente
        if 'resultado1' in locals():
            caminho1 = resultado1
        else:
            caminho1 = []
        if 'resultado2' in locals():
            caminho2 = resultado2
        else:
            caminho2 = []

        if caminho2:
            caminho_pos = [pos[cidade] for cidade in caminho2]
            plt.plot(*zip(*caminho_pos), color='red', linewidth=4, label="A* - "+str(distancia_total_astar)+" km")
            plt.legend()

        if caminho1:
            caminho_pos = [pos[cidade] for cidade in caminho1]
            plt.plot(*zip(*caminho_pos), color='blue', linewidth=2, label="Gulosa - "+str(distancia_total_gulosa)+" km")
            plt.legend()

        plt.tight_layout()
        plt.gca().invert_yaxis()        
        plt.show()

    elif opcao == '0':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
