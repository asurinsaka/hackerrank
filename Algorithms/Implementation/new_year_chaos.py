#!/bin/python3

import sys


T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    # your code goes here
    count = 0
    chaos = False
    i = 1
    l = [ 0 for _ in range(len(q))]
    length = len(q)
    while not chaos and i != length:
        for n, k in enumerate(q):
            if k == i:
                for j in range(n):
                    l[q[j]-1] += 1
                    if l[q[j]-1] > 2:
                        chaos = True
                        break
                q.remove(i)
                i += 1
                break
    if chaos:
        print("Too chaotic")
    else:
        print(sum(l))
