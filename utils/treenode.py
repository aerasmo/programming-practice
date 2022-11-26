from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def nodeBuilder(arr: Optional[int]):
        """
            builds TreeNode from an array 
            returns root of the TreeNode
        """
        if len(arr) == 0: return None
        root = TreeNode(arr[0])
        nodes = [root]
        i = 1
        diff = 1
        while i < len(arr):
            node = TreeNode(arr[i])
            if i % 2 == 1:
                nodes[i-diff].left = node
                diff += 1
            else: 
                nodes[i-diff].right = node
            nodes.append(node)
            i += 1
        return nodes[0]