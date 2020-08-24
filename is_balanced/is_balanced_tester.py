
def is_balanced_tester():
    counter = 0
    t = Binary_search_tree()
    t.insert('e', 8)
    t.insert('c', 2)
    t.insert('g', 8)
    t.insert('f', 2)
    if not t.is_balanced():
        print("Problem in is_balanced! #1")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('e', 1)
    t.insert('d', 2)
    t.insert('c', 2)
    t.insert('b', 1)
    t.insert('a', 2)
    if t.is_balanced():
         print("Problem in is_balanced! #2")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('d', 1)
    t.insert('c', 2)
    t.insert('e', 4)
    t.insert('f', 2)
    t.insert('h', 1)
    t.insert('g', 3)
    t.insert('b', 1)
    t.insert('a', 1)
    if t.is_balanced():
        print("Problem in is_balanced! #3")
    else:
        counter += 1
    t.insert('j', 2)
    t.insert('i', 5)
    if t.is_balanced():
        print("Problem in is_balanced! #4")
    else:
        counter += 1
    t = Binary_search_tree()
    if not t.is_balanced():
        print("Problem in is_balanced! #5")
    else:
        counter += 1
    t.insert('a', 1)
    if not t.is_balanced():
        print("Problem in is_balanced! #6")
    else:
        counter += 1
    t.insert('b', 1)
    if not t.is_balanced():
        print("Problem in is_balanced! #7")
    else:
        counter += 1
    if counter == 7:
        print("Great!")
