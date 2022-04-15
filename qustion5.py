def fun():
    i=0
    s=0
    while i<=10:
        if i % 3 == 0 or i % 5 == 0:
            s=s+i
        i+=1
    print(s)
fun()
