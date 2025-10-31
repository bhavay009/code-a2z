class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0

        def fs(root,prefix):
            nonlocal count
            if not root:
                return 

            if root.val>=prefix:
                count+=1

            prefix=max(root.val,prefix)
            fs(root.left,prefix)
            fs(root.right,prefix)

        fs(root,root.val)

        return count            
    
