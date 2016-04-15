N = int(raw_input().strip())
heights = set(map(int, raw_input().strip().split(" ")))


print '{0:0.3f}'.format(sum(heights)*1.000/len(heights))
