import os
import xmltodict
import json
from classes import Path
from classes import Graph


def GetGraphs():
    print("Loading graphs...")
    graphList = []
    graphsLocation = "./graphs"
    graphFiles = os.listdir(graphsLocation)

    for graphFile in graphFiles:
        graphPath = []
        file = open(f"{graphsLocation}/{graphFile}", "r")
        fileContent = file.read()
        graphDictionary = json.loads(json.dumps(xmltodict.parse(fileContent)))

        for key, value in graphDictionary["graphml"]["graph"].items():
            if key == "edge":
                for edge in value:
                    graphPath.append(Path.Path(edge["@source"], edge["@target"]))

        graphList.append(Graph.Graph(graphFile, graphPath))
        file.close()

    print("Graphs loaded...")
    return graphList
