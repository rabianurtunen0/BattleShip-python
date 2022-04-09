
from random import randint
board = []
sayac = 0
puan = 250
for i in range(5):
    board.append(["0"]*5)

def print_board(board):
    for satir in board:
        print (" ".join(satir))
def rand(board):
    return randint(1,len(board)-1)

print("-" * 35)
print("Amiral battı oyununa hoş geldiniz")
print("-" * 35)
print("Puanınız:", puan)
print("-" * 35)
print_board(board)

gemi_satir = rand(board)
gemi_sutun = rand(board)
gemi1_satir = rand(board)
gemi1_sutun = rand(board)
gemi2_satir = rand(board)
gemi2_sutun = rand(board)

while True:
    if(gemi_satir == gemi1_satir and gemi_sutun == gemi1_sutun):
        gemi1_satir = rand(board)
        gemi1_sutun = rand(board)
        continue
    elif (gemi_satir == gemi2_satir and gemi_sutun == gemi2_sutun):
        gemi2_satir = rand(board)
        gemi2_sutun = rand(board)
        continue
    elif (gemi1_satir == gemi2_satir and gemi1_sutun == gemi2_sutun):
        gemi2_satir = rand(board)
        gemi2_sutun = rand(board)
        continue
    else:
        print("-" * 35)
        tahmin_satir = int(input("Satır giriniz: "))
        tahmin_sutun = int(input("Sütun giriniz: "))

        if (tahmin_satir == gemi_satir and tahmin_sutun == gemi_sutun)\
            or (tahmin_satir == gemi1_satir and tahmin_sutun == gemi1_sutun) \
            or (tahmin_satir == gemi2_satir and tahmin_sutun == gemi2_sutun):
            if board[tahmin_satir - 1][tahmin_sutun - 1] == "/":
                print("-" * 35)
                print("Zaten tahmin ettiniz")
                print_board(board)
                print(puan)
            else:
                print("-" * 35)
                print("Tebrikler gemiyi batırdınız!")
                board[tahmin_satir - 1][tahmin_sutun - 1] = "/"
                print("Puanınız:",puan)
                print("-" * 35)
                print_board(board)
                sayac += 1
        else:
            if (tahmin_satir < 0 or tahmin_sutun < 0) or (tahmin_satir >5 or tahmin_sutun >5):
                print("-" * 35)
                print("Alan sınırları dışında değer girdiniz")

            elif board[tahmin_satir - 1][tahmin_sutun - 1] == "X":
                print("-" * 35)
                print("Zaten tahmin ettiniz")
                print("-" * 35)
                print_board(board)
            else:
                print("-" * 35)
                print("Vuramadınız")
                board[tahmin_satir - 1][tahmin_sutun - 1] = "X"
                puan -= 10
                print("Puanınız:", puan)
                print("-" * 35)
                print_board(board)

            if sayac == 3:
                print("-" * 35)
                print("Tebrikler bütün gemileri batırdınız ve oyunu kazandınız")
                print("-" * 35)
                break

#######################################################################################################################

