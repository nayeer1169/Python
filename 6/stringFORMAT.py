w="welcome {} to {} the channel".format(2,4)
print(w)

z="welcome {0} to the {1} channel".format("back","main")
print(z)

s="welcome back to the channel guys {a} {b} {c} {d} {e} {f} {g} ".format(a="i",b="hope",c="you",d="guys",e="are",f="doing",g="good")
print(s)

r="welcome {b:10} to {a} channel".format(a=30,b=40)
print(r)
print( )
r="welcome {b:^10} to {a} channel".format(a=30,b=40)
print(r)
print( )
r="welcome {b:<10} to {a} channel".format(a=30,b=40)
print(r)
print( )
r="welcome {b:>10} to {a} channel".format(a=30,b=40)
print(r)