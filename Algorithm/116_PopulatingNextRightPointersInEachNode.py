# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None or (root.left is None and root.right is None):
            return root
        
        root.next = None
        self.connectRecursive(root)
        
    def connectRecursive(self,root):
        if root.left is None and root.right is None:
            return 
        
        root.left.next = root.right
        if root.next is not None:
            root.right.next = root.next.left
        else:
            root.right.next = None
        
        self.connectRecursive(root.left)
        self.connectRecursive(root.right)
