l=[]
while True:

    c=int(input('''
    1. Push Elements
    2. Pop Elements
    3. Peek Elements
    4. Display
    5. EXIT
    '''))
    if c==1:
        n=input("Enter the value :-  ")
        l.append(n)
        print (l)
    elif c==2:
        if len(l)==0:
            print("Empty stack")
        else:     
           p=l.pop() 
           print (p)
           print(l)
    elif c==3:
        if len(l)==0:
            print("Empty stack")
        else:
            print("Last value is :-",l[-1])
    elif c==4:
        print("Display Value",l)
    elif c==5:
        break;
    else:
        print("Invalid choice")
