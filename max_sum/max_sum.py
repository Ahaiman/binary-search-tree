
def max_sum(self):
       ''' return the max sum of nodes in a path from root to leaf'''
        def rec_max_sum(node, maxSum):
                if node == None:
                        return 0
                if node.left == None and node.right == None:
                        return maxSum + node.val
                return max(rec_max_sum(node.left, maxSum + node.val),\
                           rec_max_sum(node.right, maxSum + node.val)) 

        maxSum = 0
        if self.size() == 0:
            return maxSum
        return rec_max_sum(self.root, 0)
