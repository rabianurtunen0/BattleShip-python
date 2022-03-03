import math

giriş ="""
(1) = toplama
(2) = çıkarma
(3) = bölme
(4) = çarpma
(5) = üs alma
(6) = karekökünü alma
"""

print(giriş)
soru = int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
ilk_sayı = int(input("İlk sayınızı giriniz: "))
ikinci_sayı = int(input("İkinci sayınızı giriniz: "))

if soru == 1 :
    print( ilk_sayı + ikinci_sayı)
elif soru == 2 :
    print( ilk_sayı - ikinci_sayı)
elif soru == 3 :
    print( ilk_sayı / ikinci_sayı)
elif soru == 4:
    print(ilk_sayı * ikinci_sayı)
elif soru == 5 :
    print( ilk_sayı ** ikinci_sayı)
elif soru == 6 :
    print( math.sqrt(ilk_sayı))
    print( math.sqrt(ikinci_sayı))

