n,m = map(int, raw_input().strip().split(" "))
L = list(map(int, raw_input().strip().split(" ")))
A = set(map(int, raw_input().strip().split(" ")))
B = set(map(int, raw_input().strip().split(" ")))


happiness = 0

for i in L:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print happiness
