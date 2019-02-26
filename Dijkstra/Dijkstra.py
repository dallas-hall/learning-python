#!/bin/python3
import logging, time, math, pprint, collections

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
logging.info('Dijkstra Using Adjacency List.')
time.sleep(.004)

debugging = True

# https://www.tutorialspoint.com/data_structures_algorithms/graph_data_structure.htm
# Graph vertices. This graph is directed as there is only one edge between vertices.
complete_graph = {
	'A': [('B', 1), ('C', 2)],
	'B': [('A', 1), ('D', 3)],
	'C': [('A', 2), ('D', 5), ('F', 1)],
	'D': [('B', 3), ('C', 5), ('F', 2), ('G', 7)],
	'E': [('F', 1), ('G', 1)],
	'F': [('C', 1), ('D', 2), ('E', 1)],
	'G': [('D', 7), ('E', 1), ('F', 1)]
}

start_vertex = 'A'
end_vertex = 'G'
visited_vertices = ()
current_path = ''
allowed_hops = 1

# A is the starting node so isn't represented here.
# Structure is [iteration number, current path, current cost].
# All paths are set to None and infinity when not directly connected.


def create_dijkstra_table(vertex):
	global least_cost_path
	least_cost_path = {}

	for key in complete_graph.keys():
		if key != start_vertex:
			least_cost_path[key] = [0, None, math.inf]



def get_vertex_and_nearest_neighbours(vertex):
	for key, value in complete_graph.items():
		if vertex.upper() == key:
			return value


def get_vertex_nearest_neighbours_path_and_cost(vertex):
	vertex_and_neighbours = get_vertex_and_nearest_neighbours(vertex)
	path_list = []
	for i in range(len(vertex_and_neighbours)):
		path_list.append([vertex + '-' + vertex_and_neighbours[i][0], vertex_and_neighbours[i][1]])
	return path_list



create_dijkstra_table(start_vertex)
if debugging:
	logging.debug('Graph adjacency list.')
	time.sleep(.004)
	pprint.pprint(complete_graph)
	logging.debug('Dijkstra Least Cost Path table setup.')
	time.sleep(.004)
	pprint.pprint(least_cost_path)


print(get_vertex_and_nearest_neighbours(start_vertex))
print(get_vertex_nearest_neighbours_path_and_cost(start_vertex))
# TODO - dijkstra.
"""


first iteration, A to directly connected neighbours. Store all paths.
second iteration, A to directly connected nieghbours to their directly connected neighbours. Store new paths and compare against previous paths, updating if better.
finish at 4 iterations.
"""
if debugging:
	logging.debug('Dijkstra Least Cost Path Algorithm Start.')
	time.sleep(.004)
i = 1
next_vertex = ''
processed_vertices_set = set(start_vertex)
while True:
	if i == 1:
		neighbours = get_vertex_and_nearest_neighbours(start_vertex)
		for j in range(len(neighbours)):
			least_cost_path[neighbours[j][0]] = [i, start_vertex + '-' + neighbours[j][0], neighbours[j][1]]
			processed_vertices_set.add(neighbours[j][0])
		next_vertex = chr(ord(start_vertex) + 1)
		processed_vertices_set = sorted(processed_vertices_set)
		if debugging:
			logging.debug('Iteration ' + str(i))
			time.sleep(.004)
			print('neighbours:')
			pprint.pprint(neighbours)
			print('least_cost_path:')
			pprint.pprint(least_cost_path)
			print('processed_vertices_set:')
			pprint.pprint(processed_vertices_set)
			print('i: ' + str(i))
			print('next_vertex: ' + next_vertex)
			time.sleep(.004)
		i += 1
	else:
		break
