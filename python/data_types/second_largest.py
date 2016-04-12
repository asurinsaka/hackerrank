N = int(raw_input().strip())

L = map(int, raw_input().strip().split(" "))

first = -100
second = -100

for i in xrange(N):
    if L[i] > first:
        second = first
        first = L[i]
    elif L[i] > second and L[i] < first:
        second = L[i]

print second
