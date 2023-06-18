def upper(string):
    up=""
    for i in string:
        p=ord(i)
        if p>=97 and p<=122:
            up=up+chr(p-32)
        else:
            up=up+chr(p)
    return up

def lower(string):
    lo=""
    for i in string:
        p=ord(i)
        if p>=65 and p<=90:
            lo+=chr(p+32)
        else:
            lo+=x
    return lo    



def islower(string):

    for i in string:
        y=ord(i)
        if y>=65 and y<=90:
            return False
            
        else:
            continue
    return True


def isupper(string):

    for i in string:
        y=ord(i)
        if y>=97 and y<=122:
            return False
            
        else:
            continue
                        
    return True

def isalpha(string):
    for x in string:
        p=ord(x)
        if p>=97 and p<=122:
            continue
        elif p>=65 and p<=90:
            continue
        else:
            return False
    return True

def isdigit(string):
    for x in string:
        p=ord(x)
        if p>=48 and p<=57:
            continue
        else:
            return False
    return True

def isalphanum(string):
    if type(string)==str:
        for i in string:
            if 0<=ord(i)<=47:
                return False
            elif 58<=ord(i)<=64:
                return False
            elif 91<=ord(i)<=96:
                return False
            elif 123<=ord(i)<=127:
                return False
            
            else:
                continue
        return True
    else:
        return 'invalid input please enter string'


def  swap(string):
    q=""
    for i in string:
        k=ord(i)
        if k>=65 and k<=90:
            m=k+32
            q=q+chr(m)
        elif k>=97 and k<=122:
            n=k-32
            q=q+chr(n)
        else:
            q=q+i
    return q 
