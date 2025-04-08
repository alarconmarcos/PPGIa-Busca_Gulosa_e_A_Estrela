import grafo as busca
import busca_gulosa as gs
import busca_a_estrela as star
import matplotlib.pyplot as plt


def cabecalho():
        print("================================================================================")
        print("\n")
        print("Lista de Cidades:")
        print("\n")
        print("Arad, Bucharest, Craiova, Drobeta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia, \nNeamt, Oradea, Pitesti, RimnicuVilcea, Sibiu, Timisoara, Urziceni, Vaslui e Zerind")
        print("\n================================================================================")
        print("\n")
    

while True:
    print("================================")
    print("\nEscolha uma opção:")
    print("\n1. Busca Gulosa")
    print("2. Busca A*")
    print("3. Exibir gráfico")
    print("0. Sair\n")
    print("================================\n") 

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        
        cabecalho()
        
        # Executa o algoritmo guloso
        cidade_origem = input("Digite a cidade de origem: ")
        
        resultado1 = gs.gulosa(busca.grafo, cidade_origem)

        print("\n================================")
        print("     Algoritmo Busca Gulosa     ")
        print("================================\n")

        distancia_total = 0  # Inicializa a distância total

        for i in range(len(resultado1) - 1):  # Itera até o penúltimo elemento
            cidade_atual = resultado1[i]
            proxima_cidade = resultado1[i + 1]
  
            # Verifica se a aresta existe no grafo
            if busca.grafo.has_edge(cidade_atual, proxima_cidade):
                distancia = busca.grafo[cidade_atual][proxima_cidade]['weight']
                distancia_total += distancia  # Adiciona a distância à distância total
                print(cidade_atual + " -> " + proxima_cidade + " : " + str(distancia))  # Imprime a distância entre as cidades
            else:
                print(f"Não há aresta entre {cidade_atual} e {proxima_cidade}")

        print("\nDistância total:", distancia_total)  # Imprime a distância total    
        print("\n")    
        print("======================================================================\n")
    elif opcao == '2':

        cabecalho()
        
        cidade_origem = input("Digite a cidade de origem: ")

        resultado2 = star.a_estrela(busca.grafo, cidade_origem)

        print("\n================================")
        print("         Algoritmo A*           ")
        print("================================\n")
    

        distancia_total = 0  # Inicializa a distância total

        for i in range(len(resultado2) - 1):  # Itera até o penúltimo elemento
            cidade_atual = resultado2[i]
            proxima_cidade = resultado2[i + 1]
  
            # Verifica se a aresta existe no grafo
            if busca.grafo.has_edge(cidade_atual, proxima_cidade):
                distancia = busca.grafo[cidade_atual][proxima_cidade]['weight']
                distancia_total += distancia  # Adiciona a distância à distância total
                print(cidade_atual + " -> " + proxima_cidade + " : " + str(distancia))  # Imprime a distância entre as cidades
            else:
                print(f"Não há aresta entre {cidade_atual} e {proxima_cidade}")

        print("\nDistância total:", distancia_total)  # Imprime a distância total


    elif opcao == '3':
        #Plota o grafo
        plt.figure(figsize=(10, 10))
        pos = busca.nx.spring_layout(busca.grafo)
        labels = busca.nx.get_edge_attributes(busca.grafo, 'weight')
        busca.nx.draw_networkx_nodes(busca.grafo, pos)
        busca.nx.draw_networkx_edges(busca.grafo, pos)
        busca.nx.draw_networkx_labels(busca.grafo, pos)
        busca.nx.draw_networkx_edge_labels(busca.grafo, pos, edge_labels=labels)
        plt.title("Grafo de Cidades")

        # Se o resultado1 ou resultado2 estiverem disponíveis, exiba o caminho correspondente
        if 'resultado1' in locals():
            caminho1 = resultado1
        else:
            caminho1 = []
        if 'resultado2' in locals():
            caminho2 = resultado2
        else:
            caminho2 = []

        if caminho1:
            caminho_pos = [pos[cidade] for cidade in caminho1]
            plt.plot(*zip(*caminho_pos), color='red', linewidth=2, label='Gulosa')
            plt.legend()
        
        if caminho2:
            caminho_pos = [pos[cidade] for cidade in caminho2]
            plt.plot(*zip(*caminho_pos), color='blue', linewidth=2, label='A*')
            plt.legend()

  
        plt.show()

    elif opcao == '0':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")