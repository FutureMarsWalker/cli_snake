import os
import random
import time
import keyboard

SNAKE_HEAD = "0"
SNAKE_BODY = "o"
BLANK = "x"
gameBoard = []
cols = 0
dim = (0, 0)
currPos = 0
pastPos = 0
counter = 0


def makeGameBoard(arr, dimensions):
    global dim
    global cols
    dim = dimensions
    rows = dim[0]
    cols = dim[1]
    for r in range(rows):
        for c in range(cols):
            arr.append("x")
    return arr


def printGameBoard(arr):
    count = 0
    for i in arr:
        count += 1
        if count % cols != 0:
            print(i, end=" ")
        else:
            print(i, end="\n")
    print("_" * 20)


def printPlayer():
    global currPos
    currPos = random.randrange(0, (dim[1] * dim[0]) + 1, 1)
    gameBoard[currPos] = SNAKE_HEAD


def movePlayer():
    global currPos
    global pastPos
    global counter

    while True:
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

        except:
            print("Doesn't work")
            break


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


if __name__ == "__main__":
    makeGameBoard(gameBoard, (10, 10))
    printPlayer()
    printGameBoard(gameBoard)
    movePlayer()
