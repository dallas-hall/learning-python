#!/bin/python3
import json
import logging
import os
import sys
import time

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
logging.info('Dijkstra Using Adjacency List.')
time.sleep(.010)

# https://www.tutorialspoint.com/data_structures_algorithms/graph_data_structure.htm
# Graph vertices. This graph is directed as there is only one edge between vertices.
graph = {
	'A': [('B', 1), ('C', 4)],
	'B': [('A', 1), ('C', 1), ('D', 9), ('G', 2), ('H', 10)],
	'C': [('A', 4), ('B', 1), ('D', 7), ('E', 3)],
	'D': [('B', 9), ('C', 7), ('E', 5), ('F', 2), ('G', 4)],
	'E': [('C', 3), ('D', 5), ('F', 1)],
	'F': [('D', 2), ('E', 1), ('G', 6)],
	'G': [('B', 2), ('D', 4), ('F', 6), ('H', 8)],
	'H': [('B', 10), ('G', 8)]
}

allowed_hops = 1
start_node = 'A'
end_node = 'H'
dijsktra_output = {
	'start node': 'G',
	'end node': 'E',
	'all nodes': {},
	'visited vertices': ()
}


def create_graph_nodes_and_edges():
	# Create the graph nodes using ASCII numbers
	for c in range(ord('A'), ord('H') + 1):
		dijsktra_output['all nodes'][chr(c)] = {}
		current_node = dijsktra_output['all nodes'][chr(c)]
		current_node['linked nodes'] = {}
		# Get the edge nodes
		for e in range(len(graph.get(chr(c)))):
			# 0 = name
			# 1 = cost
			current_node['linked nodes'][graph.get(chr(c))[e][0]] = {
				'cost': graph.get(chr(c))[e][1]
			}


# 	dijsktra_output['all nodes'][chr(c)]['pointer'].set_connected_node(node)
#
# if debugging:
# 	print(dijsktra_output['all nodes'].get(chr(c)).get_name() + " is " + str(
# 		dijsktra_output['all nodes'].get(chr(c))))
# 	pprint.pprint(dijsktra_output['all nodes'].get(chr(c)).get_connected_nodes())


# Dijkstra formula
#
# s = starting node
# n = number of nodes in the network
# T = the set of nodes the algorithm has used so far
# w(i,j) = the link cost between i and j when directly connected, else infinity
# L(n) = the current known least cost path from s to N
#
# Dijkstra steps
#
# Note: there will be one line per node visited after this algorithm.
#
# 1) Initialisation
#   a) Create a table with the columns T, current cost, and current path for each node. But excluding the start node.
#   b) Update T with start node as we have visited it and it has 0 cost.
#   c) Compute L(n) and current path for each node in the graph, excluding start node. If no connection, cost is infinity and path is null.
# 2) Get next directly connected node
#   a) On the current line, find the next directly connected node that isn't in T and has a least cost path that isn't infinity
#   b) Update T with the current directly connected node from the current line.
#   c) Create the next line in the table and calculate L(n) and the paths for all directly connected nodes, excluding the current path. Only cheaper paths are updated.
# 3) Repeat 2 until finished.
def dijsktra():
	print(json.dumps(dijsktra_output, indent=2))


create_graph_nodes_and_edges()
dijsktra()