def ships():

    while True:

        direction2 = randint(1, 2)
        if direction2 == "1":
            ship2x1 = randint(0, 10 - 1)
            ship2y1 = randint(0, 10)
            ship2x2 = ship2x1 + 1
            ship2y2 = ship2y1
        elif direction2 == "2":
            ship2x1 = randint(0, 10)
            ship2y1 = randint(0, 10 - 1)
            ship2x2 = ship2x1
            ship2y2 = ship2y1 + 1

        direction3 = randint(1, 2)
        if direction3 == "1":
            ship3x1 = randint(0, 10 - 2)
            ship3y1 = randint(0, 10)
            ship3x2 = ship3x1 + 1
            ship3y2 = ship3y1
            ship3x3 = ship3x1 + 2
            ship3y3 = ship3y1
        elif direction3 == "2":
            ship3x1 = randint(0, 10)
            ship3y1 = randint(0, 10 - 2)
            ship3x2 = ship3x1
            ship3y2 = ship3y1 + 1
            ship3x3 = ship3x1
            ship3y3 = ship3y1 + 2

        direction4 = randint(1, 2)
        if direction4 == "1":
            ship4x1 = randint(0, 10 - 3)
            ship4y1 = randint(0, 10)
            ship4x2 = ship4x1 + 1
            ship4y2 = ship4y1
            ship4x3 = ship4x1 + 2
            ship4y3 = ship4y1
            ship4x4 = ship4x1 + 3
            ship4y4 = ship4y1
        elif direction4 == "2":
            ship4x1 = randint(0, 10)
            ship4y1 = randint(0, 10 - 3)
            ship4x2 = ship4x1
            ship4y2 = ship4y1 + 1
            ship4x3 = ship4x1
            ship4y3 = ship4y1 + 2
            ship4x4 = ship4x1
            ship4y4 = ship4y1 + 3

        ship2 = [ship2x1, ship2y1, ship2x2, ship2y2]
        ship3 = [ship3x1, ship3y1, ship3x2, ship3y2, ship3x3, ship3y3]
        ship4 = [ship4x1, ship4y1, ship4x2, ship4y2, ship4x3, ship4y3, ship4x4, ship4y4]

        while True:
            if (ship2[:2] == ship3[:2] and ship2[:2] == ship3[2:4] and ship2[:2] == ship3[4:]):
                continue
            elif (ship2[2:] == ship3[:2] and ship2[2:] == ship3[2:4] and ship2[2:] == ship3[4:]):
                continue
            elif (ship3[:2] == ship4[:2] and ship3[:2] == ship4[2:4] and
                  ship3[:2] == ship4[4:6] and ship3[:2] == ship4[6:]):
                continue
            elif (ship3[2:4] == ship4[:2] and ship3[2:4] == ship4[2:4] and
                  ship3[2:4] == ship4[4:6] and ship3[2:4] == ship4[6:]):
                continue
            elif (ship3[4:] == ship4[:2] and ship3[4:] == ship4[2:4] and
                  ship3[4:] == ship4[4:6] and ship3[4:] == ship4[6:]):
                continue
        return ship2, ship3, ship4

board = []
for i in range(10):
    board.append(["_"] * 10)

def board1(board):
    for row in board:
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


    if (row == ship[0][0] and column == ship[0][1]) or (row == ship[0][2] and column == ship[0][3]):        print("Tebrikler 2 numaralı gemiyi vurdunuz.")
        board[row - 1][column - 1] = "X"
        board1(board)

    if (board[ship[0][0]][ship[0][1]] == "X") and (board[ship[0][2]][ship[0][3]] == "X"):
        print("Tebrikler 2 numaralı gemiyi batırdınız.")

    elif (row == ship[1][0] and column == ship[1][1]) or (row == ship[1][2] and column == ship[1][3]) or
        (row == ship[1][4] and column == ship[1][5]):
        print("Tebrikler 3 numaralı gemiyi vurdunuz.")
        board[row - 1][column - 1] = "X"
        board1(board)

    if (board[ship[1][0]][ship[1][1]] == "X") and (board[ship[1][2]][ship[1][3]] == "X") and
        (board[ship[1][4]][ship[1][5]] == "X"):
        print("Tebrikler 3 numaralı gemiyi batırdınız.")

    elif (row == ship[2][0] and column == ship[2][1]) or (row == ship[2][2] and column == ship[2][3]) or
        (row == ship[2][4] and column == ship[2][5]) or (row == ship[2][6] and column == ship[2][7]):
        print("Tebrikler 4 numaralı gemiyi vurdunuz.")
        board[row - 1][column - 1] = "X"
        board1(board)

    if (board[ship[2][0]][ship[2][1]] == "X") and (board[ship[2][2]][ship[2][3]] == "X") and
        (board[ship[2][4]][ship[2][5]] == "X") and (board[ship[2][6]][ship[2][7]]):
        print("Tebrikler 4 numaralı gemiyi batırdınız.")

    else:
        print("Maalesef isabet ettiremediniz")
        board[row - 1][column - 1] = "/"


    board[ship2[0]][ship2[1]] = "*"
    board[ship2[2]][ship2[3]] = "*"
    board[ship3[0]][ship3[1]] = "*"
    board[ship3[2]][ship3[3]] = "*"
    board[ship3[4]][ship3[5]] = "*"
    board[ship4[0]][ship4[1]] = "*"
    board[ship4[2]][ship4[3]] = "*"
    board[ship4[4]][ship4[5]] = "*"
    board[ship4[6]][ship4[7]] = "*"
    board1(board)
    print("\n\n")

