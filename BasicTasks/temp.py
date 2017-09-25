#!/usr/bin/python

temp = input("Enter the temperature: ")
t=int(temp)

if t > 40:
    print("It's too warm!")
if t < 40:
    print("It's too cold!")
if t == 40:
    print("Just right!")
