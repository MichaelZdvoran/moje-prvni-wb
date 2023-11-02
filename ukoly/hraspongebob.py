import random

def utikani():
    zivoty = 3
    pozice_spongeboba = 0
    pozice_dinosaura = random.randint(1, 10)
    
    while True:
        print("Pozice SpongeBoba: " + str(pozice_spongeboba))
        print("Pozice dinosaura: " + str(pozice_dinosaura))
        
        akce = input("Chceš skočit (s) nebo sklouznout (k)? ")
        
        if akce == "s":
            pozice_spongeboba += random.randint(1, 3)
        elif akce == "k":
            pozice_spongeboba -= random.randint(1, 2)
        
        pozice_dinosaura += random.randint(1, 2)
        
        if pozice_spongeboba >= 10:
            print("Gratuluji, SpongeBob se dostal do domečku!")
            break
        elif pozice_dinosaura >= 10:
            print("Dinosaurus SpongeBoba chytil! Zbývající životy: " + str(zivoty - 1))
            zivoty -= 1
            if zivoty == 0:
                print("Hra skončila, SpongeBob má smůlu.")
                break

utikani()
