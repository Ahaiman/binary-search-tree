def diam_tester():
    counter = 0
    t = Binary_search_tree()
    t.insert('e', 8)
    t.insert('c', 2)
    t.insert('g', 8)
    t.insert('f', 2)
    if t.diam() != 4:
        print("Problem in diam! #1")
    else:
        counter += 1
    t.insert('a', 1)
    if t.diam() != 5:
        print("Problem in diam! #2")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('f', 6)
    t.insert('e', 8)
    t.insert('d', 2)
    t.insert('c', 8)
    t.insert('b', 2)
    t.insert('a', 1)
    if t.diam() != 6:
        print("Problem in diam! #3")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('c', 1)
    t.insert('g', 3)
    t.insert('e', 5)
    t.insert('d', 7)
    t.insert('f', 8)
    t.insert('h', 6)
    t.insert('z', 6)
    if t.diam() != 5:
        print("Problem in diam! #4")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('c', 1)
    t.insert('b', 3)
    t.insert('a', 5)
    t.insert('f', 7)
    t.insert('e', 8)
    t.insert('d', 6)
    t.insert('g', 6)
    if t.diam() != 6:
        print("Problem in diam! 5")
    else:
        counter += 1
    if counter == 5:
        print("OK: Question 2D")
