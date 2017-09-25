import os

def logo():
    print("           pepsipepsipep_")
    print("       sipepsipepsipepsipeps")
    print("    ipepsipepsipepsipepsipepsip")
    print("  epsipepsipepsipepsipepsipepsipe")
    print(" ps       epsipepsipepsipepsipepsi")
    print("               pepsipepsipepsipepsi")
    print("    IPEPSIPE           sipepsip")
    print("PEPSIPEPSIPEPSIPEPSI")
    print(" PEPSIPEPSIPEPSIPEPSIPEPS       EP")
    print("  PEPSIPEPSIPEPSIPEPSIPEPSIPEPSIP")
    print("    EPSIPEPSIPEPSIPEPSIPEPSIPEP")
    print("       SIPEPSIPEPSIPEPSIPEPS")
    print("          ~IPEPSIPEPSIPE~")

#get all inputs

product1 = input("Product1 Name:")
product2 = input("Product2 Name:")
price1 = input("%s Price:" % product1)
price2 = input("%s Price:" % product2)
qty1 = input ("%s Quantity:" % product1)
qty2 = input ("%s Quantity:" % product2)

#calculate the total price
total = (int(qty1)*float(price1))+(int(qty2)*float(price2))
tax = total*0.2
discount = input("Is there a discount Y/N:")
#if there is a discount we take this off total
if (discount.upper() == "Y"):
    discountRate = input("what is the percentage? xx%:")
    total *= 1-(int(discountRate)/100)
totalCost = tax+total
lineSpace="__________________________________"
os.system('cls')
logo()
print(lineSpace)
print(product1, " x ", qty1, " @ £" + price1)
print(product2, " x ", qty2, " @ £" + price2)
print(lineSpace)
print("Total: %0.2f" % total)
print("Tax: %0.2f" % tax)
if (discount.upper() == "Y"):
    print("Discount:", discountRate + "%")
print(lineSpace)
print("Total to Pay: %0.2f" % totalCost)
print(lineSpace)
