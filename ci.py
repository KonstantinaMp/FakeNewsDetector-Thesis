#execute python3 ci.py radius
#enter radius value in command line

import sys
import os
import glob
import math
import pandas as pd
import networkx as nx
import time
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})

from maxHeap import *
from heapq_max import *

rad = sys.argv[1]

f = '/relationships/relationships true/1237937081214799872.txt'

def createGraph(file,name):
    nodes = {}
    edges = []
    node_sizes = []

    for line in file: 
        edges.append(tuple(line[:-1].split('\t')))
        source,target = tuple(line[:-1].split('\t'))
        if source not in nodes.keys():
            nodes[source] = 1
        else:
            nodes[source] += 1
        if target not in nodes.keys():      
            nodes[target] = 1
        else:
            nodes[target] += 1
    
    for node in nodes.keys():
        node_sizes.append( 5*nodes[node])
    
    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    
    return (graph,nodes,edges)

def findNodeToRemove(ciValues,maxValue):
    for key, value in ciValues.items():    
        if value == maxValue:
            nodeToRemove = key
            break
    
    return nodeToRemove

def updateCI(graph,radius,ciValues,values,sphere,nodeR):
    for node in sphere[nodeR]:
        ego = nx.ego_graph(graph, node, radius=radius, center=True, undirected=False, distance=None)
        degreeSum = 0
        for i in ego.nodes():
            degreeSum += graph.out_degree(i)
        ciValues[node] = (graph.out_degree(node)-1)*(degreeSum-1)
    
    values=list(ciValues.values())
    return (ciValues, values, sphere)

def normalize(d, target=1.0):
   raw = sum(d.values())
   factor = target/raw 
   
   return {key:value*factor for key,value in d.items()}

def collective_influence(graph,radius):
    ciValues = {}
    sphere = {}
    vector = {}
    values = []
    avg_k = graph.number_of_edges() / graph.number_of_nodes()
    for node in graph.nodes():
        ego = nx.ego_graph(graph, node, radius=radius, center=True, undirected=False, distance=None)
        sphere[node] = [i for i in ego.nodes() if i != node]
        degreeSum = 0
        for i in ego.nodes():
            degreeSum += graph.out_degree(i)
        ciValues[node] = (graph.out_degree(node)-1)*(degreeSum-1)
   
    values=list(ciValues.values())

    while True:
        heap = MaxHeap(len(values)+1) 
        for v in values:
            heap.insert(v) 
        maxValue = heap.popMax()

        nodeToRemove = findNodeToRemove(ciValues,maxValue)
        del ciValues[nodeToRemove]
        vector[nodeToRemove] = maxValue
        for key in sphere.keys():
            if nodeToRemove in sphere[key]:
                sphere[key].remove(nodeToRemove)
        heap = MaxHeap(len(values)+1) 
        ciValues, values, sphere = updateCI(graph,radius,ciValues,values,sphere,nodeToRemove)
        heap = MaxHeap(len(values)+1) 

        sumCI = sum(ciValues.values())
        exp = 1 / (radius+1)
        base = sumCI / graph.number_of_nodes()*avg_k 
        l = math.pow(base, exp)
        if l <= 1: 
            break
   
    return(vector)

def compute_significance(vector): 
    totalValue = 0
    moment_2 = 0
    signVector = {}
    
    if vector: 
        vector = normalize(vector)
    
    for node,value in vector.items():
        if totalValue >= 0.9:
            break
        totalValue += value       
        signVector[node] = value         #node significance ~50%
        moment_2 += math.pow(value,2)
    return(signVector,moment_2)  

========================================================
def drawSignGraph(edges,nodes,signVector,name): 
    node_colors = []
    signEdges = []
    node_sizes = []

    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    
    for node,size in nodes.items():
        if node in signVector.keys():
            node_colors.append('red')
            node_sizes.append(70)
        else:
            node_colors.append('gray')
            node_sizes.append(10)
    if len(signVector) >=2:
        for n1 in signVector.keys():
            for n2 in signVector.keys():
                if n1 != n2:
                    if graph.has_edge(n1,n2):
                        signEdges.append((n1,n2))
                    if graph.has_edge(n2,n1):
                        signEdges.append((n2,n1))
    
        edge_colors = ['red' if e in signEdges else 'lightgray' for e in graph.edges]
    else:
        edge_colors = ['gray' for e in range(len(graph.edges))]
    plt.figure(figsize=(20,10))
    nx.draw(graph, node_color=node_colors, edge_color=edge_colors, connectionstyle='arc3', width=0.5, arrowsize=10, node_size = node_sizes)    
    #plt.savefig(name)
    plt.show()
    plt.cla
========================================================

def main():
    radius = int(sys.argv[1])
    file = open(f)
    name=os.path.basename(f).split('.')[0]
    print(name)
    graph, nodes, edges = createGraph(file,name)
    vector = collective_influence(graph,radius)
    signVector,moment_2 = compute_significance(vector)
    drawSignGraph(edges,nodes,signVector,name) 
    print(signVector)
    

if __name__ == '__main__':
    main()
    
