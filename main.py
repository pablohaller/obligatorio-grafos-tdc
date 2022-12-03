from classes import AvailableGraphs
from utils import Utils, GraphAlgorithms

print('Obligatorio TDC\n')

availableGraphs = AvailableGraphs.AvailableGraphs(Utils.GetGraphs())

for graph in availableGraphs.graphs:
    print(graph)
    print("BFS(0)", GraphAlgorithms.BreadthFirstSearch(graph, "0"))
    print("DFS(0)", GraphAlgorithms.DepthFirstSearch(graph, "0"))
    print("-------------------------")

