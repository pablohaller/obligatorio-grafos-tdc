from classes import AvailableGraphs
from utils import Utils

print('Obligatorio TDC\n')

availableGraphs = AvailableGraphs.AvailableGraphs(Utils.GetGraphs())

for graph in availableGraphs.graphs:
    print(type(graph))

