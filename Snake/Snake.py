import os

snakey=5
snakex=5
snkae_length=1

def printMap(field):
    for i in field:
        for j in i:
            print(j, end=" ")
        print()


field = [["□" for col in range(11)] for row in range(11)]
os.system('cls')
printMap(field)

#게임시작
input("========PushAnyKey========")
os.system('cls')
field[snakey][snakex] = "■"
printMap(field)

def moveRight():
    os.system('cls')
    global snakex
    field[snakey][snakex] = "□"
    snakex +=1
    field[snakey][snakex] = "■"
    printMap(field)

def moveLeft():
    os.system('cls')
    global snakex
    field[snakey][snakex] = "□"
    snakex -=1
    field[snakey][snakex] = "■"
    printMap(field)

def moveUp():
    os.system('cls')
    global snakey
    field[snakey][snakex] = "□"
    snakey -=1
    field[snakey][snakex] = "■"
    printMap(field)

def moveDown():
    os.system('cls')
    global snakey
    field[snakey][snakex] = "□"
    snakey +=1
    field[snakey][snakex] = "■"
    printMap(field)

moveDown()
input("Down")
moveDown()
input("Up")
moveUp()
input("left")
moveLeft()
