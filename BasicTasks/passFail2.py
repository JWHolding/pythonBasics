import os

def fail(failRate):
    if failRate == 1:
        print("Retake the exam")
    elif failRate ==2 :
        print("Retake the course")
    else:
        print("Go home my friend")

def passed(tot,p):
    os.system("cls")
    print("Passed!")
    print("Total:", tot)
    print("Percentage:%0.2f%%" % p)

failed=0
phy = int(input("Enter your Physics Mark:"))
che = int(input("Enter your Chemistry Mark:"))
mat = int(input("Enter your Maths Mark:"))

if phy < 60:
    failed += 1
if che < 60:
    failed += 1
if mat < 60:
    failed += 1
if failed == 0:
    total=phy+che+mat
    per=float(total*100/300)
    passed(total,per)
else:
    fail(failed)
