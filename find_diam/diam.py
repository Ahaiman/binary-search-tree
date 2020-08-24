
def diam(self):

            def diam_rec(node, Diameter):
                    
                if node == None:
                    return 0
                
                leftH = diam_rec(node.left, Diameter)
                rightH = diam_rec(node.right, Diameter)
                depth = rightH + leftH + 1
                Diameter[0] = max(Diameter[0], depth)
                return 1 + max(leftH,rightH)

            if self.root == None:
                return 0
            Diameter = [-1]
            diam_rec(self.root, Diameter) 
            return Diameter[0]    
                 
