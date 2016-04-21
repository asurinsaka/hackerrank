from itertools import product
print ' '.join( str(i) for i in list(product(list(map(int,raw_input().strip().split(' '))), list(map(int,raw_input().strip().split(' '))))))
