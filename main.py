import os
import random
import time
import keyboard

BLANK = "_"
SNAKE_HEAD = "0"
SNAKE_BODY = "o"
FOOD = "A"
gameBoard = []
cols = 0
dim = (0, 0)
currPos = 0
foodCurrPos = 0
pastPos = 0
counter = 0
score = 0


'''def makeBody():
    global currPos
    global pastPos
    global dim

    if foodEaten():
        if currPos - pastPos == 1:
            right_arrow()
        elif currPos - pastPos == -1:
            left_arrow()
        elif currPos - pastPos == dim[1]:
            down_arrow()
        elif currPos - pastPos == -dim[1]:
            up_arrow()

    else:
        pass'''


def foo():
    pass


def foodSpawn():
    global dim
    global foodCurrPos

    foodNotEaten = True
    if foodNotEaten:
        while True:
            foodCurrPos = random.randint(0, dim[0] * dim[1])
            if foodCurrPos != currPos:
                break
        printFood(gameBoard, foodCurrPos)
    else:
        pass


def printFood(arr, randInt):
    arr[randInt] = FOOD


def makeGameBoard(arr, dimensions):
    global dim
    global cols
    dim = dimensions
    rows = dim[0]
    cols = dim[1]
    for r in range(rows):
        for c in range(cols):
            arr.append(BLANK)
    return arr


def printGameBoard(arr):
    global score
    count = 0
    print(f"\n###### Score: {score} ######\n")
    for i in arr:
        count += 1
        if count % cols != 0:
            print(i, end=" ")
        else:
            print(i, end="\n")
    print("_" * 20)


def foodEaten():
    global foodCurrPos

    if currPos == foodCurrPos:
        return True
    else:
        return False


def printPlayer(arr):
    global currPos
    currPos = random.randrange(0, (dim[1] * dim[0]) + 1, 1)
    arr[currPos] = SNAKE_HEAD


def movePlayer():
    global currPos
    global pastPos
    global counter

    try:
        if keyboard.is_pressed("left"):
            if counter < 1:
                os.system("cls")
                left_arrow()
                counter += 1
            else:
                time.sleep(0.3)
                os.system("cls")
                left_arrow()
        elif keyboard.is_pressed("right"):
            if counter < 1:
                os.system("cls")
                right_arrow()
                counter += 1
            else:
                time.sleep(0.3)
                os.system("cls")
                right_arrow()
        elif keyboard.is_pressed("up"):
            if counter < 1:
                os.system("cls")
                up_arrow()
                counter += 1
            else:
                time.sleep(0.3)
                os.system("cls")
                up_arrow()
        elif keyboard.is_pressed("down"):
            if counter < 1:
                os.system("cls")
                down_arrow()
                counter += 1
            else:
                time.sleep(0.3)
                os.system("cls")
                down_arrow()
        counter += 1

    except KeyboardInterrupt:
        pass


def left_arrow():
    global currPos
    global pastPos

    pastPos = currPos
    gameBoard[currPos - 1] = SNAKE_HEAD
    currPos = currPos - 1
    gameBoard[pastPos] = BLANK
    printGameBoard(gameBoard)


def right_arrow():
    global currPos
    global pastPos

    pastPos = currPos
    gameBoard[currPos + 1] = SNAKE_HEAD
    currPos = currPos + 1
    gameBoard[pastPos] = BLANK
    printGameBoard(gameBoard)


def up_arrow():
    global currPos
    global pastPos

    pastPos = currPos
    gameBoard[currPos - dim[1]] = SNAKE_HEAD
    currPos = currPos - dim[1]
    gameBoard[pastPos] = BLANK
    printGameBoard(gameBoard)


def down_arrow():
    global currPos
    global pastPos

    pastPos = currPos
    gameBoard[currPos + dim[1]] = SNAKE_HEAD
    currPos = currPos + dim[1]
    gameBoard[pastPos] = BLANK
    printGameBoard(gameBoard)


'''def const_vel():
    while True:
        if keyboard.KEY_DOWN == "down":
            randNum = random.randint(1, 4)
            if randNum == 1:
                time.sleep(1)
                up_arrow()
            elif randNum == 2:
                time.sleep(1)
                down_arrow()
            elif randNum == 3:
                time.sleep(1)
                left_arrow()
            elif randNum == 4:
                time.sleep(1)
                right_arrow()
        else:
            break'''


if __name__ == "__main__":
    makeGameBoard(gameBoard, (10, 10))
    printPlayer(gameBoard)
    printGameBoard(gameBoard)
    flag = False

    while True:
        if keyboard.is_pressed("q"):
            break
        else:
            while not flag:
                foodSpawn()
                flag = True
            if foodEaten():
                foodSpawn()
                score += 1
            movePlayer()
