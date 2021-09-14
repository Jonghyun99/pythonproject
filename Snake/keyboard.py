from time import sleep
import keyboard
import threading

# test=[[5,5],[5,5-1],[5,5-2]]
# for i in test:
#     print(i[0])
    


field = [["□" for col in range(11)] for row in range(11)]

test=[[1,1],[2,2],[3,3]]

for i in test:
    print(i[0])
    field[i[0]][i[1]] = "■"

for i in field:
    for j in i:
        print(j, end=" ")
    print()



    # for i in :
    #     field[i[0]][i[1]] = "■"
    # printMap(field)