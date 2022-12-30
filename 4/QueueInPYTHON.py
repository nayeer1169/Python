l=[]
while True:
    c=int(input('''
    1. Enqueue Elements
    2. Dequeue Elements
    3. Front Elements
    4. Last Elements
    5. Display
    6. EXIT
    '''))
    if c==1:
        n=input("Enter the value :-  ")
        l.append(n)
        print (l)
    elif c==2:
        if len(l)==0:
            print("Empty stack")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty stack")
        else:
            print("First queue value :- ",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty stack")
        else:
            print("Last queue value :- ",l[-1])
    elif c==5:
        print("display queue ",l)
    elif c==6:
        break;
    else:
        print("Invalid Operation")
