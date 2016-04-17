K = input()
L = list(map(int, raw_input().strip().split(" ")))

S = set(L)

print (sum(S)*K - sum(L))/(K-1)
