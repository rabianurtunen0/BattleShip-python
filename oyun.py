import random
from random import randint
"""
while True:
    print(""
          - -------------------------------
    AMİRAL BATTI OYUNUNA HOŞ GELDİNİZ

    Menü:

    (1) Oyuna Başla - Kolay Seviye
    (2) Oyuna Başla - Orta Seviye
    (3) Oyuna Başla - Zor Seviye
    (4) Yüksek Skorlar
    - -------------------------------
    "")
    
    while True:
        soru = input("Menü'den seçmek istediğiniz seçeneğin numarasını giriniz: ")
        if soru == "1":
            atishakki = 100
            break
        elif soru == "2":
            atishakki = 35
            break
        elif soru == "3":
            atishakki = 20 
            break
        elif soru == "4":
            print("Yüksek Skorlar")
            yuksekskorlar = open("yuksekskorlar.txt", "a")
            print(yuksekskorlar.read(), sep="\n")
            yuksekskorlar.close()
            break
            
        else:
            print("Lütfen yukarıdaki sayılardan birini giriniz.")
    
"""

class Battleship:
    board = []

    for i in range(10):
        board.append(["_"] * 10)

    def board1(self, board):
        for row in Battleship.board:
            print(" ".join(row))

    print("\n")
    board1(board)
    print("\n")






while True:
    row = input("Satır numaranızı giriniz: ")
    column = input("Sütun numaranızı giriniz: ")
    try:
        row = int(row)
        column = int(column)
        break
    except ValueError:
        print("Lütfen tamsayı giriniz.")
        continue

if row > 10 or column > 10:
    print("Lütfen oyun alanının dışına çıkmayınız.")
    row = int(input("Satır numaranızı giriniz: "))
    column = int(input("Sütun numaranızı giriniz: "))

