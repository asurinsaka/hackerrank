M=int(raw_input().strip())
m=set(map(int,raw_input().strip().split()))
N=int(raw_input().strip())
n=set(map(int,raw_input().strip().split()))

result=sorted(m.difference(n).union(n.difference(m)))

for i in result:
    print i
