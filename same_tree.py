# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    # print(p,q)
    if not p and not q:
        return True
    elif not p or not q:
        return False
    return (
        p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    )

p = TreeNode(1)
p.left = TreeNode(10)
p.right = TreeNode(2)
p.right.right = TreeNode(20)
p.right.left = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(10)
q.right = TreeNode(2)
q.right.right = TreeNode(20)
q.right.left = TreeNode(3)

print(isSameTree(p, q))
