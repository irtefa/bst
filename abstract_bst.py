from abc import ABCMeta, abstractmethod
from node import Node

class AbstractBst(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	# The user should implement the compare function as the Tree Node may
	# carry any data type
	def compare(self, a, b):
		pass

	# Inserts a Node containing val into root
	# @root: The node where we are inserting
	# @val: The value of the node that is being inserted
	# returns the root of the tree
	def insert(self, root, val):
		if root == None:
			return Node(val)

		comparator = self.compare(val, root.val)
		if  comparator < 1:
			# Add to the left subtree
			root.left = self.insert(root.left, val)
		else:
			# Add to the right subtree
			root.right = self.insert(root.right, val)

		return root

	def find(self, root, val):
		if root == None:
			return None

		comparator = self.compare(val, root.val)
		# Found the node
		if comparator == 0:
			return root
		# It might be on the left subtree
		elif comparator == -1:
			return self.find(root.left, val)
		# It might be on the right subtree
		return self.find(root.right, val)

