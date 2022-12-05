import queue
from collections import defaultdict
from classes import Path
import sys


def NodeInGraph(graph, node):
    return any(path.source == node or path.target == node for path in graph.path)


def BreadthFirstSearch(graph, startingNode):
    """
    Dado un nodo como entrada, devuelve el recorrido realizado por la búsqueda en amplitud partiendo de dicho nodo.

    Si el nodo no existe, retorna una lista vacía.

    Hay casos borde donde el generador de grafos crea edges inexistentes y hay que revisar bien el archivo.

    :param graph: graph
    :param startingNode: string
    :return: list
    """

    bfsPath = []
    visitingQueue = queue.Queue()

    if not NodeInGraph(graph, startingNode):
        return bfsPath

    bfsPath.append(startingNode)
    visitingQueue.put(startingNode)

    while visitingQueue.qsize() != 0:
        currentSource = visitingQueue.get()
        for path in graph.path:
            # Esto lo hago porque el graphml lo toma como dirigido siempre (tiene source y target)
            # Hago un swap auxiliar de source y target para que no piense que no hay conexión.
            # Ej.: si empiezo desde 0, y hay un camino 4 -> 0, que no lo pase de largo y lo ponga en la lista igual.
            auxPath = Path.Path(path.target, path.source) if path.target == currentSource else path

            if (auxPath.source == currentSource) \
                    and auxPath.target not in visitingQueue.queue \
                    and auxPath.target not in bfsPath:

                visitingQueue.put(auxPath.target)

                if auxPath.target not in bfsPath:
                    bfsPath.append(auxPath.target)

    return bfsPath


def DepthFirstSearch(graph, startingNode):
    """
    Dado un nodo como entrada, devuelve el recorrido realizado por la búsqueda en profundidad partiendo de dicho nodo.

    Si el nodo no existe, devuelve una lista vacía.

    :param graph: graph
    :param startingNode: startingNode
    :return: list
    """

    dfsPath = []
    stack = []

    if not NodeInGraph(graph, startingNode):
        return dfsPath

    stack.append(startingNode)

    while len(stack) != 0:
        currentSource = stack.pop()
        stopSearching = False

        for path in graph.path:
            if stopSearching:
                break

            auxPath = Path.Path(path.target, path.source) if path.target == currentSource else path

            if auxPath.source == currentSource and auxPath.target not in dfsPath:
                stack.append(currentSource)
                stack.append(auxPath.target)
                stopSearching = False

        if currentSource not in dfsPath:
            dfsPath.append(currentSource)

    return dfsPath


def GetConnectedComponents(graph):
    """
    Dado un grafo, devolver una lista de nodos.

    Cada sub lista representa una componente conexa del grafo.

    :param graph: graph
    :return: list
    """
    connectedComponents = []
    visited = []

    for path in graph.path:
        if path.source not in visited:
            bfsPath = BreadthFirstSearch(graph, path.source)
            connectedComponents.append(bfsPath)
            visited = [*visited, *bfsPath]

    return connectedComponents


def GetIsConnected(graph):
    """
     Dado un grafo, se devuelve True si el grafo es conexo.

     :param graph: graph
     :return: boolean
     """
    return False if len(GetConnectedComponents(graph)) > 1 else True


def GetConnectedComponentsAmount(graph):
    """
     Dado un grafo, retorna la cantidad de componentes conexas que lo componen

     :param graph: graph
     :return: boolean
     """
    return len(GetConnectedComponents(graph))

def GetNodeAdjacencies(graph, node):
    """
        Devuelve las adyacencias de un nodo en un grafo.

        :param graph: graph
        :param node: string
        :return: list
    """

    adjacencies = []
    for path in graph.path:
        auxPath = Path.Path(path.target, path.source) if path.target == node else path

        if auxPath.target == node and auxPath.target not in adjacencies:
            adjacencies.append(auxPath.source)

        if auxPath.source == node and auxPath.source not in adjacencies:
            adjacencies.append(auxPath.target)

    return adjacencies


def asInt(number):
    try:
        return int(number), ''
    except ValueError:
        return sys.maxint, number


def GetOrderedAdjacenciesList(graph):
    """
    Obtengo una lista de adyacencias

    :param graph: graph
    :return: dictionary
    """
    adjacencyList = {}
    for path in graph.path:
        if path.target not in adjacencyList:
            adjacencyList[path.target] = GetNodeAdjacencies(graph, path.target)

        if path.source not in adjacencyList:
            adjacencyList[path.source] = GetNodeAdjacencies(graph, path.source)

    # Hago esto por las dudas porque no vienen en orden
    return {k: adjacencyList[k] for k in sorted(adjacencyList, key=asInt)}


def BFSShortestPath(adjacencyList, startingNode, destinationNode):
    """
        Variante de BFS para obtener listas el camino más corto.

        :param adjacencyList: list
        :param startingNode: string
        :param destinationNode: string
        :return: list
 
 material de referencia:

        https://www.baeldung.com/cs/graph-number-of-shortest-paths
        https://www.geeksforgeeks.org/print-all-shortest-paths-between-given-source-and-destination-in-an-undirected-graph/

    """

    distances = defaultdict(lambda: float('inf'))
    paths = {}
    visitingQueue = queue.Queue()

    for source in adjacencyList.keys():
        paths[source] = []

    distances[startingNode] = 0
    paths = defaultdict(list)
    paths[startingNode] = [startingNode]

    visitingQueue.put(startingNode)

    while visitingQueue.qsize() != 0:
        currentSource = visitingQueue.get()
        if currentSource == destinationNode:
            break

        for target in adjacencyList[currentSource]:
            if distances[target] == float('inf'):
                distances[target] = distances[currentSource] + 1
                paths[target] = paths[currentSource] + [target]
                visitingQueue.put(target)

    return paths[destinationNode]


def GetShortestPath(graph, startingNode, destinationNode):
    """
    Obtengo el primer camino más cortos posible

    :param graph: graph
    :param startingNode: string
    :param destinationNode: string
    :return: list
    """

    return [] if not NodeInGraph(graph, startingNode) or not NodeInGraph(graph, destinationNode) \
        else BFSShortestPath(GetOrderedAdjacenciesList(graph), startingNode, destinationNode)


def GetShortestPathLength(graph, startingNode, destinationNode):
    """
    Retorno el largo del camino más corto entre dos nodos

    :param graph: graph
    :param startingNode: string
    :param destinationNode: string
    :return: number
    """

    return len(GetShortestPath(graph, startingNode, destinationNode))


def CompareShortestPaths(graph, path):
    """
        Retorna si el camino indicado es el más corto

        :param graph: graph
        :param path: list
        :return: boolean
    """

    if len(path) < 2:
        return False

    startingNode = path[0]
    destinationNode = path[-1]

    if not NodeInGraph(graph, startingNode) or not NodeInGraph(graph, destinationNode):
        return False

    adjacencyList = GetOrderedAdjacenciesList(graph)
    shortestPathLength = GetShortestPathLength(graph, startingNode, destinationNode)
    maxIndex = len(path)
    pathLength = 1
    nodeNotAdjacent = False

    for x in range(0, maxIndex):
        if nodeNotAdjacent:
            break

        node = path[x]
        nextNode = path[x+1] if x != maxIndex-1 else -1

        if nextNode in adjacencyList[node] and nextNode != -1:
            pathLength = pathLength + 1
        elif nextNode != -1:
            nodeNotAdjacent = True

    return False if nodeNotAdjacent else pathLength == shortestPathLength



