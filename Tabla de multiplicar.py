#Tabla de multiplicar
a=int(input("Inserte la tabla que quiera: "))
b=1
for b in range (1,11):
    c=a*b
    print(a,"*",b,"=",c)
    b+=1

if c == 100:
    print("jamon we")