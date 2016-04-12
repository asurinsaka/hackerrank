X = int(raw_input().strip())
Y = int(raw_input().strip())
Z = int(raw_input().strip())
N = int(raw_input().strip())

result = []

for x in xrange(X+1):
    for y in xrange(Y+1):
        for z in xrange(Z+1):
            if x + y + z != N:
                result.append([x, y, z])

print result
