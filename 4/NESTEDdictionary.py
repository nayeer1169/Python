#1
course={
    'php':{'duration': '3 months','fees':15000},
    'python':{'duration': '2 months','fees':10000},
    'java':{'duration': '4 months','fees':17000}
}
print(course)

print( )
#iterate
print(course['php'])
print(course['php'] ['fees'])

print( )
#item
for k,v in course.items():
    print(k,v)

print( )
#accurate value 
for k,v in course.items():
    print(k,v['duration'],v['fees'])

print( )
#update
print(course)
course['java'] ['fees']=20000