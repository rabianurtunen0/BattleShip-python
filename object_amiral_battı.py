from random import randint

class AmiralBatti():
    gemi2 = []
    gemi3 = []
    gemi4 = []

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

    def kordinat_yerlestir(self):
        while True:
            cakisma_var = False

            randx = randint(0, 9)
            randy = randint(0, 9)
            yerlesim = randint(0, 1)
            if yerlesim:
                if (randy > 0):
                    self.gemi2.append({
                        'x': randx,
                        'y': randy - 1,
                    })
                    self.gemi2.append({
                        'x': randx,
                        'y': randy,
                    })

                else:
                    self.gemi2.append({
                        'x': randx,
                        'y': randy + 1,
                    })
                    self.gemi2.append({
                        'x': randx,
                        'y': randy,
                    })
            else:
                if (randx > 0):
                    self.gemi2.append({
                        'x': randx - 1,
                        'y': randy,
                    })
                    self.gemi2.append({
                        'x': randx,
                        'y': randy,
                    })
                else:
                    self.gemi2.append({
                        'x': randx + 1,
                        'y': randy,
                    })
                    self.gemi2.append({
                        'x': randx,
                        'y': randy,
                    })

            randx = randint(0, 9)
            randy = randint(0, 9)
            yerlesim = randint(0, 1)
            if yerlesim:
                if (randy > 1):
                    self.gemi3.append({
                        'x': randx,
                        'y': randy - 2,
                    })
                    self.gemi3.append({
                        'x': randx,
                        'y': randy - 1,
                    })
                    self.gemi3.append({
                        'x': randx,
                        'y': randy,
                    })
                else:
                    self.gemi3.append({
                        'x': randx,
                        'y': randy + 2,
                    })
                    self.gemi3.append({
                        'x': randx,
                        'y': randy + 1,
                    })
                    self.gemi3.append({
                        'x': randx,
                        'y': randy,
                    })
            else:
                if (randx > 1):
                    self.gemi3.append({
                        'x': randx - 2,
                        'y': randy,
                    })
                    self.gemi3.append({
                        'x': randx - 1,
                        'y': randy,
                    })
                    self.gemi3.append({
                        'x': randx,
                        'y': randy,
                    })
                else:
                    self.gemi3.append({
                        'x': randx + 2,
                        'y': randy,
                    })
                    self.gemi3.append({
                        'x': randx + 1,
                        'y': randy,
                    })
                    self.gemi3.append({
                        'x': randx,
                        'y': randy,
                    })

            randx = randint(0, 9)
            randy = randint(0, 9)
            yerlesim = randint(0, 1)
            if yerlesim:
                if (randy > 2):
                    self.gemi4.append({
                        'x': randx,
                        'y': randy - 3,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy - 2,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy - 1,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy,
                    })
                else:
                    self.gemi4.append({
                        'x': randx,
                        'y': randy + 3,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy + 2,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy + 1,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy,
                    })
            else:
                if (randx > 2):
                    self.gemi4.append({
                        'x': randx - 3,
                        'y': randy,
                    })
                    self.gemi4.append({
                        'x': randx - 2,
                        'y': randy,
                    })
                    self.gemi4.append({
                        'x': randx - 1,
                        'y': randy,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy,
                    })
                else:
                    self.gemi4.append({
                        'x': randx + 3,
                        'y': randy,
                    })
                    self.gemi4.append({
                        'x': randx + 2,
                        'y': randy,
                    })
                    self.gemi4.append({
                        'x': randx + 1,
                        'y': randy,
                    })
                    self.gemi4.append({
                        'x': randx,
                        'y': randy,
                    })

            if gemi2['x'][0] == gemi3['x'][0] or gemi2['x'][0] == gemi3['x'][1] or gemi2['x'][0] == gemi3['x'][2] or \
                gemi2['x'][1] == gemi3['x'][0] or gemi2['x'][1] == gemi3['x'][1] or gemi2['x'][1] == gemi3['x'][2]:
                cakisma_var = True

            elif gemi2['y'][0] == gemi3['y'][0] or gemi2['y'][0] == gemi3['y'][1] or gemi2['y'][0] == gemi3['y'][2] or \
                gemi2['y'][1] == gemi3['y'][0] or gemi2['y'][1] == gemi3['y'][1] or gemi2['y'][1] == gemi3['y'][2]:
                cakisma_var = True

            elif gemi2['x'][0] == gemi4['x'][0] or gemi2['x'][0] == gemi4['x'][1] or \
                gemi2['x'][0] == gemi4['x'][2] or gemi2['x'][0] == gemi4['x'][3] or \
                gemi2['x'][1] == gemi4['x'][0] or gemi2['x'][1] == gemi4['x'][1] or \
                gemi2['x'][1] == gemi4['x'][2] or gemi2['x'][1] == gemi4['x'][3]:
                cakisma_var = True

            elif gemi2['y'][0] == gemi4['y'][0] or gemi2['y'][0] == gemi4['y'][1] or \
                gemi2['y'][0] == gemi4['y'][2] or gemi2['y'][0] == gemi4['y'][3] or \
                gemi2['y'][1] == gemi4['y'][0] or gemi2['y'][1] == gemi4['y'][1] or \
                gemi2['y'][1] == gemi4['y'][2] or gemi2['y'][1] == gemi4['y'][3]:
                cakisma_var = True

            elif gemi3['x'][0] == gemi4['x'][0] or gemi3['x'][0] == gemi4['x'][1] or \
                gemi3['x'][0] == gemi4['x'][2] or gemi3['x'][0] == gemi4['x'][3] or \
                gemi3['x'][1] == gemi4['x'][0] or gemi3['x'][1] == gemi4['x'][1] or \
                gemi3['x'][1] == gemi4['x'][2] or gemi3['x'][1] == gemi4['x'][3] or \
                gemi3['x'][2] == gemi4['x'][0] or gemi3['x'][2] == gemi4['x'][1] or \
                gemi3['x'][2] == gemi4['x'][2] or gemi3['x'][2] == gemi4['x'][3]:
                cakisma_var = True

            elif gemi3['y'][0] == gemi4['y'][0] or gemi3['y'][0] == gemi4['y'][1] or \
                gemi3['y'][0] == gemi4['y'][2] or gemi3['y'][0] == gemi4['y'][3] or \
                gemi3['y'][1] == gemi4['y'][0] or gemi3['y'][1] == gemi4['y'][1] or \
                gemi3['y'][1] == gemi4['y'][2] or gemi3['y'][1] == gemi4['y'][3] or \
                gemi3['y'][2] == gemi4['y'][0] or gemi3['y'][2] == gemi4['y'][1] or \
                gemi3['y'][2] == gemi4['y'][2] or gemi3['y'][2] == gemi4['y'][3]:
                cakisma_var = True

            if not cakisma_var:

                oyun.self.tahta[self.gemi2[0]['y']][self.gemi2[0]['x']] = 'O'
                self.tahta[self.gemi2[1]['y']][self.gemi2[1]['x']] = 'O'

                oyun.tahta[self.gemi3[0]['y']][self.gemi2[0]['x']] = 'O'
                oyun.tahta[self.gemi3[1]['y']][self.gemi2[1]['x']] = 'O'
                oyun.tahta[self.gemi2[2]['y']][self.gemi2[2]['x']] = 'O'

                oyun.tahta[self.gemi2[0]['y']][self.gemi2[0]['x']] = 'O'
                oyun.tahta[self.gemi2[1]['y']][self.gemi2[1]['x']] = 'O'
                oyun.tahta[self.gemi2[2]['y']][self.gemi2[2]['x']] = 'O'
                oyun.tahta[self.gemi2[3]['y']][self.gemi2[3]['x']] = 'O'
                break


                kordinat_yerlestir()
oyun.ekrana_bas()

""" def kontrol(self):
        for gemi in [self.gemi2, self.gemi3, self.gemi4]:
            for coordinate in self.gemi3:
                if gemi[0]['x'] == coordinate['x']: """

