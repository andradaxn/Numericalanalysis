stanga = raw_input('Alegeti capatul din stanga al intervalului: ')
st=float(stanga)

dreapta = raw_input('Alegeti capatul din dreapta al intervalului: ')
dr=float(dreapta)


i=1
rezultate=[]

def fun(x):
    return x**2-x

while i<=6:
    xzero=st-(fun(st)*(dr-st))/(fun(dr)-fun(st))
    st=xzero
    i+=1
    rezultate.append("%.6f" % xzero)
  

print rezultate

