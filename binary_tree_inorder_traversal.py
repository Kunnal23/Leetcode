class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    if not root:
        return res
    st = []
    curr = root
    while curr is not None:
        st.append(curr)
        curr = curr.left
    while len(st) > 0:
        curr = st.pop()
        res.append(curr.val)
        curr = curr.right
        while curr is not None:
            st.append(curr)
            curr = curr.left
    return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))