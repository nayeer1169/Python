#using zip function
l=[10,20,30,40,50]
z=[40,50,60,80,60]
for a,b in zip(l,z):
    print(a,b)

#other way
l=[10,20,30,40,50]
z=[40,50,60,80,60]
t=len(l)
print( )
print(t)
print( )
for a,b in zip(l,z):
    print(a,b)
    for h in range(t):
        print(l[h],z[h])
