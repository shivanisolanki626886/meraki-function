def add_numbers():
    list=[2,6,18,10,3,75]
    list1=[6,19,24,12,3,87]
    i=0
    while i<len(list):
        if list[i]%2==0 and list1[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i+=1
add_numbers()