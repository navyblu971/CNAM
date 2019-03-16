import numpy as np ; 

l = [ [2,0,0], [4,-1,0], [-6,1,2]] ; 
b = [2,3,-7] ; 



def fsub(A,b):
    n = np.size(b)
    x = np.zeros(n)
    sol = 1
    for i in range(n):
        t = b[i] - np.sum(A[i,:i] * x[:i])
        if A[i,i] == 0. :
            if t == 0. :
                sol = -1
                x[i] = 0.
            else :
                sol = 0
                x.fill(np.nan)
                return x, sol
        else :
            x[i] = t / A[i,i]
    return x, sol

def forwardSub (u , b) :
    n =len(b)-1 ;
    print (u) ; 
    print (b) ; 
    somme = 0 ; 

    y=[0 for d in range (n)] ; 

  
    y[0] = b[0] ; 
    for i in range (1, len(b)-1):
        somme =0 ; 
        for j in range (0,i-2):
            somme = somme + u[i][j]*y[j] ;
        y[i] =  b[i] - somme  ;


    print ("y ") ;
    print  ( y) ; 
    return y ; 

#y  = forwardSub ([ [2,0,0], [4,-1,0], [-6,1,2]] , [2,3,-7] )


def gaussJordan (A ):
    r=0
    m=np.size(A, 1) 
    n =np.size(A,0) 

    print ("m=", m)
    print ("n=", n)
  
    for j in np.arange (0,m) :
        k =np.argmax(abs(A.T[j][r:])) +r
        print ("colomn analysed :" , A.T[j][r:])
        print ("indice max = ",k) 
        print ("A")
        print ( A)
        #print ("A.T[2][:1]-->",A.T[2][0:])
        if A[k,j] != 0:
            #r=r+1
            print ("r=", r) 
            print ("A[k]=" , A[k]) 
            print ("A[k,j] " , A[k,j])
            A[k] = A[k]/ A[k,j]
            print ("A[k] / A[k,j]= " , A[k]) 
            tmp = A[k] 
            print ("tmp =" , tmp)
            A[k]= A[r] 
            A[r]= tmp   
           #NOT WORKING  A[[k,r] = A[[r,k]] ; 

           
            print("r =",r)
            for i in np.arange (0,n):
                print ("updating line i=", i)
                if i != r:
                    A[i]=A[i] - A[r]*A[i,j]
                    print ("A[i]=" , A[i])
            r=r+1

        print ("XXXXXXXXXXX")
        print ("new A=")
        print ( A)
        print ("XXXXXXXXXXX")
        print ("j=", j)

    return A 
            



A2 = np.array([[2.,-1.,0.] , [-1., 2., -1.], [0.,-1., 2.]])

print ("result --->")
print ( gaussJordan(A2) )





#print fsub (l,b) ; 

##print ("result ForwardSub") ; 
##print (np.allclose(np.dot(l, b), y) )

#print ("np.linalg.solve") ; 
#print ( np.linalg.solve ([ [2,0,0], [4,-1,0], [-6,1,2]] ,[2,3,-7]  )) ; 