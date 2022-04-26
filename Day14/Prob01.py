
t=[10,12,13]
y=[10,12,14]

class greter(Exception):
    pass

class lesser(Exception):
    pass

class notequl(Exception):
    pass

class eual(Exception):
    pass

age=9
try:
    if len(y)>len(t):
        raise lesser("second list  is greater ")
    elif t==y and len(t)==len(y):
        raise eual("WOWOWOW both list are equal in length and elements")
    elif len(t)> len(y):
        raise greter(" 1 st list is greter in the lenght")
    elif t != y:
        raise notequl("The list are not equal....")

except greter as L:
    print(L)
except lesser as le:
    print(le)
except notequl as e:
    print(e)
except eual as eu:
    print(eu)
finally:
    print("process completed ")