#######################################################################################################################

import random

class BattleshipGame:
    def __init__(self, num_of_players):
        if num_of_players == 1:
            self.players = [HumanPlayer("Player"), ComputerPlayer("The Computer")]
        else:
            self.players = [HumanPlayer("Player 1"), HumanPlayer("Player 2")]
        self.players[0].set_opponent(self.players[1])
        self.players[1].set_opponent(self.players[0])

    def play(self):
        self.players[0].position_fleet()
        self.players[1].position_fleet()

        input("Both fleets are ready to play. Press enter to play... ")
        winner = False
        first_players_turn = True
        while not winner:
            if first_players_turn:
                winner = self.players[0].take_turn()
                if winner:
                    print("Game over!", self.players[0].player_name, "wins!")
            else:
                winner = self.players[1].take_turn()
                if winner:
                    print("Game over!", self.players[1].player_name, "wins!")
            first_players_turn = not first_players_turn


class Board:
    def __init__(self):
        self.grid = [[" _"]*10 for i in range(10)]
        self.hit_count = 0

    def __str__(self):
        str_val = "  0 1 2 3 4 5 6 7 8 9\n"
        for i in range(10):
            str_val += str(i)
            for j in range(10):
                str_val += self.grid[i][j]
            if i != 9:
                str_val += "\n"
        return str_val

    def get_public_view(self):
        str_val = "  0 1 2 3 4 5 6 7 8 9\n"
        for i in range(10):
            str_val += str(i)
            for j in range(10):
                if self.grid[i][j] == " B":
                    str_val += " _"
                else:
                    str_val += self.grid[i][j]
            if i != 9:
                str_val += "\n"
        return str_val

    def add_boat(self, boat):
        width = 1
        height = 1
        if boat.orientation == "v":
            height = boat.size
        else:
            width = boat.size
        if (boat.x < 0) or (boat.y < 0) or (boat.x+width > 10) or (boat.y+height > 10):
            return False

        for x in range(width):
            for y in range(height):
                if self.grid[boat.y + y][boat.x + x] != " _":
                    return False

        for x in range(width):
            for y in range(height):
                self.grid[boat.y + y][boat.x + x] = " B"
        return True

    def attack(self, x, y):
        current_value = self.grid[y][x]
        if current_value == " B":
            self.grid[y][x] = " X"
            self.hit_count += 1
            return True
        elif current_value == " _":
            self.grid[y][x] = " O"
            return False
        else:
            return False

    def is_defeated(self):
        if self.hit_count == 17:
            return True
        else:
            return False


class Boat:
    def __init__(self, label, size):
        self.label = label
        self.size = size
        self.x = None
        self.y = None
        self.orientation = None

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_orientation(self, orientation):
        self.orientation = orientation


