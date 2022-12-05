import queue
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
            auxPath = Path.Path(path.target, path.source, path.weight) if path.target == currentSource else path

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

            auxPath = Path.Path(path.target, path.source, path.weight) if path.target == currentSource else path

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


def GetNodeAdjacencies(graph, node):
    """
        Devuelve las adyacencias de un nodo en un grafo.

        :param graph: graph
        :param node: string
        :return: list
    """

    adjacencies = []
    for path in graph.path:
        auxPath = Path.Path(path.target, path.source, path.weight) if path.target == node else path

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


def FindPaths(finalPaths, newPath, sortedPaths, startingNode, destinationNode) -> None:
    # Base Case
    if destinationNode == "0":
        finalPaths.append(newPath.copy())
        return

    # Loop for all the parents
    # of the given vertex
    for path in sortedPaths[destinationNode]:
        # Insert the current
        # vertex in path
        newPath.append(destinationNode)

        # Recursive call for its parent
        FindPaths(finalPaths, newPath, sortedPaths, startingNode, path)

        # Remove the current vertex
        newPath.pop()


def GetAllShortestPaths(graph, startingNode, destinationNode):
    """
    Obtengo todos los caminos más cortos posibles

    :param graph: graph
    :param startingNode: string
    :param destinationNode: string
    :return: list

    https://www.baeldung.com/cs/graph-number-of-shortest-paths
    https://www.geeksforgeeks.org/print-all-shortest-paths-between-given-source-and-destination-in-an-undirected-graph/
    """

    if not NodeInGraph(graph, startingNode) or not NodeInGraph(graph, destinationNode):
        return []

    placeholder = []
    adjacencyList = {}

    print(graph.name)
    for path in graph.path:
        if path.target not in adjacencyList:
            adjacencyList[path.target] = GetNodeAdjacencies(graph, path.target)

        if path.source not in adjacencyList:
            adjacencyList[path.source] = GetNodeAdjacencies(graph, path.source)

    # Hago esto por las dudas porque no vienen en orden
    distance = {}
    paths = {}
    visited = {}

    for source in adjacencyList.keys():
        distance[source] = 99
        paths[source] = []
        visited[source] = False

    distance[startingNode] = 0

    # BFS
    visitingQueue = queue.Queue()
    visitingQueue.put(startingNode)

    while visitingQueue.qsize() != 0:
        currentSource = visitingQueue.get()
        for adjacent in adjacencyList[currentSource]:

            if distance[adjacent] > distance[currentSource] + 1:
                distance[adjacent] = distance[currentSource] + 1
                visitingQueue.put(adjacent)
                paths[adjacent].clear()
                paths[adjacent].append(currentSource)

            elif distance[adjacent] == distance[currentSource] + 1:
                paths[adjacent].append(currentSource)

    sortedPaths = {k: paths[k] for k in sorted(paths, key=asInt)}

    newPath = []
    finalPaths = []
    FindPaths(finalPaths, newPath,  sortedPaths, len(adjacencyList.keys()), destinationNode)

    for path in finalPaths:
        for node in reversed(path):
            print(node, end=" ")
        print()

    return placeholder
