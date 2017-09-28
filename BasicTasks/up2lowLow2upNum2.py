"""Example stuff."""

string = input("Enter a String: ")
A = int(0)
string2 = ""
while A < len(string):
    if ord(string[A]) >= 65 and ord(string[A]) <= 90:
        string2 = string2 + chr(ord(string[A]) + 32)
    elif ord(string[A]) >= 97 and ord(string[A]) <= 122:
        string2 = string2 + chr(ord(string[A])-32)
    elif ord(string[A]) >= 48 and ord(string[A]) <= 57:
        string2 = string2 + str(int(string[A])*2)
    else:
        string2 = string2 + string[A]
    A = A+1
print(string, "became", string2)
