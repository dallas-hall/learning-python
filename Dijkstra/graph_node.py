class GraphNode:

	# Constructor
	def __init__(self, name):
		self.name = name
		self.connected_nodes = {}

	# String representation
	def __str__(self):
		return str(self.__dict__)

	# Object representation - https://stackoverflow.com/a/23851642
	def __repr__(self):
		from pprint import pformat
		return pformat(vars(self), indent=2, width=1)

	# JSON representation
	def toJson(self):
		import json
		return json.dumps(self, default=lambda o: o.__dict__)

	def get_name(self):
		return self.name

	def get_node(self, name):
		return self.connected_nodes[name]

	def get_connected_nodes(self):
		return self.connected_nodes

	def set_connected_node(self, name, cost):
		self.connected_nodes[name] = {
			'cost': cost
		}
