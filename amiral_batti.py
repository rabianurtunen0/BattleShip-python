from random import randint

class AmiralBatti():

    tahta = []
    def __init__(self):
        for x in range(0, 10):
            self.tahta.append([])
            for y in range(0, 10):
                self.tahta[x].append('_')

    def ekrana_bas(self):
        for row in self.tahta:
            print(" ".join(row))


oyun = AmiralBatti()

def gemi_yerlestir():
    while True:
        cakisma_var = False

        gemi2x1 = randint(0, 9)
        gemi2y1 = randint(0, 9)
        yerlesim = randint(0, 1)  # 0 gelirse x ekseninde yerleştirsin 1se y ekseninde
        if yerlesim:
            if (gemi2y1 > 0):
                gemi2y2 = gemi2y1 - 1
                gemi2x2 = gemi2x1
            else:
                gemi2y2 = gemi2y1 + 1
                gemi2x2 = gemi2x1
        else:
            if (gemi2x1 > 0):
                gemi2x2 = gemi2x1 - 1
                gemi2y2 = gemi2y1
            else:
                gemi2x2 = gemi2x1 + 1
                gemi2y2 = gemi2y1

        gemi3x1 = randint(0, 9)
        gemi3y1 = randint(0, 9)
        yerlesim = randint(0, 1)  # 0 gelirse x ekseninde yerleştirsin 1se y ekseninde
        if yerlesim:
            if (gemi3y1 > 1):
                gemi3y2 = gemi3y1 - 1
                gemi3y3 = gemi3y1 - 2
                gemi3x2 = gemi3x1
                gemi3x3 = gemi3x1
            else:
                gemi3y2 = gemi3y1 + 1
                gemi3y3 = gemi3y1 + 2
                gemi3x2 = gemi3x1
                gemi3x3 = gemi3x1
        else:
            if (gemi3x1 > 1):
                gemi3x2 = gemi3x1 - 1
                gemi3x3 = gemi3x1 - 2
                gemi3y2 = gemi3y1
                gemi3y3 = gemi3y1
            else:
                gemi3x2 = gemi3x1 + 1
                gemi3x3 = gemi3x1 + 2
                gemi3y2 = gemi3y1
                gemi3y3 = gemi3y1

        gemi4x1 = randint(0, 9)
        gemi4y1 = randint(0, 9)
        yerlesim = randint(0, 1)  # 0 gelirse x ekseninde yerleştirsin 1se y ekseninde
        if yerlesim:
            if (gemi4y1 > 2):
                gemi4y2 = gemi4y1 - 1
                gemi4y3 = gemi4y1 - 2
                gemi4y4 = gemi4y1 - 3
                gemi4x2 = gemi4x1
                gemi4x3 = gemi4x1
                gemi4x4 = gemi4x1
            else:
                gemi4y2 = gemi4y1 + 1
                gemi4y3 = gemi4y1 + 2
                gemi4y4 = gemi4y1 + 3
                gemi4x2 = gemi4x1
                gemi4x3 = gemi4x1
                gemi4x4 = gemi4x1
        else:
            if (gemi4x1 > 2):
                gemi4x2 = gemi4x1 - 1
                gemi4x3 = gemi4x1 - 2
                gemi4x4 = gemi4x1 - 3
                gemi4y2 = gemi4y1
                gemi4y3 = gemi4y1
                gemi4y4 = gemi4y1
            else:
                gemi4x2 = gemi4x1 + 1
                gemi4x3 = gemi4x1 + 2
                gemi4x4 = gemi4x1 + 3
                gemi4y2 = gemi4y1
                gemi4y3 = gemi4y1
                gemi4y4 = gemi4y1

        if gemi2x1 == gemi3x1 or gemi2x1 == gemi3x2 or gemi2x1 == gemi3x3 or \
            gemi2x2 == gemi3x1 or gemi2x2 == gemi3x2 or gemi2x2 == gemi3x3:
            cakisma_var = True

        elif gemi2y1 == gemi3y1 or gemi2y1 == gemi3y2 or gemi2y1 == gemi3y3 or \
            gemi2y2 == gemi3y1 or gemi2y2 == gemi3y2 or gemi2y2 == gemi3y3:
            cakisma_var = True

        elif gemi2x1 == gemi4x1 or gemi2x1 == gemi4x2 or gemi2x1 == gemi4x3 or gemi2x1 == gemi4x4 or \
            gemi2x2 == gemi4x1 or gemi2x2 == gemi4x2 or gemi2x2 == gemi4x3 or gemi2x2 == gemi4x4:
            cakisma_var = True

        elif gemi2y1 == gemi4y1 or gemi2y1 == gemi4y2 or gemi2y1 == gemi4y3 or gemi2y1 == gemi4y4 or \
            gemi2y2 == gemi4y1 or gemi2y2 == gemi4y2 or gemi2y2 == gemi4y3 or gemi2y2 == gemi4y4:
            cakisma_var = True

        elif gemi3x1 == gemi4x1 or gemi3x1 == gemi4x2 or gemi3x1 == gemi4x3 or gemi3x1 == gemi4x4 or \
            gemi3x2 == gemi4x1 or gemi3x2 == gemi4x2 or gemi3x2 == gemi4x3 or gemi3x2 == gemi4x4 or \
            gemi3x3 == gemi4x1 or gemi3x3 == gemi4x2 or gemi3x3 == gemi4x3 or gemi3x3 == gemi4x4:
            cakisma_var = True

        elif gemi3y1 == gemi4y1 or gemi3y1 == gemi4y2 or gemi3y1 == gemi4y3 or gemi3y1 == gemi4y4 or \
            gemi3y2 == gemi4y1 or gemi3y2 == gemi4y2 or gemi3y2 == gemi4y3 or gemi3y2 == gemi4y4 or \
            gemi3y3 == gemi4y1 or gemi3y3 == gemi4y2 or gemi3y3 == gemi4y3 or gemi3y3 == gemi4y4:
            cakisma_var = True

        if not cakisma_var:
            oyun.tahta[gemi2y1][gemi2x1] = 'O'
            oyun.tahta[gemi2y2][gemi2x2] = 'O'

            oyun.tahta[gemi3y1][gemi3x1] = 'O'
            oyun.tahta[gemi3y2][gemi3x2] = 'O'
            oyun.tahta[gemi3y3][gemi3x3] = 'O'

            oyun.tahta[gemi4y1][gemi4x1] = 'O'
            oyun.tahta[gemi4y2][gemi4x2] = 'O'
            oyun.tahta[gemi4y3][gemi4x3] = 'O'
            oyun.tahta[gemi4y4][gemi4x4] = 'O'
            break

