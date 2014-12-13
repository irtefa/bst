import unittest
from abstract_bst import AbstractBst


class AssertAbstractBstTest(unittest.TestCase):
	# We may initialize this with something in the future
	def setUp(self):
		pass

class WhenAbstractMethodsNotInitiated(AssertAbstractBstTest):

	# Abstract class should raise a TypeError as it is instantiated with an abstract method
	def test_should_raise_type_error(self):
		self.assertRaises(TypeError, AbstractBst)

if __name__ == '__main__':
    unittest.main()
