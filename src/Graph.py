from Node import *
#==============================================================
# Class: Graph
# Author: Ryan Cunningham
# Date: 8/20/2016
# Description: A basic graph that supports all basic graph
# functionality. The graph is created from a txt file
#==============================================================

class Graph:
#========================================================
# Constructor
#========================================================
    def __init__(self, file):
        self.matrix = []
        self.linked_list = []
#========================================================
# Public Functions
#========================================================
    def create_graph(self, file):
        count = 1
        matrix = []
        linked_list = []
        with open(file) as f:
            for line in f:
                line = line.split()
                if count == 1:
                    numNodes = int(line[0])
                    for i in range(0, numNodes):
                        new = []
                        matrix.append(new)
                        linked_list.append(Node(i,float(0)))
                        for j in range(0, numNodes):
                            new.append(float("inf"))
                    count = 2
                else:
                    val = int(line[0])
                    node = int(line[1])
                    weight = float(line[2])
                    matrix[val][val] = float(0)
                    matrix[val][node] = weight

        self.linked_list = linked_list
        self.matrix = matrix



