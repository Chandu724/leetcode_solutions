# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        res= []
        
        def dfs(node, res, ind):
            if not node:
                return
            if len(res) == ind:
                res.append([node.val])
            else:
                res[ind].append(node.val)
            dfs(node.left, res, ind+1)
            dfs(node.right, res, ind+1)
            
        dfs(root, res, 0)
        
        for i in range(len(res)):
            res[i] = max(res[i])
            
        return res
        
        
                