import os
import time

def clear():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

def main():
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Jollibee Foods Store  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━┫
┃     1. Order           ┃
┃     2. View Order      ┃
┃     3. History         ┃
┃     0. Exit            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━┛""")
    choice = int(input(" Choice: "))
    clear()

    if choice == 1:
        order()
    elif choice == 2:
        vieworder()
    elif choice == 3:
        history()
    elif choice == 0:
        time.sleep(1)
        print("Thank you for visiting Jollibee!")
        quit()

foodmenu = {
    1: ("Chicken Joy", 100),
    2: ("Burger Steak", 85),
    3: ("Spaghetti", 100),
    4: ("Hamburger", 50),
    5: ("Crispy Fries", 50)
}

foods = ""
quantityfoods = 0
total = 0
nameorder = ""

def order():
    global foods, quantityfoods, total, nameorder
    print("""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃      Jollibee Foods    ┃ Price  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  1. Chicken Joy        ┃  ₱100  ┃
┃  2. Burger Steak       ┃  ₱85   ┃
┃  3. Spaghetti          ┃  ₱100  ┃
┃  4. Hamburger          ┃  ₱50   ┃
┃  5. Crispy Fries       ┃  ₱50   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
    food = int(input(" Choice (1-5): "))
    if food in foodmenu:
        foods, price = foodmenu[food]
    quantityfoods = int(input(" Quantity: "))
    total = quantityfoods * price
    nameorder = input(" Name: ")
    time.sleep(2)
    clear()
    orderdone()

def orderdone():
    print("━━━━━━━━━━━━━━━━━━━━━")
    print("Order successfully!")
    print("━━━━━━━━━━━━━━━━━━━━━")
    text = input("Press any key to continue . . . ")
    time.sleep(2)
    clear()
    main()

def vieworder():
    global foods, quantityfoods, total
    if not foods:
        print("Oops no orders yet!")
        input("Press any key to exit . . . ")
        time.sleep(2)
        clear()
        main()
    else:
        print(f"""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  Quantity      Foods        Price  ┃
┃   x{quantityfoods:<7}   {foods:<15}₱{total:<6}┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        print(" 1. Payment")
        print(" 0. Back")
        print("")
        try:
            choice = int(input(" Enter: "))
            if choice == 1:
                clear()
                deposit()
            elif choice == 0:
                clear()
                main()
            else:
                print("Invalid choice! Returning to main menu.")
                time.sleep(2)
                clear()
                main()
        except ValueError:
            print("Invalid input! Returning to main menu.")
            time.sleep(2)
            clear()
            main()

def history():
    global foods, nameorder, total, quantityfoods, change, deposit
    if not foods:
        print("Oops no orders yet!")
        input("Press any key to exit . . . ")
        time.sleep(2)
        clear()
        main()
    else:
        print("   Payment History")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Name: {nameorder}")
        print(f"Cash: ₱{deposit}")
        print(f"Foods: {foods}  x{quantityfoods}")
        print(f"Total price: ₱{total}")
        print("━━━━━━")
        print(f"Change: ₱{change}")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        text = input("Press any key to continue . . . ")

def deposit():
    global nameorder, total, deposit
    print("  Jollibee Deposit")
    print("━━━━━━━━━━━━━━━━━━━━━")
    print(f"Total price: ₱{total}")
    deposit = int(input("Deposit cash: ₱"))
    time.sleep(2)
    print("━━━━━━━━━━━━━━━━━━━━━")
    print("Deposit successfully!")
    print("━━━━━━━━━━━━━━━━━━━━━")
    text = input("Press any key to continue . . . ")
    time.sleep(2)
    clear()
    payment()
        
def payment():
    global deposit, foods, change
    print(f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: {nameorder}
Cash: ₱{deposit}
━━━━━━
Order: {foods} x{quantityfoods}
Total price: ₱{total}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
    text = input("Press any key to Pay your order . . . ")
    time.sleep(2)
    clear()
    if deposit >= total:
        change = deposit - total
        print(f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Payment successfully!

Name: {nameorder}
Cash: ₱{deposit}
Total price: ₱{total}
━━━━━━
Change: ₱{change}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
        text = input("Press any key to continue . . .")
        time.sleep(1)
        clear()
        main()

while True:
    clear()
    main()