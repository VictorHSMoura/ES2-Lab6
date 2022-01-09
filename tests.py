from unittest import TestCase

from tree import *

class TestNode(TestCase):
    def setUp(self):
        self.node = Node(5)

    def test_create_node(self):
        self.assertIsNotNone(self.node)
        self.assertEqual(self.node.getValue(), 5)    

    def test_insert_left(self):
        self.node.insertLeft(Node(8))

        self.assertEqual(self.node.getLeft().getValue(), 8)

    def test_insert_right(self):
        self.node.insertRight(Node(45))

        self.assertEqual(self.node.getRight().getValue(), 45)


class TestTree(TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_create_tree(self):
        self.assertIsNone(self.tree.getRoot())

    def test_add_root(self):
        self.tree.add(3)

        self.assertEqual(self.tree.getRoot().getValue(), 3)

    def test_add_left(self):
        self.tree.add(3)
        self.tree.add(1)

        root = self.tree.getRoot()

        self.assertEqual(root.getLeft().getValue(), 1)

    def test_add_right(self):
        self.tree.add(3)
        self.tree.add(5)

        root = self.tree.getRoot()
        self.assertEqual(root.getRight().getValue(), 5)

    def test_find_node(self):
        self.tree.add(3)
        self.tree.add(5)
        self.tree.add(7)

        self.assertIsNotNone(self.tree.find(7))

    def test_not_find_node(self):
        self.tree.add(3)
        self.tree.add(5)
        self.tree.add(7)

        self.assertIsNone(self.tree.find(9))

    def test_delete_tree(self):
        self.tree.add(3)
        self.tree.add(5)
        self.tree.add(7)

        self.assertIsNotNone(self.tree.getRoot())

        self.tree.deleteTree()
        self.assertIsNone(self.tree.getRoot())