gemi_yerlestir()
oyun.ekrana_bas()

while True:
    try:
        x = int(input("Vurmak istediğiniz noktayı giriniz x: ")) - 1
        y = int(input("Vurmak istediğiniz noktayı giriniz y: ")) - 1
        if x > 10 or y > 10:
            print("Lütfen boyut aralıklarında değer giriniz.")
            continue

    except ValueError:
        print("Lütfen tam sayı giriniz.")
        continue


    if (y == gemi2y1 and x == gemi2x1) or \
        (y == gemi2y2 and x == gemi2x2):
        print("2 numaralı gemiyi vurdunuz")
        oyun.tahta[y][x] = 'X'

    elif (y == gemi3y1 and x == gemi3x1) or \
        (y == gemi3y2 and x == gemi3x2) or \
        (y == gemi3y3 and x == gemi3x3):
        print("3 numaralı gemiyi vurdunuz")
        oyun.tahta[y][x] = 'X'

    elif (y == gemi4y1 and x == gemi4x1) or \
        (y == gemi4y2 and x == gemi4x2) or \
        (y == gemi4y3 and x == gemi4x3) or \
        (y == gemi4y4 and x == gemi4x4):
        print("4 numaralı gemiyi vurdunuz")
        oyun.tahta[y][x] = 'X'

    else:
        print("Vuramadınız")



