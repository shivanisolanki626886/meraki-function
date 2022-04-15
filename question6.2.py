def function():
    list=[5,10,50,20]
    list1=[2,20,3,5]
    i=0
    d=[]
    while i<len(list): 
        a=list[i]*list1[i]
        d.append(a)
        i=i+1
    print(d)
function()