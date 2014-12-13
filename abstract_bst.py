from node import Node
from collections import deque
from abc import ABCMeta, abstractmethod


class AbstractBst(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	# The user should implement the compare function as the Tree Node may
	# carry any data type
	def compare(self, a, b):
		pass

	# Inserts a Node containing val into root
	# @root: The root of the tree where we are inserting
	# @val: The value of the node that is being inserted
	# returns the root of the tree
	def insert(self, root, val):
		if root == None:
			return Node(val)

		comparator = self.compare(val, root.val)
		if  comparator == -1:
			# Add to the left subtree
			root.left = self.insert(root.left, val)
		elif comparator == 1:
			# Add to the right subtree
			root.right = self.insert(root.right, val)
		else:
			# Key already exists so return
			return root

		return root

	# Finds a Node containing val
	# @root: The root of the given tree
	# @val: The value of the node that we are looking for
	# returns the node the found node
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


	# Perform a pretty level order traversal
	# @root: The root of the given tree
	# does not return anything
	def level_order(self, root):
		depth = self.depth(root)
		level = 1
		if root:
			# We use this dictionary to store the two queues
			q_dict = {}
			q_dict['q1'] = deque([root])
			q_dict['q2'] = deque([])

			# We use these variables to keep track of the current queue
			current = 'q1'
			other = 'q2'

			# Print the indentations for the root
			indent = 2**(depth-level) - 1
			for _ in range(0, indent):
				print " ",

			while (len(q_dict['q1']) or len(q_dict['q2'])) and level <= depth:
				spaces = 2**(depth-level+1) - 1

				curr_node = q_dict[current].popleft()
				# Print the current node's value
				self.print_node(curr_node, spaces)

				# Append left and right children to the other queue
				if curr_node != " ":
					if curr_node.left:
						q_dict[other].append(curr_node.left)
					else:
						q_dict[other].append(" ")
					if curr_node.right:
						q_dict[other].append(curr_node.right)
					else:
						q_dict[other].append(" ")
				# If it's an empty node we still need to add empty children as the tree could be sparse but might
				# have a node(s) present on the very far right
				else:
					q_dict[other].append(" ")
					q_dict[other].append(" ")

				# Swap the queue if it is empty and is set to current
				if len(q_dict['q1'])==0 and current == 'q1':
					current = 'q2'
					other = 'q1'
					level+=1
					self.print_indent(depth, level)
				elif len(q_dict['q2'])==0 and current == 'q2':
					current = 'q1'
					other = 'q2'
					level+=1
					self.print_indent(depth, level)

	# HELPER FUNCTIONS

	# Finds the depth of a tree rooted at root
	# @root: Root of the given binary tree
	# returns an int i.e. the depth of the tree
	def depth(self, root):
		if root == None:
			return 0
		return 1 + max(self.depth(root.left), self.depth(root.right))

	# Prints a node with appropriate spaces
	# @node: The node that we are printing
	# @spaces: The space around the node
	# does not return anything
	def print_node(self, node, spaces):
			if node != " ":
				print node.val,
			else:
				print node,
			# Print spaces
			for _ in range(0, spaces):
				print " ",

	# Prints the indentation at each level
	# @depth: Depth of the tree
	# @level: Current level of the tree
	# does not return anything
	def print_indent(self, depth, level):
			print ""
			indent = 2**(depth-level) - 1
			if level <= depth:
				for _ in range(0, indent):
					print " ",