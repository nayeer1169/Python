#normal way
l=[ ]
for a in range(1,101,1):
    #print(a)
    l.append(a)
print(l) 


#comprehension way
n=[a for a in range(1,101,1)]
print(n)

#comprehension way in even order
m=[z for  z in range(1,101,1) if (z%2==0)]
print(m)


#comprehension way to string 
s="hello"
n=[g for g in s]
print(n)