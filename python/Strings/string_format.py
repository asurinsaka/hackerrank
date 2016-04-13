x = int(raw_input().strip())
length = len(bin(x))-1

for i in xrange(x):
    a = i+1
    print str(a).rjust(length-1)+str(oct(a))[1:].rjust(length)+str(hex(a))[2:].upper().rjust(length)+str(bin(a))[2:].rjust(length)
