import pug

def stage1(a, b, c):
    if a != c:
        if a > c:
            a = int(pug.obska(a, b, 0))
        else:
            a = int(pug.obska(a, b, 2))
        return a, b
    else:
        return(a)

tr = 0

def stage2(l, i):
    output = ""
    global tr
    if tr >= len(i):
        return(i)
    for q in range(len(l)):
        if l[q] == i[tr]:
            tr += 1
            output = i[:tr]
            return(output)
    return(i[:tr])
