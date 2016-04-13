S = raw_input().strip()
result = ""
for c in S:
    if c.islower():
        result += c.upper()
    elif c.isupper():
        result += c.lower()
    else:
        result += c

print result
