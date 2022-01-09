from unittest import TestCase

from tree import *

class TestTree(TestCase):
    def test_create_tree(self):
        tree = Tree()
        self.assertIsNone(tree.getRoot())