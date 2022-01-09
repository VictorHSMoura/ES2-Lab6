from unittest import TestCase

from tree import *

class TestTree(TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_create_tree(self):
        self.assertIsNone(self.tree.getRoot())

    def test_add_root(self):
        self.tree.add(3)

        self.assertIsNotNone(self.tree.getRoot())
        self.assertEqual(self.tree.getRoot().getValue(), 3)

    def test_add_left(self):
        self.tree.add(3)
        self.tree.add(1)

        root = self.tree.getRoot()

        self.assertIsNotNone(root.getLeft())
        self.assertEqual(root.getLeft().getValue(), 1)

    def test_add_right(self):
        self.tree.add(3)
        self.tree.add(5)

        root = self.tree.getRoot()
        self.assertIsNotNone(root.getRight())
        self.assertEqual(root.getRight().getValue(), 5)