class HumanPlayer:
    def __init__(self, player_name):
        self.player_name = player_name
        self.board = Board()
        self.fleet = [Boat("Aircraft Carrier", 5), Boat("Battleship", 4), Boat("Submarine", 3), Boat("Destroyer", 3), \
                      Boat("Patrol Boat", 2)]
        self.opponent = None
        self.log = [0,0,0]

    def set_opponent(self, opponent):
        self.opponent = opponent

    def position_fleet(self):
        input(self.player_name+": Are you ready to position your fleet?  Press enter to begin! ")

        for boat in self.fleet:
            self.position_boat(boat)

        print("Your fleet is ready to play.  Your board is positioned as follows:")
        print(self.board)

    def position_boat(self, boat):
        print(self.board)
        print("You need to position a", boat.label, "of length", boat.size, "on the board above.")

        orientation = None
        while orientation is None:
            orientation = input("Would you like to use a vertical or horizontal orientation? (v/h) ")
            if (orientation != "v") and (orientation != "h"):
                print("You must enter a 'v' or a 'h'.  Please try again.")
                orientation = None

        position = None
        while position is None:
            try:
                position = input("Please enter the position for the top-left location of the boat. " + \
                                 " Use the form x,y (e.g., 1,3): ")
                coords = position.split(",")
                x = int(coords[0])
                y = int(coords[1])
                boat.set_orientation(orientation)
                boat.set_position(x,y)

                if not self.board.add_boat(boat):
                    raise Exception
            except ValueError:
                print("You must a valid position for the boat.  Please try again.")
                position = None
            except:
                print("You must choose a position that is (a) on the board and (b) doesn't intersect" + \
                      "with any other boats.")
                position = None

    def take_turn(self):
        # Display boards.
        print(self.player_name+"'s board:")
        print(self.board)
        print()
        print("Your view of "+self.opponent.player_name+"'s board:")
        print(self.opponent.board.get_public_view())
        # Display current statistics for player
        print(self.player_name, "Statistics\nAttacks: ", self.log[0], "\tHits: ", self.log[1], "\tMisses: ", self.log[2])
        # Get attack position.
        position = None
        while position is None:
            try:
                position = input("Please enter the position you would like to attack.  Use the form x,y (e.g., 1,3): ")
                coords = position.split(",")
                x = int(coords[0])
                y = int(coords[1])
                if (x < 0) or (x > 9) or (y < 0) or (y > 9):
                    raise Exception
                else:
                    break
            except:
                print("You must a valid position in the form x,y where both x and y are integers in the range of" + \
                      "0-9. Please try again.")
                position = None

        hit_flag = self.opponent.board.attack(x, y)
        self.log[0] += 1
        if hit_flag:
            self.log[1] += 1
            print("You hit a boat!")
        else:
            self.log[2] += 1
            print("You missed.")
        if self.opponent.board.is_defeated():
            return True
        else:
            return False


class ComputerPlayer:
    def __init__(self, player_name):
        self.player_name = player_name
        self.board = Board()
        self.fleet = [Boat("Aircraft Carrier", 5), Boat("Battleship", 4), Boat("Submarine", 3), Boat("Destroyer", 3), \
                      Boat("Patrol Boat", 2)]
        self.opponent = None
        self.log = [0,0,0]

    def set_opponent(self, opponent):
        self.opponent = opponent

    def position_fleet(self):
        for boat in self.fleet:
            self.position_boat(boat)

        input("The Computer's fleet is ready to play.  Press enter to continue...")

    def position_boat(self, boat):
        position = False
        while position == False:
            o = random.randint(0, 1)
            if o == 0:
                orientation = "v"
            else:
                orientation = "h"

            x = random.randint(1, 10) - 1
            y = random.randint(1, 10) - 1

            boat.set_orientation(orientation)
            boat.set_position(x,y)

            result = self.board.add_boat(boat)
            if result == True:
                position = True

    def take_turn(self):
        # Randomize attack position of Computer.
        x = random.randint(1, 10) - 1
        y = random.randint(1, 10) - 1

        print(self.player_name, "Statistics\nAttacks: ", self.log[0], "\tHits: ", self.log[1], "\tMisses: ",
              self.log[2])

        hit_flag = self.opponent.board.attack(x, y)
        self.log[0] += 1
        if hit_flag:
            self.log[1] += 1
            print("\nThe Computer hit a boat!")
        else:
            self.log[2] += 1
            print("\nThe Computer missed.")

        if self.opponent.board.is_defeated():
            return True
        else:
            return False


print("*************** Welcome to BATTLESHIP! ***************")
num_of_players = None
while num_of_players == None:
    try:
        num_of_players = int(input("Would you like to play with 1 player or 2? "))
        if (num_of_players != 1) and (num_of_players != 2):
            raise Exception()
    except:
        print("You must enter either 1 or 2.  Please try again.")
        num_of_players = None

game = BattleshipGame(num_of_players)
game.play()

#######################################################################################################################

import csv

def generateStartMap(size):
    startingMap = []
    for counter in range(size):
        currentLine = []
        for counter in range(size):
            currentLine.append("~")
        startingMap.append(currentLine)

    return startingMap

