#discard()   discard and remove is same
s={10,20,30,40,50,60,70,80,90}
s.discard(20)
print(s)


print( )
#clear( )
s={10,20,30,40,50,60,70,80,90}
s.clear()
print(s)


print( )
#update
s={10,20,30,40,50,60,70,80,90}
l=[12,23,34,45,56,67,70]
s.update(l)
print(s)

#update doubt
s={10,20,30,40,50,60,70,80,90}
a=(12,23,34,56,78)
s.update(a)
print(s)
