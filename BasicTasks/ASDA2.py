product1 = "7up"
product2 = "Coke"

price1=1.75
price2=1.21

qty1=10
qty2=5

total = (qty1*price1)+(qty2*price2)

discount = input("Is there a discount Y/N:")
if (discount.upper() == "Y"):
    discountRate = input("what is the percentage? xx%:")
    total *= 1-(int(discountRate)/100)
tax = total*1.2
totalCost = tax+total
lineSpace="_____________________"
print(lineSpace)
print(product1, "  x  ", qty1, " @ ", price1)
print(product2, " x   ", qty2, " @ ", price2)
print(lineSpace)
print("Total: %0.2f" % total)
print("Tax: %0.2f" % tax)
if (discount.upper() == "Y"):
    print("Discount:", discountRate + "%")
print(lineSpace)
print("Total to Pay: %0.2f" % totalCost)
print(lineSpace)