def shotToNumbers(coordinateString, headingsList):
    shotList = []
    shotList.append(int(coordinateString[1]))

    for column in headingsList:
        if coordinateString[0] == column:
            shotList.append(headingsList.index(column))
    return shotList

def checkHit(shot, map):
    if map[shot[0]][shot[1]] == "O":
        return ["X", "Miss!"]
    elif map[shot[0]][shot[1]] == "B":
        return ["B", "You hit the BATTLESHIP!"]
    elif map[shot[0]][shot[1]] == "S":
        return ["S", "You hit the SUBMARINE!"]
    elif map[shot[0]][shot[1]] == "D":
        return ["D", "You hit the DESTROYER!"]
    elif map[shot[0]][shot[1]] == "C":
        return ["C", "You hit the CARRIER!"]

def updateMap(lastShotCell, lastShotResult, map):
    map[lastShotCell[0]][lastShotCell[1]] = lastShotResult
    return map

def checkShipStatus(shipList, shipMap):
    shipStatus = []
    for index in range(len(shipList)):
        shipStatus.append(False)
    for index in range(len(shipList)):
        for list in shipMap:
            if shipList[index] in list:
                shipStatus[index] = True
    return shipStatus

gridSize = 10
validRows = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
validColumns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
shipSymbols = ["B", "S", "D", "C"]
shipNames = ["BATTLESHIP", "SUBMARINE", "DESTROYER", "CARRIER"]
playing = True

print("---------------------------\n"
      "        BATTLESHIPS\n"
      "---------------------------\n")

while playing:

    fileName = "battleshipMap.txt"
    accessMode = "r"
    shipMap = []

    try:
        with open(fileName, accessMode) as fileData:
            shipLocations = csv.reader(fileData)
            for row in shipLocations:
                shipMap.append(row)
    except FileNotFoundError:
        print("Sorry, there was an error loading a required file.")

    while True:
        difficulty = input("What difficulty would you like to play? (easy/hard) ").lower()
        if difficulty == "easy":
            missileCount = 50
            break
        elif difficulty == "hard":
            missileCount = 35
            break
        else:
            print("Please enter a valid difficulty setting.")

    currentMap = generateStartMap(gridSize)
    previousShots = []

    while missileCount > 0:
        print("---------------------------")
        print("  " + " ".join(validColumns))
        for counter in range(gridSize):
            print(str(counter) + " " + " ".join(currentMap[counter]))

        print("---------------------------\n"
              "MISSILES REMAINING: " + str(missileCount))

        while True:
            userShot = input("Enter the coordinates you wish to shoot: ").upper()
            if len(userShot) != 2:
                print("Please enter a valid coordinate:")
            elif userShot in previousShots:
                print("You've already shot there, pick a different coordinate.")
            elif userShot[0] not in validColumns or userShot[1] not in validRows:
                print("Please choose a coordinate in range.")
            else:
                previousShots.append(userShot)
                shotCoordinateList = shotToNumbers(userShot, validColumns)
                break

        print("---------------------------")

        shotResult = checkHit(shotCoordinateList, shipMap)
        print(shotResult[1])

        shipMap = updateMap(shotCoordinateList, "X", shipMap)

        shipsStillAlive = checkShipStatus(shipSymbols, shipMap)
        for index in range(len(shipsStillAlive)):
            if shipsStillAlive[index]:
                print("The " + shipNames[index] + " still sails!")
            else:
                print("You have sunk the " + shipNames[index] + "!")

        currentMap = updateMap(shotCoordinateList, shotResult[0], currentMap)

        if True not in shipsStillAlive:
            print("Good shooting! You have destroyed the enemy fleet!")
            break

        missileCount -= 1
        if missileCount == 0:
            print("Looks like the enemy fleet has escaped the harbour! You had better get your crew in order Admiral!")

    print("---------------------------")
    userContinue = input("Would you like to play again? (Y/N) ").upper()
    while True:
        if userContinue == "Y":
            playing = True
            break
        elif userContinue == "N":
            playing = False
            break
        else:
            print("Unknown inout, please enter Y or N")


print("\nThanks for playing!")








