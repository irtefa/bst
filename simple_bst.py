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

if __name__ == "__main__":
	simple_bst = SimpleBst()

	root = simple_bst.insert(None, 10)
	for i in [5, 15, 1, 7, 12, 20]:
		simple_bst.insert(root, i)
	print "A balanced tree:"
	simple_bst.level_order(root)

	root = simple_bst.insert(None, 10)
	insert_these = [20, 5, 15, 22, 1, 7, 6, 23, 25, 30]
	for i in insert_these:
		simple_bst.insert(root, i)

	print "A sparse tree which is heavier on the right:"
	simple_bst.level_order(root)


	root = simple_bst.insert(None, 15)
	for i in [12,11,10,9,8,1]:
		simple_bst.insert(root, i)

	print "A sparse tree which is heavier on the left:"
	simple_bst.level_order(root)
