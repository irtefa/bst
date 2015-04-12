# BST-Doordash 

Since implementing a simple binary search tree just for integers or numbers limits its extensibility, I created an AbstractBst that has the ability to create any form of bst as long as the user creates a class that inherits from AbstractBst and implements a compare method. Therefore, my implementation of bst is not just limited to numbers but also custom objects where the user can implement a custom compare method.

These are the different files I have:

  - abstract_bst.py: The Abstract bst that has find and print_tree.
  - simple_bst.py: A Simple bst that I implemented with a compare function (just for numbers).
  - node.py: A node for binary tree.
  - test_abstract_bst.py: Unittests for abstract_bst.py
  - test_simple_bst.py: Unittests for simple_bst.py

Disclaimer: 
 - I used this  [Stackoverflow] post to figure out the number of spaces and indentations I need at each level. However, I did not use anyone else's code.
 - This code is written and testes in Python 2.7

In order to see results for a few cases please execute simple_bst.py

[Stackoverflow]:http://stackoverflow.com/questions/8964279/coding-a-basic-pretty-printer-for-trees-in-java

[buzzbd]:Story://com.buzzbd.mirtefa
