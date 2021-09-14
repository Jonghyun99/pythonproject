import os
import keyboard
import random
import threading

from time import sleep

#맵크기
filed_size=11

#시작위치
start_position = int(filed_size/2)

#시작위치변수
snake_y=start_position
snake_x=start_position

snake_position=[[snake_y,snake_x]]
    
#스레드 키 입력 변수
key=None

game_speed = 0.5
star_count = 0

#별 생성 주기
star_gen_cycle=5
star_list=[]

def printMap(field):
    for i in field:
        for j in i:
            print(j, end=" ")
        print()
    print("별 위치 : {0}".format(star_list))
    print("뱀 위치 : {0},{1}".format(snake_y,snake_x))
    # print(star_count)
    # print(snake_position)
    print("q나 r 누를 시 초기화")

#게임시작
def initGame():
    global field
    global snake_x
    global snake_y
    global star_count
    
    field = [["□" for col in range(filed_size)] for row in range(filed_size)]
    os.system('cls')
    printMap(field)

    snake_x=start_position
    snake_y=start_position
    star_count=0

    os.system('cls')
    field[start_position][start_position] = "■"
    printMap(field)
    print("========PushAnyArrowKey========")

def moveUp():
    os.system('cls')
    global snake_y
    field[snake_y][snake_x] = "□"
    snake_y -=1
    field[snake_y][snake_x] = "■"
    printMap(field)

def moveDown():
    os.system('cls')
    global snake_y
    field[snake_y][snake_x] = "□"
    snake_y +=1
    field[snake_y][snake_x] = "■"
    printMap(field)

def moveLeft():
    os.system('cls')
    global snake_x
    field[snake_y][snake_x] = "□"
    snake_x -=1
    field[snake_y][snake_x] = "■"
    printMap(field)

def moveRight():
    os.system('cls')
    global snake_x
    field[snake_y][snake_x] = "□"
    snake_x +=1
    field[snake_y][snake_x] = "■"
    printMap(field)
        

#별 생성함수
def generateStar():
    star_x = random.randrange(0,filed_size)
    star_y = random.randrange(0,filed_size)
    global star_list
    
    #별 생성 위치에 오브젝트 존재할 시 다른 곳으로 출력
    if(field[star_y][star_x] in ["■", "★"]):
        while field[star_y][star_x] in ["■", "★"]:
            star_x = random.randrange(0,filed_size)
            star_y = random.randrange(0,filed_size)
        field[star_y][star_x] = "★"
        printMap(field)
        star_list.append([star_y,star_x])
    else:
        field[star_y][star_x] = "★"
        printMap(field)
        star_list.append([star_y,star_x])

def getStar():
    for i in star_list:
        if i == [snake_y,snake_x]:
            star_list.remove([snake_y,snake_x])
        
def controll():
    while True:
        global star_count
        if key=='up':
            while (key=='up'):
                star_count+=1
                moveUp()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        elif key=='down':
            while (key=='down'):
                star_count+=1
                moveDown()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        elif key=='left':
            while (key=='left'):
                star_count+=1
                moveLeft()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        elif key=='right':
            while (key=='right'):
                star_count+=1
                moveRight()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        #게임초기화
        elif key=='q' or key=='r':
            break
        getStar()
    game()
            
def readKey():
    global key
    key=keyboard.read_key()
    sleep(0.1)
    threading.Thread(target=readKey,daemon=True).start()

# def grow():
#     global snake_position
#     global tail_x
#     global tail_y

#     if(len(snake_position)==1):
#         tail_y=snake_y
#         tail_x=snake_x
    
#     if(key=='up'):
#         tail_y=snake_y+1
#         snake_position.append([tail_y,tail_x])
#     if(key=='down'):
#         tail_y=snake_y-1
#         snake_position.append([tail_y,tail_x])
#     if(key=='left'):
#         tail_y=snake_x+1
#         snake_position.append([tail_y,tail_x])
#     if(key=='right'):
#         tail_y=snake_x-1
#         snake_position.append([tail_y,tail_x])

    

def game():
    try:
        initGame()
        readKey()
        controll()
    except IndexError as e:
        printMap(field)
        print("***********GAMEOVER***************")
        print(e)
        a = input("다시 하려면 q나 r 입력, 다른 거 입력하면 종료")
        if a in ('q','r'):
            game()
game()

      