# MENU IN CAFE
menu = {
    'PIZZA':120,
    'PASTA':50,
    'BURGER':60,
    'SALAD':30,
    'COFFEE':80,
}

#GREETING TO CUSTOMER
print("Welcome To AYUSH Restaurant")
print("PIZZA: Rs120\nPASTA: Rs50\nBURGER: Rs60\nSALAD: Rs30\nCOFFEE: Rs80\n")

#INITIALLY THE ORDER IS 0
order_total = 0

# TAKING ORDER ONE 
item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"ordered item {item_1} is not available yet..we are sorry!!!")
 
# ASKING FOR ADDITIONAL ITEM   
another_order = input("Do you want to add another item??? (YES/NO): ")
if another_order == "YES":
    item_2 = input("Enter the name of second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!!!")

print(f"The total amount of items to pay is {order_total}")

# WRITE YOUR ORDERS IN CAPITAL LETTERS


