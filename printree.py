

#main function: printree
#byKey = True -> showing keys instead of values

def printree(tree, bykey = True):
        """ Prints a textual representation of the tree"""
        return listByLevels(tree, bykey)

def listByLevels(tree, bykey = False):
        """Return a list of textual representations of the levels in the tree"""
        if tree == None:
                return ["#"]

        thistr = str(tree.key) if bykey else str(tree.val)

        return concatLevel(listByLevels(tree.left,bykey),
                           thistr,
                           listByLevels(tree.right,bykey))

def concatLevel(left,root,right):
        """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""
        
        lwid = len(left[-1])
        rwid = len(right[-1])
        rootwid = len(root)
        
        result = [(lwid+1)*" " + root + (rwid+1)*" "]
        
        ls = leftspace(left[0])
        rs = rightspace(right[0])
        result.append(ls*" " + (lwid-ls)*"_" + "/" + rootwid*" " + "|" + rs*"_" + (rwid-rs)*" ")
        
        for i in range(max(len(left),len(right))):
                row = ""
                if i<len(left):
                        row += left[i]
                else:
                        row += lwid*" "

                row += (rootwid+2)*" "
                
                if i<len(right):
                        row += right[i]
                else:
                        row += rwid*" "
                        
                result.append(row)
                
        return result

def leftspace(row):
        """used for concatLevel function"""
        #row is the first row of a left node
        #returns the index of where the second whitespace starts
        i = len(row)-1
        while row[i]== " ":
                i -= 1
        return i+1

def rightspace(row):
        """used for concatLevel function"""
        #row is the first row of a right node
        #returns the index of where the first whitespace ends
        i = 0
        while row[i]== " ":
                i+=1
        return i





