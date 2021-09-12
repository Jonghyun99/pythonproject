import os
import keyboard
import random
import threading

from time import sleep


snkae_length=1

#맵크기
filed_size=11

#시작위치
start_position = int(filed_size/2)

#시작위치변수
snake_y=start_position
snake_x=start_position

def printMap(field):
    for i in field:
        for j in i:
            print(j, end=" ")
        print()


field = [["□" for col in range(filed_size)] for row in range(filed_size)]
os.system('cls')
printMap(field)


#게임시작
os.system('cls')
field[start_position][start_position] = "■"
printMap(field)
print("========PushAnyArrowKey========")

def moveRight():
    os.system('cls')
    global snake_x
    field[snake_y][snake_x] = "□"
    snake_x +=1
    field[snake_y][snake_x] = "■"
    printMap(field)
    sleep(0.1)

def moveLeft():
    os.system('cls')
    global snake_x
    field[snake_y][snake_x] = "□"
    snake_x -=1
    field[snake_y][snake_x] = "■"
    printMap(field)
    sleep(0.1)

def moveUp():
    os.system('cls')
    global snake_y
    field[snake_y][snake_x] = "□"
    snake_y -=1
    field[snake_y][snake_x] = "■"
    printMap(field)
    sleep(0.1)

def moveDown():
    os.system('cls')
    global snake_y
    field[snake_y][snake_x] = "□"
    snake_y +=1
    field[snake_y][snake_x] = "■"
    printMap(field)
    sleep(0.1)

#포인트 생성함수
def getPoint():
    pointX = random.randrange(0,filed_size)
    pointY = random.randrange(0,filed_size)
    
    #포인트 생성 위치에 오브젝트 존재할 시 다른 곳으로 되돌림
    if(field[pointY][pointX] in ["■", "★"]):
        while field[pointY][pointX] in ["■", "★"]:
            pointX = random.randrange(0,filed_size)
            pointY = random.randrange(0,filed_size)
        field[pointY][pointX] = "★"
        printMap(field)
    else:
        field[pointY][pointX] = "★"
        printMap(field)
        
def controll():
    count=0
    while True:
            if keyboard.is_pressed('up'):
                moveUp()
                count+=1
            elif keyboard.is_pressed('down'):
                moveDown()
                count+=1
            elif keyboard.is_pressed('left'):
                moveLeft()
                count+=1
            elif keyboard.is_pressed('right'):
                moveRight()
                count+=1

            if(count==5):
                getPoint()
                count=0

controll()
            

      