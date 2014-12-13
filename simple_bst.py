from abstract_bst import AbstractBst

class SimpleBst(AbstractBst):


	# A simple compare method for integers
	# @given_val: The value we are inserting or looking for
	# @current_val: Value at the current node in our traversal
	# returns an integer where
	# -1: given_val is less than current_val
	#  1: given_val is greater than current_val
	#  0: given_val and current_val are equal
	def compare(self, given_val, current_val):
		if given_val < current_val:
			return -1
		elif given_val > current_val:
			return 1
		return 0
