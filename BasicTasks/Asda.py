product1 = "7up"
product2 = "Coke"

price1=1.75
price2=1.20

qty1=10
qty2=5

total = (qty1*price1)+(qty2*price2)
tax = total*1.2
totalCost = tax+total
lineSpace="_____________________"
print(lineSpace)
print(product1, "  x  ", qty1)
print(product2, " x   ", qty2)
print(lineSpace)
print("Total: %0.2f" % total)
print("Tax: %0.2f" % tax)
print(lineSpace)
print("Total to Pay: %0.2f" % totalCost)
print(lineSpace)
