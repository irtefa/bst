from abc import ABCMeta, abstractmethod
from node import Node
from collections import deque


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
		if  comparator < 1:
			# Add to the left subtree
			root.left = self.insert(root.left, val)
		else:
			# Add to the right subtree
			root.right = self.insert(root.right, val)

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

	def depth(self, root):
		if root == None:
			return 0
		return 1 + max(self.depth(root.left), self.depth(root.right))

	def level_order(self, root, depth):
		level = 1
		if root:
			q1 = deque([root])
			q2 = deque([])
			current = 'q1'

			while (len(q1) or len(q2)) and level <= depth:
				indent = 2**(depth-level) - 1
				spaces = 2**(depth-level+1) - 1
				if current == 'q1':
					curr_node = q1.popleft()
					# Print the current node's value
					# Print indentation

					for _ in range(0, indent):
						print " ",
					if curr_node != " ":
						print curr_node.val,
					else:
						print curr_node,
					# Print spaces
					for _ in range(0, spaces):
						print " ",

					# Append left and right children to the other queue
					if curr_node != " ":
						if curr_node.left:
							q2.append(curr_node.left)
						else:
							q2.append(" ")
						if curr_node.right:
							q2.append(curr_node.right)
						else:
							q2.append(" ")
				else:
					curr_node = q2.popleft()
					# Print the current node's value
					for _ in range(0, indent):
						print " ",
					if curr_node != " ":
						print curr_node.val,
					else:
						print curr_node,
					# Print spaces
					for _ in range(0, spaces):
						print " ",

					# Append the left and right children to the other queue
					if curr_node != " ":
						if curr_node.left:
							q1.append(curr_node.left)
						else:
							q1.append(" ")
						if curr_node.right:
							q1.append(curr_node.right)
						else:
							q1.append(" ")
				# Swap the queue if it is empty and is set to current
				if len(q1)==0 and current == 'q1':
					current = 'q2'
					print ""
					level+=1
				elif len(q2)==0 and current == 'q2':
					current = 'q1'
					print ""
					level+=1
