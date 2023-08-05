def mult(*var):
    res=1
    if(len(var)==0):
        return 0
    for i in var:
        res*=i
    return res