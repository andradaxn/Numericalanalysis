import intervals as I

def fun(x):
    return x**2-x

stanga = raw_input('Alegeti capatul din stanga al intervalului: ')
st=float(stanga)

dreapta = raw_input('Alegeti capatul din dreapta al intervalului: ')
dr=float(dreapta)

interval=I.closed(st, dr)
print interval
  
i=1
rezultate=[]


while i<=6:
    xzero=(st+dr)/2
    if(fun(xzero)*fun(st)<0):
         dr=xzero
    else:
         st=xzero
    i+=1
    rezultate.append("%.4f" % xzero)

print rezultate

     
     


