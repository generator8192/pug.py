import time as ST

def obska(a, b, t):
    if t == 2:
        return(a + (b * a))
    else:
        if a == 0: a = 0.001 
        return(a - (b / a))

def laba(i, x):
    ST.sleep(i)
    return(x)

    
