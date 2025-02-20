class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    res = []

    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return res


root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(2)
root.right.right = TreeNode(20)
root.right.left = TreeNode(3)

print(preorderTraversal(root))
