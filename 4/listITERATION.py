#1st way by range
l=[1,2,3,4,5]
a=len(l)
print(a)
print( )
for r in range(a):
    print(l[r])

#another way direct
print( )
l=[5,6,7,8,9]
a=len(l)
print(a)
print( )
for r in l:
    print(r)

#reverse order 
#for reversing we should do the range method only 
#other method is not available
print( )
l=[12,24,36,48,60]
a=len(l)
print(a)
print( )
for r in range(a-1,-1,-1):
    print(l[r])