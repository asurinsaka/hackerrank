from itertools import permutations
s,n = raw_input().strip().split(' ')
n = int(n)

print  '\n'.join(''.join(x) for x in (i for i in sorted(list(permutations(s,n)))))
