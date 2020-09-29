"""Project name :  Advanced Loop Training
    File name : main.py
    Programmer : Colin B. Chin Choy
"""

col = ""
row = ""


def drawBoard():
    x = input("Please enter the quantity of columns:- ")
    y = input("Please enter the quantity of rows:- ")

    col = int(x)
    row = int(y)
    ro1 = (row*2)-1

    for i in range(0,ro1):
        if (int(i) % 2 == 0):
            print((" ")+(" "+" "+" "+"|")*(col-1))
        else:
            print(" "+("-"*((col*3)+(col-1))))

drawBoard()
print("True")
