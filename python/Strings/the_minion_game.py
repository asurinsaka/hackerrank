def isvowal(c):
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        return True
    else:
        return False


s = raw_input().strip()
Stuart = 0
Kevin = 0
for i in xrange(len(s)):
    if not isvowal(s[i]):
        Stuart += len(s)-i
    else:
        Kevin += len(s)-i
        
if Stuart > Kevin:
    print "Stuart " + str(Stuart)
elif Stuart == Kevin:
    print "Draw"
else:
    print "Kevin " + str(Kevin)
    
