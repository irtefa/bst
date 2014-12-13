from abc import ABCMeta, abstractmethod

class AbstractBst(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	# The user should implement the compare function as the Tree Node may
	# carry any data type
	def compare(self, a, b):
		pass
