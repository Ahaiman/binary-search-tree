#Add this for importing print tree funcion: from printree import *

class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    #Example: (key:value)
    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"
    
class Binary_search_tree():

    def __init__(self):
        self.root = None

    #using external function from file: print.py
    def __repr__(self): 
        out = ""
        for row in printree(self.root): 
            out = out + row + "\n"
        return out


    def search(self, key):
        ''' return tree node with key, using recursion '''

        def search_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return search_rec(node.left, key)
            else:
                return search_rec(node.right, key)

        return search_rec(self.root, key)



    def insert(self, key, val):
        ''' insert node with key and val into tree, using recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val     
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else: #key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return
        
        if self.root == None: #empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)


    def minimum(self):
        ''' return node with minimal key '''
        if self.root == None:
            return None
        node = self.root
        left = node.left
        while left != None:
            node = left
            left = node.left
        return node


    def depth(self):
        ''' return depth of tree, uses recursion'''
        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)


    def size(self):
        ''' return number of nodes in tree, uses recursion '''
        def size_rec(node):
            if node == None:
                return 0
            else:
                return 1 + size_rec(node.left) + size_rec(node.right)

        return size_rec(self.root)

