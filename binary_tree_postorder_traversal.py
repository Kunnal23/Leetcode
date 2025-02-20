# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    res = []
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)
    postorder(root)
    return res

root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(2)
root.right.right = TreeNode(20)
root.right.left = TreeNode(3)

print(postorderTraversal(root))
