
def max_sum_tester():
    countingRight = 0
    
    tree = Binary_search_tree()
    tree.insert('d', 1)
    tree.insert('c', 2)
    tree.insert('e', 4)
    tree.insert('b', 5)
    tree.insert('a', 2)
    if tree.max_sum() != 10:
        print("Problem in max_sum! #1")
    else:
        countingRight += 1
        
    tree.insert('f', 10)
    
    if tree.max_sum() != 15:
        print("Problem in max_sum! #2")
    else:
        countingRight += 1
        
    tree = Binary_search_tree()
    tree.insert('d', 1)
    tree.insert('c', 2)
    tree.insert('e', 4)
    tree.insert('f', 2)
    tree.insert('h', 1)
    tree.insert('g', 3)
    tree.insert('b', 1)
    tree.insert('a', 1)
    
    if tree.max_sum() != 11:
        print("Problem in max_sum! #3")
    else:
        countingRight += 1
        
    tree.insert('j', 2)
    tree.insert('i', 5)
    
    if tree.max_sum() != 15:
         print("Problem in max_sum! #4")
    else:
        countingRight += 1
        
    tree = Binary_search_tree()
    tree.insert('e', 1)
    tree.insert('d', 2)
    tree.insert('c', 2)
    tree.insert('b', 1)
    tree.insert('a', 2)
    
    if tree.max_sum() != 8:
         print("Problem in max_sum! #5")
    else:
        countingRight += 1
    tree.insert('f', 12)
    
    if tree.max_sum() != 13:
         print("Problem in max_sum! #6")
    else:
        countingRight += 1

    #empty tree case
    tree = Binary_search_tree()
    if tree.max_sum() != 0:
        print("Problem in max_sum! #7")
    else:
        counter += 1
    tree.insert('a', 1)
    if tree.max_sum() != 1:
        print("Problem in max_sum! #8")
    else:
        countingRight += 1
    if countingRight == 8:
        print("OK")
