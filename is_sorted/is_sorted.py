 def is_sorted(self):

           def sorted_rec(node, minVal, maxVal):
                if node == None:
                        return True
                if node.val < minVal or node.val > maxVal:
                        return False
                return sorted_rec(node.left,minVal, node.val) \
                       and sorted_rec(node.right, node.val, maxVal)
                
           if self.root == None:
                   return True
           return sorted_rec(self.root,0, 101)
