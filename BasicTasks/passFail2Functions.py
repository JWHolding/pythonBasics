import os

def fail(failRate):
    if failRate == 1:
        os.system("cls")
        print("Retake the exam")
    elif failRate ==2 :
        os.system("cls")
        print("Retake the course")
    else:
        os.system("cls")
        print("Go home my friend")

def passed(tot,p):
    os.system("cls")
    print("Passed!")
    print("Total:", tot)
    print("Percentage:%0.2f%%" % p)
