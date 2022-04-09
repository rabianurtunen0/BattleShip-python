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

#import math

#giriş ="""
#(1) = toplama
#(2) = çıkarma
#(3) = bölme
#(4) = çarpma
#(5) = üssünü alma
#(6) = karekökünü alma
#"""

#print(giriş)
#soru = int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
#ilk_sayi = int(input("İlk sayınızı giriniz: "))
#ikinci_sayi = int(input("İkinci sayınızı giriniz: "))

#if soru == 1 :
#    print(ilk_sayi + ikinci_sayi)
#elif soru == 2 :
#    print(ilk_sayi - ikinci_sayi)
#elif soru == 3 :
#    print(ilk_sayi / ikinci_sayi)
#elif soru == 4:
#    print(ilk_sayi * ikinci_sayi)
#elif soru == 5 :
#    print(ilk_sayi ** ikinci_sayi)
#elif soru == 6 :
#    print( math.sqrt(ilk_sayi))
#    print( math.sqrt(ikinci_sayi))

#while True :
#    soru = input("Yapmak istediğiniz işlemin numarasını giriniz(Çıkmak için q): ")
#
#    if soru == "q" :
#        print("Çıkılıyor")
#        break

""""
a=0

while a <= 100 :
    if a % 2 == 0 :
        print(a)
    a += 1
"""
"""
for i in range(100):
    if i % 2 == 0 :
        print(i)
"""
"""
lorem = "yartu cok guzel bir yer!"

for i in lorem:
    print(i)
"""
"""
sayılar = "123456789"
for sayı in sayılar :
    print(int(sayı) ** 2)
"""
"""
sayılar = "123456789"

for i in sayılar:
    if int(i) > 3:
        print(i)
"""
"""
tr_karakter = "şçüğöİı"

parola = input("Parolanızı giriniz: ")
for karakter in parola :
    if karakter in tr_karakter :
        print("Türkçe karakter kullanmayınız!")
"""
"""
while True :
    parola = input("Bir parola belirleyiniz: ")
    if not parola:
        print("Parola bölümü boş geçilemez!!")
    elif len(parola)>8 or len(parola)<3:
        print("Parolanız 3 karakterden kısa ve 8 karakterden uzun olamaz!!")
    else:
        print("Yeni parolanız:", parola)
        break
"""
"""
izinli_karakterler = "0123456789+-*/= "
print(""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
"")
"""
"""
while True:
    veri = input("Yapmak istediğiniz işlemi giriniz(Çıkmak için q tuşuna basınız.): ")
    if veri == "q":
        print("Çıkılıyor...")
        break
    for s in veri :
        if s not in izinli_karakterler :
            print("Ne yaptığını sanıyorsun!!")
            quit()
    hesap = eval(veri)
    print(hesap)
"""
"""
for i in range(10, 0, -3):
    print(i)
"""
"""
print(*range(0,11), sep = ", ")
"""
"""
while True:
    sayi = int(input("Sayınızı giriniz: "))
    
    if sayi == 0:
        break
    elif sayi < 0:
        pass
    else:
        print(sayi)
"""
"""
while True:
    s = input("Bir sayı giriniz: ")

    if s == "iptal":
        print("Programdan çıkılıyor..")
        break
    if len(s) <= 3:
        continue
    print("En fazla üç haneli bir sayı girebilirsiniz!!")
"""
"""
a = 0
while True:
    print(a)
    a += 1
    if == 3:
        break;
    else:
        print("else çalıştı")
"""
""""
karakter_dizisi = "Python öğreniyoruz"
for karakter in karakter_dizisi:
    if karakter == "o":
        print("o harfi bulundu.")
else:
print("o harfi bulunamadı.")
"""
"""
ilk_metin = "mıyjhkjnıujnkghnjınıjmı"
ikinci_metin = "xrecscyurgkjbrtsfct"
fark = ""
print("Frak'ın ilk tanımlandığı zamanki kimlik numarası : ", id(fark))

for s in ilk_metin:
    if not s in ikinci_metin:
        if not s in fark:
            fark += s
print(fark)
print("Frak'ın program sonundaki kimlik numarası : ", id(fark))
"""
"""
d1 = open("isimler1.txt", encoding="utf-8")
d1_rows = d1.readlines()

d2 = open("isimler2.txt", encoding="cp1254")
d2_rows = d2.readlines()

for s in d1_rows:
    if s in d2_rows:
        print(s)

d1.close()
d2.close()
"""
"""
metin = ""Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır.""

harf = input("Sorgulamak istediğiniz harf: ")
sayı = ''

for s in metin:
    if harf == s:
        sayı += harf
print(len(sayı))
"""
"""
hakkında = open("hakkında.txt", encoding="utf-8")
harf = input("Sorgulmak istediğiniz harf: ")
sayı = 0

for karakter_dizisi in hakkında:
    print(repr(karakter_dizisi))
    for karakter in karakter_dizisi:
        if harf == karakter:
            sayı += 1
print(sayı)
hakkında.close()
"""
"""
ilk_sayi = input("İlk sayınızı giriniz: ")
ikinci_sayi = input("İkinci sayınızı giriniz: ")

try:
    sayi1 = int(ilk_sayi)
    sayi2 = int(ikinci_sayi)
    print(sayi1, "/", sayi2, "=", sayi1 / sayi2)
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!!")
except ValueError: #except (ZeroDivisionError, ValueError):
    print("Lütfen sadece sayı giriniz!!")
"""
"""
ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError) as hata:
    print("Bir hata oluştu")
    print(hata)
"""
"""
try:
    bölünen = int(input("Bölünecek sayıyı giriniz: "))
    bölen = int(input("Bölen sayıyı giriniz: "))
except ValueError:
    print("Lütfen sayı giriniz.")
else:
    try:
        print(bölünen/bölen)
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz.")
"""
"""
try:
    dosya = open("dosyaadı", "r")
    #...burada dosyayla bazı işlemler yapıyoruz...
    #...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()
"""
"""
tr_karakterler = "şçğüöıi"
parola = input("Parolanızı giriniz: ")

for i in parola:
    if i in tr_karakterler:
        raise TypeError("Parola'da türkçe karakter kullanılamaz.")
    else:
        pass
print("Parola kabul edildi.")
"""
"""
giriş = input("Merhaba, adın ne? ")
if len(giriş) == 0:
    raise AssertionError("İsim bölümü boş!!")
print("Hoşgeldiniz.")

giriş = input("Merhaba, adınız nedir? ")
assert len(giriş) !=0, "İsim bölümü boş."
print("Hoşgeldiniz.")
"""
"""
try:
    birtakım kodlar
except ValueError:
    print("Yanlış değer")
except ZeroDivisionError:
    print("Sıfıra bölme hatası")
except:
    print("Beklenmeyen bir hata oluştu!")
"""
"""
kardiz = "hbydgcurtgnjvnutkgndfukbnrtugksvfmvıtgk"
for karakter in range(len(kardiz)):
    print(kardiz[karakter])
"""


















