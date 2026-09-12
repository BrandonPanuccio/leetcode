# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matches = 0

        def nodeAverages(node: TreeNode) -> tuple[int,int]:
            nonlocal matches

            if node is None:
                return 0, 0

            left_sum, left_count = nodeAverages(node.left)
            right_sum, right_count = nodeAverages(node.right)

            total_val = node.val + left_sum + right_sum
            total_nodes = 1 + left_count + right_count

            if total_val // total_nodes == node.val:
                matches += 1

            return total_val, total_nodes

        nodeAverages(root)

        return matches


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(6)

    result = solution.averageOfSubtree(root)
    print(result)