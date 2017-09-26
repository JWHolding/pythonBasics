
def eval(passRate):
    if passRate == 0:
        total=phy+che+mat
        per=float(total*100/300)
        print("Total:", total)
        print("Percentage:%0.2f%%" % per)
    elif passRate == 1:
        print("Retake the exam")
    elif passRate ==2 :
        print("Retake the course")
    else:
        print("Go home my friend")

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
eval(failed)
