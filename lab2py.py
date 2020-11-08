x=int(input("masukan nilai x ="))
y=int(input("masukan nilai y ="))
z=int(input("masukan nilai z ="))

if (x>y) and (x>z) :
    print(f"nilai terbesar adalah x = {x}")
elif (y>x) and (y>z) :
    print(f"nilai terbesar adalah y = {y}")
elif (z>x) and (z>y) :
    print(f"nilai terbesar adalah z = {z}")
else:
    print ("tidak ada nilai yang lebih besar")