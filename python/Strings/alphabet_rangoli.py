import string
N = int(raw_input().strip())
a = list(string.ascii_lowercase)


for i in xrange(2*N-1):
    s = ""
    for j in xrange(4*N-3):
        if abs(2*N-2-j)%2 == 0 and abs(2*N-2-j)/2 <= i and i < N:
            s += a[abs(2*N-2-j)/2+N-i-1]
        elif abs(2*N-2-j)%2 == 0 and abs(2*N-2-j)/2 <= 2*N-2 - i and i >= N:
            s += a[abs(2*N-2-j)/2+i-N+1]
        else:
            s += '-'
    print s