print("Hello World")
exit()

if 6 > 2:
    print("Altı ikiden daha büyüktür.")

x = 9
y = "Konya"
print(x)
print(y)

x = str(5)
y = int(5)
z = float(5)
print(x)
print(y)
print(z)

x = 5
y = "Jhon"
print(type(x))
print(type(y))
#<class 'int'>
#<class 'str'>

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#Illegal variable names:
#2myvar = "John"
#my-var = "John"
#my var = "John"

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

x, y, z = "Orange", "Banana", "Cherry"
a = b = c = "Orange"
fruits = ["apple", "banana", "cherry"]
m, n, k = fruits
print(m)
print(n)
print(k)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x + y) #hata

x = 5
y = "John"
print(x, y)

x = "güzeldir"
def cumle():
    print("Hayat " + x)
cumle()

x = "a"
def myfunc():
    x = "b"
    print("Python is " + x)
myfunc()
print("Python is " + x)
#Python is b
#Python is a

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)
#Python is fantastic

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types: list, tuple, range
#Mapping Type: dict
#Set Types:	set, frozenset
#Boolean Type: bool
#Binary Types: bytes, bytearray, memoryview

x = "Hello World"	#str
x = 20	#int
x = 20.5 #x = 35e3	#float
x = 1j	#complex
x = ["apple", "banana", "cherry"]	#list
x = ("apple", "banana", "cherry")	#tuple
x = range(6)	#range
x = {"name" : "John", "age" : 36}	#dict
x = {"apple", "banana", "cherry"}	#set
x = frozenset({"apple", "banana", "cherry"})	#frozenset
x = True	#bool
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryview

x = str("Hello World")	#str
x = int(20)	#int
x = float(20.5)	#float
x = complex(1j)	#complex
x = list(("apple", "banana", "cherry"))	#list
x = tuple(("apple", "banana", "cherry"))	#tuple
x = range(6)	#range
x = dict(name="John", age=36)	#dict
x = set(("apple", "banana", "cherry"))	#set
x = frozenset(("apple", "banana", "cherry"))	#frozenset
x = bool(5)	#bool
x = bytes(5)	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryview


x = float(1)
y = int(2.8)
z = complex(x)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
#1.0
#2
#(1+0j)
#<class 'float'>
#<class 'int'>
#<class 'complex'>

import random
print(random.randrange(1, 10))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

a = "Hello, World"
print(a[1]) #e

for x in "banana":
    print(x)
#b
#a
#n
#a
#n
#a

a = "JHBYFDGBRJ vfhdbfyfbys"
print(len(a))
#22

txt = "The best things in life are free!"
print("free" in txt)
#True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#Yes, 'free' is present.

txt = "The best things in life are free!"
print("expensive" not in txt)
#True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#No, 'expensive' is NOT present.

b = "Hello, World!"
print(b[3:10])
#lo, Wor

