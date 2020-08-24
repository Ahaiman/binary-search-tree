
def is_sorted_tester():
    counter = 0
    t = Binary_search_tree()
    t.insert('e', 4)
    t.insert('c', 3)
    t.insert('a', 2)
    t.insert('d', 1)
    t.insert('b', 8)
    t.insert('f', 5)
    if t.is_sorted():
        print("Problem in is_sorted! #1")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('e', 1)
    t.insert('d', 2)
    t.insert('c', 2)
    t.insert('b', 1)
    t.insert('a', 2)
    if t.is_sorted():
        print("Problem in is_sorted! #2")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('e', 5)
    t.insert('d', 4)
    t.insert('c', 3)
    if not t.is_sorted():
        print("Problem in is_sorted! #3")
    else:
        counter += 1
    t = Binary_search_tree()
    if not t.is_sorted():
        print("Problem in is_sorted! #4")
    else:
        counter += 1
    t.insert('a', 1)
    if not t.is_sorted():
        print("Problem in is_sorted! #5")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('d', 8)
    t.insert('c', 2)
    t.insert('e', 8)
    t.insert('f', 2)
    if t.is_sorted():
        print("Problem in is_sorted! #6")
    else:
        counter += 1
    t = Binary_search_tree()
    t.insert('e', 8)
    t.insert('c', 2)
    t.insert('g', 8)
    t.insert('f', 2)
    if t.is_sorted():
        print("Problem in is_sorted! #7")
    else:
        counter += 1
    if counter == 7:
        print("OK: Question 2B")
