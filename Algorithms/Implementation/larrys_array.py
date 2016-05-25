for _ in range(int(input())):
    count = 0
    n = int(input());
    l = list(map(int,input().split()))
    for i in range(len(l)):
        if l[i] != i+1:
            temp = l[i]
            
            for n, k in enumerate(l):
                if k == i+1:
                    l[n] = temp
                    l[i] = i+1
                    break
            count += 1
            
    if count % 2 == 0:
        print("YES")
    else:
        print("NO")
