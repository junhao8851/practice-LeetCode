class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
         return root.val == root.left.val + root.right.val
#return 一个判断语句会返回布尔型变量
#判断根节点是否等于子节点之和