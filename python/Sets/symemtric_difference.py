n1 = input()
s1 = set(map(int, raw_input().strip().split(" ")))
n2 = input()
s2 = set(map(int, raw_input().strip().split(" ")))

print len(s1^s2)
