from math import sqrt

a,b,c=3,5,2
print("Rezolvarea ecuatiei de gradul 2 : {0}X^2+{1}X+{2}=0".format(a,b,c))
delta=pow(b,2)-4*a*c

if delta<0:
    print("Delta este {0}.Ecuatia nu are solutii reale".format(delta))
elif delta==0:
    x1=-b/(2*a)
    print("Delta este 0. X1=X2={0}".format(x1))
else:
    print("Delta este pozitiv")
    x1=(-b-sqrt(delta))/(2*a)
    x2=(-b+sqrt(delta))/(2*a)
    print("Solutiile ecuatiei: X1={0} si X2={1}".format(x1,x2))