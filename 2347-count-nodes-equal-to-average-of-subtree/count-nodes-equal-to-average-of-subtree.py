# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if node is None:
                return 0, 0, 0

            left_sum, left_count, left_ans = dfs(node.left)
            right_sum, right_count, right_ans = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            average = total_sum // total_count

            current = 0
            if node.val == average:
                current = 1

            total_ans = left_ans + right_ans + current

            return total_sum, total_count, total_ans

        total_sum, total_count, answer = dfs(root)

        return answer