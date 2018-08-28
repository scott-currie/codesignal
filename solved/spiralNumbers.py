import itertools

def main():
    n = 4
    print_matrix(spiralNumbers(n))

def spiralNumbers(n):
    m = make_matrix(n)
    cursor = [0,-1]
    next_curs = [0, 0]
    # Directions are what you need to add to the cursor
    # coordinates to make them move first right, then down,
    # then left, then up. Need to start from the beginning
    # again to continue looping
    directions = [(0,1), (-1,0), (0, -1), (1, 0)]

    i = 1
    for d in itertools.cycle(directions):
        print_matrix(m)
        print('direction:', d)
        while m[next_curs[0]][next_curs[1]] == 0:
            if i == pow(n, 2) + 1:
                break
            # Check out next cursor pos by adding direction components to its coords
            next_curs = [cursor[0] + d[0], cursor[1] + d[1]]
            # Is next_curs within our matrix?
            if 0 <= next_curs[0] < n and 0 <= next_curs[1] < n:
                # Is the cell at next_curs a 0?
                if m[next_curs[0]][next_curs[1]] == 0:
                    # cursor[0] += d[0]
                    # cursor[1] += d[1]
                    cursor = next_curs
                    print('cursor:', cursor)
                    m[cursor[0]][cursor[1]] = i
                    i += 1
                else:
                    continue
        if i == pow(n, 2):
            break
    return m
    
    # print(m)
    
def make_matrix(n):
    m = []
    for r in range(n):
        m.append([0 for i in range(n)])
    return m

def print_matrix(m):
    for r in m:
        print(' '.join([str(i) for i in r]) + '\n')

if __name__ == '__main__':
    main()