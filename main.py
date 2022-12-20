import random
import string
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name):
        self.name = name  # Add a name attribute to identify each node
        self.firing_threshold = random.uniform(0, 1)  # Set firing threshold to a random number between 0 and 1
        self.firing_sequence = []
        self.connections = []  # Add an attribute to store the connections for each node
        self.connected_nodes = []  # Add an attribute to store the connected nodes for each connection

    def fire(self, current_input):
        if current_input > self.firing_threshold:
            self.firing_sequence.append(1)
        else:
            self.firing_sequence.append(0)

    def add_connection(self, connection, node):
        self.connections.append(connection)  # Add a connection to the list of connections for the node
        self.connected_nodes.append(node)  # Add the connected node to the list of connected nodes for the connection

    def print_connections(self):
        print(f"Node {self.name} connections:")
        for i, (connection, node) in enumerate(zip(self.connections, self.connected_nodes)):
            print(f"{i+1}. Strength: {connection.strength}, Delay: {connection.delay}, Connected node: {node.name}")  # Print the strength, delay, and connected node for each connection

class Connection:
    def __init__(self, strength, delay):
        self.strength = strength
        self.delay = delay

    def strengthen(self):
        self.strength += 1

class Network:
    def __init__(self, start, end, memory):
        self.start = start
        self.end = end
        self.memory = memory

def create_network(nodes, connections):
    # Select a random start and end node
    start = random.choice(nodes)
    end = random.choice(nodes)
    while end == start:
        end = random.choice(nodes)

    # Create a random set of connections between the nodes
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if random.random() < 0.5:  # 50% chance of creating a connection between each pair of nodes
                connections.append(Connection(1, 0))
                nodes[i].add_connection(connections[-1], nodes[j])  # Add the connection and connected node to the node's list of connections
                nodes[j].add_connection(connections[-1], nodes[i])  # Add the connection and connected node to the node's list of connections

    # Create a network with the selected start and end nodes, and a random memory
    memory = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    network = Network(start, end, memory)
    return network

# Create a list of 10 nodes with randomly generated firing thresholds and names
nodes = [Node(f"Node {i+1}") for i in range(10)]

# Create an empty list of connections
connections = []

# Create a network with the randomly generated structure and connection pattern
network = create_network(nodes, connections)

# # Print the connections for each node
# for node in nodes:
#     node.print_connections()



# Create an empty graph
G = nx.Graph()

# Add the nodes to the graph
for node in nodes:
    G.add_node(node.name)

# Add the connections to the graph
for node in nodes:
    for connection, connected_node in zip(node.connections, node.connected_nodes):
        G.add_edge(node.name, connected_node.name, weight=connection.strength)

# Draw the graph
nx.draw(G, with_labels=True)
