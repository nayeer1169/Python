#get
#1
d={
    'name':'abc',
    'fees': 8000,
    'course':'Python'
}
g=d.get('name')
print(g)
#2
g=d['name']
print(g)

print( )
#keys
for a in d.keys():
    print(a)

print( )
#value
for a in d.values():
    print(a)

print( )
#item
for a,b in d.items():
    print(a,b)

print( )
#delete
del d['fees']
print(d)

print( )
#pop
a=d.pop('name')
print(a)
print(d)

print( )
#dict
f=dict(name='Python',fees=8000)
print(f)

print( )
#update
d.update({'fees':12000})
print(d)

print( )
#clear
d.clear()
print(d)

print( )
#insert
d['desc']="This is python"
print(d)