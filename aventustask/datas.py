a="aabcglactdd"
mylist=list(a)
inp=input("enter a string: ")
elem=list(inp)
flag=0

for i in mylist:
    for j in elem:
        if i==j:
            print("yes")
            flag=1
            break
if (flag==0):
    print("not found")

    # if elem in mylist:
    #   print(elem,"yes")
    # else:
    #     print("no")