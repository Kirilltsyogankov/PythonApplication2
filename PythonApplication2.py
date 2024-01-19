from ssl import match_hostname
from threading import main_thread
from daletetime import *
from random import *
#11
ta=int.today().year()
sp=date(int(input("sünniaasta")),int(input("Sünnikuu: ")), int(input("Sünnipäev: "))).year
if (ta-sp)%5==0:
    print("Juubel")
else:
    print("Tavaline sünnipäaev")




#14
math=int(input("Bussi math: "))
i=int(input("Inimeste arv: "))
ba=(i/math) #2,3->2
if i%math!=0:
    ba+=1
vb=i%maht
print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))
