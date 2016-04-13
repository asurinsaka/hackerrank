s = raw_input().strip()
a = raw_input().strip().split(" ")

print s[:int(a[0])] + a[1] + s[int(a[0])+1:]
