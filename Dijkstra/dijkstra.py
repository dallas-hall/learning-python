#!/bin/python3
import logging
import os
import pprint
import sys
import time

from graph_node import GraphNode

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
start_graph = {
	'A': [('B', 1), ('C', 4)],
	'B': [('A', 1), ('C', 1), ('D', 9), ('G', 2), ('H', 10)],
	'C': [('A', 4), ('B', 1), ('D', 7), ('E', 3)],
	'D': [('B', 9), ('C', 7), ('E', 5), ('F', 2), ('G', 4)],
	'E': [('C', 3), ('D', 5), ('F', 1)],
	'F': [('D', 2), ('E', 1), ('G', 6)],
	'G': [('B', 2), ('D', 4), ('F', 6), ('H', 8)],
	'H': [('B', 10), ('G', 8)]
}

nodes = {}
travel_start_node = 'G'
travel_end_node = 'E'
visited_vertices = ()
current_path = ''
allowed_hops = 1


def create_graph_nodes():
	# Create the graph nodes using ASCII numbers
	for c in range(ord('A'), ord('I')):
		nodes[chr(c)] = GraphNode(chr(c))


def create_graph_edges():
	for c in range(ord('A'), ord('I')):
		node = nodes[chr(c)]
		# Get the edge nodes
		for e in range(len(start_graph.get(chr(c)))):
			# 0 = name
			# 1 = node pointer
			# 2 = cost
			node.set_connected_node(
				start_graph.get(chr(c))[e][0],
				nodes.get(start_graph.get(chr(c))[e][0]),
				start_graph.get(chr(c))[e][1]
			)
		if debugging:
			print(nodes.get(chr(c)).get_name() + " is " + str(nodes.get(chr(c))))
			pprint.pprint(nodes.get(chr(c)).get_connected_nodes())


create_graph_nodes()
create_graph_edges()

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
#   c) Create the next line and calculate L(n) and the paths for all directly connected nodes, excluding the current path. Only cheaper paths are updated.
# 3) Repeat 2 until finished.

