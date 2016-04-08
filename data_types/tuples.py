import __builtin__

N=int(raw_input().strip())
T=tuple(int(x) for x in raw_input().strip().split())

print hash(T)
