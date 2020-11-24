class GraphNode:

	# Constructor
	def __init__(self, name):
		self.name = name
		self.connected_nodes = {}

	def get_name(self):
		return self.name

	def get_node(self, name):
		return self.connected_nodes[name]

	def get_connected_nodes(self):
		return self.connected_nodes

	def set_connected_node(self, name, node, cost):
		node_link = {
			"node": node,
			"cost": cost
		}
		self.connected_nodes[name] = node_link
