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

snake_position=[[snake_y,snake_x],[snake_y,snake_x],[snake_y,snake_x]]
    
#스레드 키 입력 변수
key=None

game_speed = 0.2
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
    print(snake_position)
    print("q나 r 누를 시 초기화")

#초기화
def initGame():
    global field
    global snake_x
    global snake_y
    global star_count
    global snake_position
    global star_list

    if len(snake_position)>=3:
        del snake_position
    if len(star_list)>=1:
        del star_list
    snake_position=[[start_position,start_position],[start_position,start_position],[start_position,start_position]]
    star_list=[]
    field = [["□" for col in range(filed_size)] for row in range(filed_size)]
    os.system('cls')
    printMap(field)

    star_count=0

    os.system('cls')
    for i in snake_position:
        field[i[0]][i[1]] = "■"
    printMap(field)
    print("========PushAnyArrowKey========")

def moveUp():
    os.system('cls')
    cnt = len(snake_position) -1
    field[snake_position[cnt][0]][snake_position[cnt][1]] = "□"
    while cnt>=1:
        snake_position[cnt] = snake_position[cnt-1]
        cnt-=1
    snake_position[0] = [snake_position[0][0]-1,snake_position[0][1]]
    for i in snake_position:
        field[i[0]][i[1]] = "■"
    printMap(field)

def moveDown():
    os.system('cls')
    cnt = len(snake_position) -1
    field[snake_position[cnt][0]][snake_position[cnt][1]] = "□"
    while cnt>=1:
        snake_position[cnt] = snake_position[cnt-1]
        cnt-=1
    snake_position[0] = [snake_position[0][0]+1,snake_position[0][1]]
    for i in snake_position:
        field[i[0]][i[1]] = "■"
    printMap(field)

def moveLeft():
    os.system('cls')
    cnt = len(snake_position) -1
    field[snake_position[cnt][0]][snake_position[cnt][1]] = "□"
    while cnt>=1:
        snake_position[cnt] = snake_position[cnt-1]
        cnt-=1
    snake_position[0] = [snake_position[0][0],snake_position[0][1]-1]
    for i in snake_position:
        field[i[0]][i[1]] = "■"
    printMap(field)

def moveRight():
    os.system('cls')
    cnt = len(snake_position) -1
    field[snake_position[cnt][0]][snake_position[cnt][1]] = "□"
    while cnt>=1:
        snake_position[cnt] = snake_position[cnt-1]
        cnt-=1
    snake_position[0] = [snake_position[0][0],snake_position[0][1]+1]
    for i in snake_position:
        field[i[0]][i[1]] = "■"
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
        if snake_position[0] in star_list:
            grow()
            star_list.remove(snake_position[0])
        
def controll():
    while True:
        global star_count
        if key=='up':
            while (key=='up'):
                star_count+=1
                moveUp()
                getStar()
                collision()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        elif key=='down':
            while (key=='down'):
                star_count+=1
                moveDown()
                getStar()
                collision()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        elif key=='left':
            while (key=='left'):
                star_count+=1
                moveLeft()
                getStar()
                collision()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        elif key=='right':
            while (key=='right'):
                star_count+=1
                moveRight()
                getStar()
                collision()
                sleep(game_speed)
                if star_count>=star_gen_cycle:
                    generateStar()
                    star_count=0
        #게임초기화
        elif key=='q' or key=='r':
            break
    game()
            
def readKey():
    global key
    key=keyboard.read_key()
    sleep(0.1)
    threading.Thread(target=readKey,daemon=True).start()

def grow():
    global snake_position
    tail_y=snake_position[0][0]
    tail_x=snake_position[0][1]
    
    if(key=='up'):
        tail_y=snake_y+1
        snake_position.append([tail_y,tail_x])
    if(key=='down'):
        tail_y=snake_y-1
        snake_position.append([tail_y,tail_x])
    if(key=='left'):
        tail_y=snake_x+1
        snake_position.append([tail_y,tail_x])
    if(key=='right'):
        tail_y=snake_x-1
        snake_position.append([tail_y,tail_x])

def gameover():
    os.system('cls')
    printMap(field)
    print("***********GAMEOVER***************")
    a = input("다시 하려면 q나 r 입력, 다른 거 입력하면 종료")
    if a in ('q','r'):
        game()

def collision():
    if snake_position[0] in snake_position[1:]:
        gameover()

def game():
    try:
        initGame()
        readKey()
        controll()
    except IndexError as e:
        gameover()
game()


