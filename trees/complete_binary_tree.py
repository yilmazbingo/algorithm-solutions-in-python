'''
222. Medium Count Complete Tree Nodes
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity. It has to be either o(logN) or O(1)
'''
# Total number of node in full tree 2^(h-1)-1. level of root is 1. So height does not start from 0
# we need to figure out time complexity of "h" value
#Heigh of binary tree is log(N). time complexity of finding h:O(log(N))