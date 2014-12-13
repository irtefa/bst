import unittest
from simple_bst import SimpleBst


class AssertSimpleBstTest(unittest.TestCase):
	# We may initialize this with something in the future
	def setUp(self):
		# Creates empty Simple Bst
		self.simple_bst = SimpleBst()


class WhenSimpleBstIsEmpty(AssertSimpleBstTest):

	# When we search for a key in empty SimpleBst, it should return None
	def test_should_return_none(self):
		self.assertEqual(None, self.simple_bst.find(None, 2))


class WhenInsertedAnElement(AssertSimpleBstTest):

	# When inserted a Node containing value 2, it should return the Node with value 2
	def test_should_return_inserted_key(self):
		root = self.simple_bst.insert(None, 2)

		self.assertEqual(2, self.simple_bst.find(root, 2).val)

	# When inserted multiple nodes, it should be able to find a give node
	def test_should_return_inserted_key_when_multiple_keys_are_inserted(self):
		root = self.simple_bst.insert(None, 10)
		self.simple_bst.insert(root, 5)
		self.simple_bst.insert(root, 15)

		self.assertEqual(5, self.simple_bst.find(root, 5).val)

	# When inserted a Node, it should return a depth of 1
	def test_should_return_correct_depth(self):
		root = self.simple_bst.insert(None, 1)

		self.assertEqual(2, self.simple_bst.depth(root))

	# When inserted multiple nodes, it should return the appropriate depth
	def test_should_return_correct_depth(self):
		root = self.simple_bst.insert(None, 10)
		self.simple_bst.insert(root, 5)
		self.simple_bst.insert(root, 15)
		self.simple_bst.insert(root, 16)
		self.simple_bst.insert(root, 17)
		self.simple_bst.insert(root, 18)
		self.simple_bst.insert(root, 19)
		self.simple_bst.insert(root, 20)

		self.assertEqual(7, self.simple_bst.depth(root))

if __name__ == '__main__':
    unittest.main()