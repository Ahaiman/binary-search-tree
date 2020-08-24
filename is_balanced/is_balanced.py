
def is_balanced(self):

        def is_balanced_rec(node):
            
            if node is None:
                return 0
            leftH = is_balanced_rec(node.left)
            if leftH == -1: return -1
            
            rightH = is_balanced_rec(node.right)
            if rightH == -1: return -1

            if abs(leftH - rightH) > 1:
                return -1
     
            return max(leftH, rightH) + 1
                    
        return is_balanced_rec(self.root) > -1
