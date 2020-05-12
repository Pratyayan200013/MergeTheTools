s=input("")
k=int(input(""))
def merg_the_tool(n,a):
    b=len(n)//a
    l=[]
    g=[]
    for i in n:
        l.append(i)
    for i in range(b):
        t1=""
        u1=""
        for j in range(a):
            t1+=l[j]
        for h in t1:
            if h not in u1:
                u1+=h
        g.append(u1)
        for e in t1:
            if e in l:
                l.remove(e)
    for f in g:
        print(f)
merg_the_tool(s,k)
