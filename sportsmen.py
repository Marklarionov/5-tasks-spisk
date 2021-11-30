#Kmd=[] #tühi järjend
#Km=10 # esimine päev
#print("1. päeval pikkus oli ", Km)
#Kmd.append(Km)
#
#for p in range(2,8):
#    Km*=1.1 # > 10%
#    Kmd.append(round(Km,2))
#print(Kmd)
#print(Kmd[2])
#print(Kmd.index(16.11))
#Kmd.remove(10) #pop(0)
#print(Kmd,"listis on kokku" ,Kmd.count(16.11), "elemendid mis võrdub 16.11")
#print(len(Kmd), "on jäänud listis")

#po4tovi Index
Maakonnad=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","IdaVirumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
#    try:
#        Index=int(input())
#        if len(str(Index))==5:
#            break
#    except ValueError:
#        print("Valesti sisestatud index!")
#i_list=list(str(Index))
#s1=int(i_list[0]) #1->0,2->1...
#print(Maakonnad[s1-1])
#if s1 in [1,2,3]:
#    print("оставайтесь дома")
#else:
#    print("носите маска")

#Peremena mest
from random import *
#spisok=[]
#N=int(input("N=")) # >2
#for i in range(N):
#    spisok.append(randint(1,100))
#print(spisok)
#for s in spisok:
#    print(s)
#len(spisok)%2==0
##spisok_c=spisok.copy()
##spisok_c.reverse()
##print(spisok_c)

#pervyi=spisok[0]
#posledni=spisok[N-1] #-1
#spisok.pop(0)
#spisok.insert(0,posledni)

#OR
#spisok.remove(posledni)#?
#spisok.append(pervyi)

#bespolezny num

spisok=[]
N=int(input("N="))
for i in range(N):
    spisok.append(randint(1,100))
print(spisok)
max_=max(spisok)
print(max_)
max_2=max(spisok)/len(spisok)
print(max_2)
ind=spisok.index(max_)
spisok.pop(ind)
spisok.insert(ind,max_2)
print(max_2)
print(spisok)


#sort

spisok=[]
N=int(input("N="))
for i in range(N):
    spisok.append(randint(1,100))
spisok.sort()
print(spisok)
spisok.reverse()
spisok.sort(spisok.reverse())
print(spisok)