N = int(raw_input().strip())

L = map(int, raw_input().strip().split(" "))

L.sort()



i = N-2;
while i != 0:
    if L[i] < L[N-1]:
        break
    i -= 1
    

print L[i]
