import os
import xmltodict
import json


def GetGraphs():
    print("Loading graphs...")
    graphs = []
    graphsLocation = "./graphs"
    graphFiles = os.listdir(graphsLocation)

    for graphFile in graphFiles:
        file = open(f"{graphsLocation}/{graphFile}", "r")
        fileContent = file.read()
        # Parsing
        jsonObject = json.loads(json.dumps(xmltodict.parse(fileContent)))
        # End Parsing
        graphs.append(jsonObject)
        file.close()

    print("Graphs loaded")
    return graphs