b = "Hello, World!"
print(b[:5])
#Hello

b = "Hello, World!"
print(b[2:])
#llo, World!

b = "Hello, World!"
print(b[-5:-2])
#orl

a = "Hello, World!"
print(a.upper())
#HELLO, WORLD!

a = "Hello, World!"
print(a.lower())
#hello, world!

a = "   Nasılsın   "
print(a.strip())
#Nasılsın

a = "Hello, World!"
print(a.replace("H", "J"))
#Jello, World!

a = "Hello, World!"
b = a.split(",")
print(b)
#['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c)
#HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Hello World

age = 21
txt = "My name is John, and I am {}"
print(txt.format(age))
#My name is John, and I am 21

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#I want to pay 49.95 dollars for 3 pieces of item 567


#txt = "We are the so-called "Vikings" from the north." #hata
txt = "We are the so-called \"Vikings\" from the north."
#We are the so-called "Vikings" from the north.

txt = 'It\'s alright.'
print(txt)
#It's alright.

txt = "This will insert one \\ (backslash)."
print(txt)
#This will insert one \ (backslash).

txt = "Hello\nWorld!"
print(txt)
#Hello
#World!

txt = "Hello\rWorld!"
print(txt)
#Hello
#World!

txt = "Hello\tWorld!"
print(txt)
#Hello   World!

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
#HelloWorld!

#\f	- > Form Feed

#A backslash followed by three integers will result in a octal value: \ooo
txt = "\110\145\154\154\157"
print(txt)
#Hello

#A backslash followed by an 'x' and a hex number represents a hex value: \xhh
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
#Hello

###capitalize()###

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
#Hello, and welcome to my world.

txt = "python is FUN!"
x = txt.capitalize()
print (x)
#Python is fun!

txt = "36 is my age."
x = txt.capitalize()
print (x)
#36 is my age


###casefold()###

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
#hello, and welcome to my world!


###center()###

txt = "banana"
x = txt.center(20)
print(x)
#       banana

txt = "banana"
x = txt.center(20, "O")
print(x)
#OOOOOOObananaOOOOOOO


###count()###

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
#2

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
#1


###encode()###

txt = "My name is Ståle"
x = txt.encode() #UTF-8
print(x)
#b'My name is St\xc3\xe5le'

#string.encode(encoding=encoding, errors=errors)
#errors="strict" -> Varsayılan, hata durumunda hata verir.
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
#b'My name is St\\xe5le'
#b'My name is Stle'
#b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
#b'My name is St?le'
#b'My name is Ståle'


###endswith()###

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
#True

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
#True

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)
#False


###expandtabs()###

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
#H       e       l       l       o
#H       e       l       l       o
#H e l l o
#H   e   l   l   o
#H         e         l         l         o


###find()###

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
#7

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)
#1

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)
#8

txt = "Hello, welcome to my world."
print(txt.find("q"))
print(txt.index("q"))
#-1
#Traceback (most recent call last):
#  File "demo_ref_string_find_vs_index.py", line 4 in <module>
#    print(txt.index("q"))
#ValueError: substring not found


###format()###

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
#49.00

txt1 = "My name is {fname}, I'm {age}".format(fname = "Sema", age = "73")
txt2 = "My name is {0}, I'm {1}".format("Sema", 73)
txt3 = "My name is {}, I'm {}".format("Sema", 73)
print(txt1)
print(txt2)
print(txt3)
#My name is Sema, I'm 73
#My name is Sema, I'm 73
#My name is Sema, I'm 73

#Formating Types

txt = "We have {:<8} chickens."
print(txt.format(49))
#We have 49       chickens.

txt = "We have {:>8} chickens."
print(txt.format(49))
#We have       49 chickens.

txt = "We have {:^8} chickens."
print(txt.format(49))
#We have    49    chickens.

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
#The temperature is -      5 degrees.

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
#The temperature is between -3 and +7 degrees celsius.

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
#The temperature is between -3 and 7 degrees celsius.

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
#The temperature is between -3 and  7 degrees celsius.

txt = "The universe is {:,} years old."
print(txt.format(13800000000))
#The universe is 13,800,000,000 years old.

txt = "The universe is {:_} years old."
print(txt.format(13800000000))
#The universe is 13_800_000_000 years old.

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
#The binary version of 5 is 101

# :c -> unicode karaktere dönüştürür

txt = "We have {:d} chickens."
print(txt.format(0b101))
#We have 5 chickens.

txt = "We have {:e} chickens."
print(txt.format(5))
#We have 5.000000e+00 chickens.

txt = "We have {:E} chickens."
print(txt.format(5))
#We have 5.000000E+00 chickens.

txt = "The price is {:.2f} dollars."
print(txt.format(45))
txt = "The price is {:f} dollars."
print(txt.format(45))
#The price is 45.00 dollars.
#The price is 45.000000 dollars.

x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))
txt = "The price is {:f} dollars."
print(txt.format(x))
#The price is INF dollars.
#The price is inf dollars.












