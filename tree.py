#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

    def insertLeft(self, node):
        self.l = node

    def getLeft(self):
        return self.l

    def insertRight(self, node):
        self.r = node

    def getRight(self):
        return self.r

    def getValue(self):
        return self.v

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.getValue():
            if node.getLeft() is not None:
                self._add(val, node.getLeft())
            else:
                node.insertLeft(Node(val))
        else:
            if node.getRight() is not None:
                self._add(val, node.getRight())
            else:
                node.insertRight(Node(val))

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.getValue():
            return node
        elif (val < node.getValue() and node.getLeft() is not None):
            return self._find(val, node.getLeft())
        elif (val > node.getValue() and node.getRight() is not None):
            return self._find(val, node.getRight())

    def deleteTree(self):
        self.root = None