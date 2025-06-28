### I'm so proud of this 
# https://leetcode.com/problems/symmetric-tree/?envType=problem-list-v2&envId=depth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### source https://www.geeksforgeeks.org/dsa/dfs-traversal-of-a-tree-using-recursion/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### source https://www.geeksforgeeks.org/dsa/dfs-traversal-of-a-tree-using-recursion/ 

class Solution:
    def leftPostorder(self, root, leftarr): 
        # print ("left postorder")
        if root:
            # print(root.val)
            # First recur on left child
            self.leftPostorder(root.left, leftarr)
            # the recur on right child
            self.leftPostorder(root.right, leftarr)
            # now print the data of node
            # print(root.val)
            leftarr.append(root.val)
            # return leftarr ## 4ms 
            return root.val ## 0ms
        # print(root)
        leftarr.append(root)
        # return leftarr ## 4ms 
        return root ## 0ms


    def rightPostorder(self, root, rightarr): 
        # print("right postorder")
        if root:
            # print(root.val)
            # First recur on right child
            self.rightPostorder(root.right, rightarr)
            # the recur on left child
            self.rightPostorder(root.left, rightarr)
            # now print the data of node
            # print(root.val)
            rightarr.append(root.val)
            # return rightarr 
            return root.val ## 0ms
        # print(root)
        rightarr.append(root)
        # return rightarr ## 4ms 
        return root ## 0ms

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True 

        ## begin 0ms section
        leftarr=[]
        rightarr=[]

        print("left postorder")
        self.leftPostorder(root.left, leftarr)
        print(leftarr)

        print("right postorder") 
        self.rightPostorder(root.right, rightarr)
        print(rightarr)
        
        return (leftarr == rightarr) ## 0ms

        # return(self.leftPostorder(root.left, leftarr) == self.rightPostorder(root.right, rightarr)) ## 4ms
