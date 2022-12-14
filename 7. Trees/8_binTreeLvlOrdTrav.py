# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # queue of node objects
        queue = deque([root])
        res = []
        while queue:
            row = []
            for i in range(len(queue)):
                node = queue.popleft()
                row.append(int(node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(row)
        return res
