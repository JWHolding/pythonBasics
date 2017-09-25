#!/usr/bin/python

fuelPerLap = 2.25

laps = input("How Many Laps in Race: ")
fuelRequirement = fuelPerLap*float(laps)
fuelRequirement *= 1.5
time = 80.45 + (0.35*((fuelRequirement - 5)/10))

print("You will need:", fuelRequirement, "kg of fuel")
print("Your first lap time will be:", time, "seconds")
