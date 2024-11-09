# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        while q:
            node = q.popleft()

            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return node.val