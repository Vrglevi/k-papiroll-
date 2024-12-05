import random



def kopapirollo():
    igaz=True
    cuccok=["olló","papir","kő"]
    proba=1
    while igaz:
        gep=random.choice(cuccok)
        print(str(proba) + ". Próba")
        print(gep)
        valasz=input("Válasz egy cuccot kő, papir, olló : ")
        if valasz in  cuccok:
            if valasz == gep:
                print("Döntetlen")
                proba+=1
            elif valasz == "olló" and gep == "papir":
                print("Nyertél")
                igaz=False
            elif valasz == "papir" and gep == "kő":
                print ("Nyertél")
                igaz=False
            elif valasz == "kő" and gep == "olló":
                print ("Nyertél")
                igaz=False
            else:
                print ("Nem nyert próbálkozz újra")
                proba+=1
        else:
            print("Nem jó cucc")
        
    print("Gratulálok")
    print(str(proba) + " Próbából sikerűlt legyőzni a gépet." )





kopapirollo()
igaz2=True
while igaz2:
    ujra=input("Szeretnél még játszani y/n: ")
    if ujra == "n":
        print ("Viszlát")
        igaz2=False
    elif ujra == "y":
       kopapirollo()
    else:
        print("igen vagy nem")