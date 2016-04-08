N=int(raw_input().strip())

student = {}
for i in xrange(N):
    text=raw_input().strip().split()
    average = (float(text[1]) + float(text[2]) + float(text[3]))/3
    student[text[0]] = average

querry=raw_input().strip()

if (querry in student):
    print "{0:.2f}".format(student[querry])
else:
    print "not here"

#print student
