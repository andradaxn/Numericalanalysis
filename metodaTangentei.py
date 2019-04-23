
eps=10**(-6)

stanga = raw_input('Alegeti capatul din stanga al intervalului: ')
st=float(stanga)

dreapta = raw_input('Alegeti capatul din dreapta al intervalului: ')
dr=float(dreapta)

xzero=(st+dr)/2

def fun(x):
    return x**3-x-1

def derivata(x):
    return 3*x**2-1
     
rezultate=[]
er=1

while (er>eps):
    x=xzero-(fun(xzero)/derivata(xzero))
    rezultate.append("%.6f" % xzero)
    xzero=x
    er=abs(x-xzero)
    
print rezultate





