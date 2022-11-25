import queue
from classes import Path


def NodeInGraph(graph, node):
    return any(path.source == node or path.target == node for path in graph.path)


def BreadthFirstSearch(graph, startingNode):
    """Dado un grafo (graph), y un nodo de entrada (startingNode)

    Retorna una lista con el recorrido realizado por la búsqueda en amplitud
    partiendo de dicho nodo para el grafo.

    Si el nodo no existe, retorna una lista vacía
    """
    bfsPath = []
    visitingQueue = queue.Queue()

    if not NodeInGraph(graph, startingNode):
        return bfsPath

    bfsPath.append(startingNode)
    visitingQueue.put(startingNode)
    print("-------------------\n\n")
    print(graph.name)
    print(visitingQueue.queue)

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

        print(visitingQueue.queue)
        print(bfsPath)

    return bfsPath

