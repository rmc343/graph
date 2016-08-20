#==============================================================
# Class: Node
# Author: Ryan Cunningham
# Date: 8/20/2016
# Description: A basic graph node containing the nodes value
# weight and linked node
#==============================================================

class Node:
# ========================================================
# Constructor
# ========================================================
    def __init__(self,val,weight):
        self.weight = weight
        self.val = val
        self.node = None
        self.status = 0
#========================================================
# Getters and Setters
#========================================================
    def get_val(self):
        return self.val
    def get_weight(self):
        return self.weight
    def get_next(self):
        return self.node
    def set_next(self,val,weight):
        node = Node(val,weight)
        self.node = node
    def get_status(self):
        return self.status
    def get_last(self):
        node = self
        while(node.get_next() != None):
            node = node.get_next()
        return node
#========================================================
#Public functions
#========================================================
    def add(self,val,weight):
        node = self.get_last()
        node.set_next(val,weight)

    def print_node(self):
        print(self.getVal())
        node = self
        while (node.getNext() != None):
            node = node.getNext()
            print(node.getVal())
        print()






