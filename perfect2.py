def function():
    n=1
    while n<=1000:
        i=1
        sum=0
        while i<n:
            if n%i==0:
                sum+=i
            i+=1
        if sum == n:
            print(n)
        n+=1
function()