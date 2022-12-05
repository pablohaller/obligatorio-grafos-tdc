from classes import AvailableGraphs
from utils import Utils, GraphAlgorithms

print('Obligatorio TDC\n')

availableGraphs = AvailableGraphs.AvailableGraphs(Utils.GetGraphs())

for graph in availableGraphs.graphs:
    print(graph)
    print("BFS(0):", GraphAlgorithms.BreadthFirstSearch(graph, "0"))
    print("DFS(0):", GraphAlgorithms.DepthFirstSearch(graph, "0"))
    print("Connected Components:", GraphAlgorithms.GetConnectedComponents(graph))
    print("Get is connected:", GraphAlgorithms.GetIsConnected(graph))
    print("Get connected components amount:", GraphAlgorithms.GetConnectedComponentsAmount(graph))
    print("Shortest Path:", GraphAlgorithms.GetShortestPath(graph, "0", "11"))
    print("Shortest Path Length:", GraphAlgorithms.GetShortestPathLength(graph, "0", "11"))
    print("Is Shortest Path?:", GraphAlgorithms.CompareShortestPaths(graph, ['0', '2', '7', '6', '4', '5', '10', '11']))
    print("-------------------------")

