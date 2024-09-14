import numpy as np

def ways_np():
    penny=1
    nikel=5
    m=[]

    

    print("enter the change ")
    change=int(input())
    n=int(change/5) #no of ways
    if(change>=5):

        if(change%5==0):                    #change is multiple of 5
            d=int(change/5)
            val=[0,d]
            arr=np.array([val])
            arr2=arr.copy()
            for i in range(0,n):
                d=d-1
                penny=int(change-5*(d))
                val=[[penny,d]]
                newarr = np.array_split (np.append(arr,val,axis=0),2,axis=0)         #spliting for the 2nd combination
                arr2=np.concatenate((arr2,newarr[1]),axis=0)                        #adding the 2nd combination to a new array
                #print(np.insert(arr,0,val,axis=0))
             
            
        else:
                arr2=np.array([[0,0]]) #making additional array for copying the combination
                d=int(change/5)
                result=arr2.all()

                remain=int(change%5)
                for i in range (0,n+1):
                    penny=change-d*5
                    val=[penny,d]
                    
                    arr=np.array([val])
                    if(result!=True):
                        arr2=arr.copy()
                        result=True
                    else:
                        
                        arr2=np.concatenate((arr2,arr),axis=0)
                    d=d-1

        
        for i in arr2:
            print (":",i)
    else:
        
        print(change,0)     

ways_np()

