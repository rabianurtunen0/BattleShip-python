#çap = input("Dairenin çapını giriniz: ")
#yarıçap = int(çap) / 2
#pi = 3.14159
#alan = pi * (yarıçap * yarıçap)
#print("Çapı", çap, "olan bir dairenin alanı", alan, "cm2'dir.")

#v1 = input("Toplama işlemi için ilk sayıyı giriniz: ")
#v2 = input("Toplama işlemi için ikinci sayıyı giriniz: ")
#sayı1 = int(v1)
#sayı2 = int(v2)
#print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

#veri = input("Bir sayı giriniz: ")
#sayı = int(veri)
#print ("Girdiğiniz sayının karesi:", sayı ** 2)

#ocak = mart = mayıs = temmuz = agustos = ekim = aralık = 31
#nisan = haziran = eylul = kasım = 30
#subat = 28
#birim_fiyat = 0.79
#aylık_sarfiyat = input("Aylık dogalgaz sarfiyat degerinizi m3 olarak giriniz: ")
#donem = input('''Hangi aya ait faturanızı hesaplamak istersiniz? :
#Lütfen ay adını küçük harflerle yazınız.\n''')
#ay = eval(donem)
#gunluk_sarfiyat = int(aylık_sarfiyat) / ay
#fatura = birim_fiyat * gunluk_sarfiyat * ay
#print("Günlük sarfiyatınız: \t", gunluk_sarfiyat, "\nTahmini fatura tutarınız: \t", fatura, "TL")

#veri = input("İşleminiz: ")
#sonuc = eval(veri)
#print(sonuc)

#sayı = int(input("Bir sayı giriniz: "))
#if sayı > 10:
#    print("Girdiğiniz sayı 10'dan büyüktür!")
#if sayı < 10:
#    print("Girdiğiniz sayı 10'dan küçüktür!")
#if sayı == 10:
#    print("Girdiğiniz sayı 10'dur!")

#parola = input("Parolanızı giriniz: ")
#if parola == "1258659":
#    print("Sisteme Hoş Geldiniz!")
#if parola != "1258659":
#    print("Hatalı Parola!!!")

#boy = int(input("Boyunuzu giriniz: "))
#if boy < 160:
#    print("Boyunuz kısa.")
#elif boy < 180:
#    print("Boyunuz normal.")
#else :
#    print("Boyunuz uzun.")

#kullanıcı_adı = input("Kullanıcı adını giriniz: ")
#parola = input("Parolanızı giriniz: ")
#uzunluk = len(kullanıcı_adı) + len(parola)
#mesaj = "Kullanıcı adı ve parolanız {} karakterden oluşuyor."
#print(mesaj.format(uzunluk))
#if uzunluk <= 40:
#    print("Sisteme Hoş Geldiniz.")
#else :
#    print("Kullanıcı adı ve parolanızın toplam karakter uzunluğu 40'tan fazla olmamalıdır. ")

#sayı = int(input("Bir sayı giriniz: "))
#if sayı % 2 == 0:
#    print("Girdiğiniz sayı çift sayıdır.")
#else:
#    print("Girdiğiniz sayı tek sayıdır.")

#bölünen = int(input("Bölünen sayınızı giriniz: "))
#bölen = int(input("Bölen sayınızı giriniz: "))
#sablon = "{} sayısı {} sayısına tam".format(bölünen,bölen)
#if bölünen % bölen == 0:
#    print(sablon, "bölünüyor.")
#else :
#    print(sablon, "bölünmüyor.")

#isim = input("İsminiz: ")
#print(isim == "Ferhat")

#kullanıcı = input("Kullanıcı adınız: ")
#if bool(kullanıcı) == True :
#    print("Teşekkürler!")
#else :
#    print("Kullanıcı adı alanı boş bırakılamaz!!")

#kullanıcı_adı = input("Kullanıcı adınızı giriniz: ")
#parola = input("Parolanızı giriniz: ")
#if kullanıcı_adı == "rabianurtunen0" and parola == "17807175848":
#    print("Sisteme Hoş Geldiniz...")
#else :
#    print("Kullanıcı adınız veya parolanız hatalı!!!")

#puan = int(input("Notunuzu Giriniz: "))
#if puan > 100 or puan < 0 :
#    print("Hatalı Giriş")
#elif puan >= 90 and puan <= 100 :
#    print("Harf notunuz A")
#elif puan >= 85 and puan <= 89 :
#    print("Harf notunuz A-")
#elif puan >= 80 and puan <= 84 :
#    print("Harf notunuz B+")
#elif puan >= 75 and puan <= 79 :
#    print("Harf notunuz B")
#elif puan >= 70 and puan <= 74 :
#    print("Harf notunuz B-")
#elif puan >= 65 and puan <= 69 :
#    print("Harf notunuz C+")
#elif puan >= 60 and puan <= 64 :
#    print("Harf notunuz C")
#elif puan >= 55 and puan <= 59 :
#    print("Harf notunuz C-")
#elif puan >= 50 and puan <= 54 :
#    print("Harf notunuz D+")
#elif puan >= 0 and puan <= 49 :
#    print("Harf notunuz FF")

#parola = input("Parolanız: ")
#if not parola:
#    print("Parola boş bırakılmaz!!")

import math

print("L", "İ", "N", "U", "X", sep=".")

giriş ="""
(1) = toplama
(2) = çıkarma
(3) = bölme
(4) = çarpma
(5) = üssünü alma
(6) = karekökünü alma
"""

print(giriş)
soru = int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
ilk_sayı = int(input("İlk sayınızı giriniz: "))
ikinci_sayı = int(input("İkinci sayınızı giriniz: "))

if soru == 1 :
    print(ilk_sayı + ikinci_sayı)
elif soru == 2 :
    print(ilk_sayı - ikinci_sayı)
elif soru == 3 :
    print(ilk_sayı / ikinci_sayı)
elif soru == 4:
    print(ilk_sayı * ikinci_sayı)
elif soru == 5 :
    print(ilk_sayı ** ikinci_sayı)
elif soru == 6 :
    print( math.sqrt(ilk_sayı))
    print( math.sqrt(ikinci_sayı))

