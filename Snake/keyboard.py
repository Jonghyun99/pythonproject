from time import sleep
import keyboard
import threading

# field = [["□" for col in range(3)] for row in range(3)]
# field[1][1]="a"
# print(field)

# if field[1][1] in ["★", "■"]:
#     print("■혹은 ★입니다.")
# else:
#     print("아닙니다.")

# pointList=[1,2]
# print(pointList)

# pointList.append([5,5])
# print(pointList)

# key = 'up'

def test1():
    print(key)
    # while True:
    #     if key==('up'):
    #         print('up')
    #         break
    #     elif key==('down'):
    #         print('down')
    #         break

def test2():

    threading.Thread(target=test2,daemon=True).start
    global key
    while True:
        if keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            if keyboard.is_pressed('up'):
                key = 'up'
                print("키입력됨")
                sleep(0.1)
                test1()
            
            elif keyboard.is_pressed('down'):
                key = 'down'
                print("키입력됨")
                sleep(0.1)
                test1()



test2()