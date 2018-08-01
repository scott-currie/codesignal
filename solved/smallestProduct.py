
# https://app.codesignal.com/challenge/8FdeLisamv6cFZPAc
# Challenge is to take an array of integers, including negatives, and return
# the smallest product of any three of them. This solution totally sucks,
# but it works fast enough for the code judge.
import itertools

def smallestProduct(arr):
    p = 0
    
    # for i in itertools.combinations(arr, 3):
    #     pr = prod(i)
    #     m = pr if p == 0 or pr <= m else m
    #     p += 1
    # return m
    arr = sorted(arr)
    # if arr[0] == 0:
    #     return 0
    # if arr[0] > 0:
    #     return(prod(arr[:3]))
    # else:
    #     # rp = arr[0] * arr[-1] * arr[-2]
    #     pos_elem = [i for i in range(1, len(arr) - 1)]
    #     if max(pos_elem) == 0:
    #         return 0
    #     else:
    #     # for i in range(1, len(arr) - 1):
    #     #     if i > 0:
    #     #         return rp * i
    #         return arr[0] * arr[-1] * arr[-2]
    #         
    if len(arr) < 20:
        candidates = arr
    else:
        neg_arr = [n for n in arr if n < 0]
        pos_arr = [n for n in arr if n >= 0]
        candidates = neg_arr[:3] + neg_arr[-3:] + pos_arr[:3] + pos_arr[-3:]
    
    return min([x * y * z for x, y, z in itertools.combinations(candidates, 3)])
    
    # # No negs. Return smallest 3 >= 0
    # if len(neg_arr) == 0:
    #     return prod(pos_arr)[:3]
    

def prod(l):
    p = 1
    for n in l:
        p *= n
    return p