class Solution:
    def sum_tree(self, node):
            if node is None:
                return 0
            return node.val + self.sum_tree(node.left) + self.sum_tree(node.right)

    def update_tree(self, node, previous):
            if previous > node.val:
                node.val += previous
            if node.right is None and node.left is None:
                return(node.val)
            if node.right is not None:
                node.val += self.sum_tree(node.right)
                self.update_tree(node.right, previous)
            if node.left is not None:
                previous = node.val
                self.update_tree(node.left, previous)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        previous = -1
        self.update_tree(root, previous)
        return(root)
