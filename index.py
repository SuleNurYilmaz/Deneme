liste=[2,3,2,3,21,2,1]
n=int(input("listedeki sayıyı giriniz:" ))
while(liste.count(n)>0):
    print("index:",liste.index(n))
    liste.remove(n)
    
