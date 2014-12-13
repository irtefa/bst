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

if __name__ == '__main__':
    unittest.main()