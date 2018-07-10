def sortByHeight(a):
    trees_at = [i for i, v in enumerate(a) if v == -1]
    people = [i for i in a if i != -1]
    sorted(people)
    for tree in trees_at:
        people.insert(tree, -1)
    return people