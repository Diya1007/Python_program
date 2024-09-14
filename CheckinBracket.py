#check the order of brackets
def checkParan():
    global x,n,match
    match=0
    x=input("Enter the paran ")
    n=len(x)
    a=[n]
    for i in range (0,n):
        a.append(1)

    if(n%2==0):
        for i in range (0,n-1): 
            if (x[i]!=')' or (a[i]==0)) :

                for j in range (i+1,n):
                 var = (a[j]!=0) and (a[i]!=0)
                 if(x[i]!=x[j]) and var:
                    a[i]=0
                    a[j]=0
                    break

    for i in range (0,n):
        print("new array ", a[i])
        if(a[i]!=0):
            return False
    return True
ans=checkParan()
print(ans)

