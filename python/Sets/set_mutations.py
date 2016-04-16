n1 = input()
s1 = set(map(int, raw_input().strip().split(" ")))
N = input()

for _ in xrange(N):
    l = list(raw_input().strip().split(" "))
    s2 = set(map(int, raw_input().strip().split(" ")))
    if l[0] == 'update':
        s1 |= s2
    if l[0] == 'intersection_update':
        s1 &= s2
    if l[0] == 'difference_update':
        s1 -= s2
    if l[0] == 'symmetric_difference_update':
        s1 ^= s2

print sum(s1)
