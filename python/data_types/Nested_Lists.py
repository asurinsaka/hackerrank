N = int(raw_input().strip())
L=[]
lowest = 10000
sec_low = 10000
L = sorted([[raw_input().strip(), float(raw_input().strip())] for _ in xrange(N)])
scores = sorted(set([L[i][1] for i in xrange(N)]))
scores[1]
for i in xrange(N):
    if scores[1] == L[i][1]:
        print L[i][0]
