s = raw_input().strip()
sub = raw_input().strip()
count = 0
for i in xrange(len(s)):
    if sub == s[i:i+len(sub)]:
        count += 1
        
print count
