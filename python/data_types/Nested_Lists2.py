N = int(raw_input().strip())
students=[]
[students.append([raw_input().strip(), float(raw_input().strip())]) for _ in xrange(N)]
students = sorted(students)
scores = sorted(set(students[i][1] for i in xrange(N)))

second = scores[1]
for i in students:
    if second == i[1]:
        print i[0]
