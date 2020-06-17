x = int(input("The number upto which the sequence is to be found :"))
print(x)
z = 0
t = 1
if (x < 0) :
    print ("\n Wrong input") 
else :
    print("\n The sequence is : ")
    print("\n",z)
    y = 0
    while( y + t < x ):
        y = y + t
        t = y - t
        
        print( "\n", y)
