s = raw_input().strip()
a = [False, False, False, False, False]
for c in s:
    if c.isalnum():
        a[0] = True
    if c.isalpha():
        a[1] = True
    if c.isdigit():
        a[2] = True
    if c.islower():
        a[3] = True
    if c.isupper():
        a[4] = True

for i in a:
    print i
