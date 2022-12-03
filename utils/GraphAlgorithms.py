import queue
from classes import Path


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
