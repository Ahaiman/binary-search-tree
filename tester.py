#Tester for the Binary_search_tree class
#Copy this to the relevant file, or import the functions.



def test():
    bin_tree = Binary_search_tree()
    print("MIN ",bin_tree.minimum())
    print("DEPTH ",bin_tree.depth())
    print("SIZE ",bin_tree.size())
    print(bin_tree)
    bin_tree.insert(2,"a")
    print(bin_tree)
    bin_tree.insert(4,"b")
    print(bin_tree.lookup(4))
    print(bin_tree)
    bin_tree.insert(2,"c")
    print(bin_tree)
    bin_tree.insert(3,"d")
    print(bin_tree)
    bin_tree.insert(1,"e")
    print(bin_tree)
    bin_tree.insert(0,"f")
    bin_tree.insert(5,"g")
    bin_tree.insert(7,"h")
    bin_tree.insert(6,"i")
    print(bin_tree)
    print(bin_tree.lookup(1))
    print(bin_tree.lookup(2))
    print(bin_tree.lookup(9))
    print("MIN ",bin_tree.minimum())
    print("DEPTH ",bin_tree.depth())
    print("SIZE ",bin_tree.size())
