from pizzapy import Customer, StoreLocator, ConsoleInput, Order

def searchMenu(menu):
    print("You are now searching the menu...")
    
    item = input('Type an item to look for:').strip().lower()

    if len(item) > 1:
        item = item[0].upper() + item[1:]
        print(f"Results for: {item}")
        menu.search(Name=item)
        print()
    else:
        print("No results")


def addToOrder(order):
    print("Please type the codes of the itmes you'd like to order")
    print("Press ENTER to stop odering")
    while True:
        item = input('Code: ').upper()
        try:
            order.add_item(item)
        except:
            if item == '':
                break
            print("Invalid Code...")
    
            
customer = ConsoleInput.get_new_customer()

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print("\nClosest Store:")
print(my_local_dominos)

ans = input("Would you like to order from this store? (Y/N)")
if ans.lower() not in ['yes','y']:
    print("goodbye")
    print()


print("\nMENU\n")

menu = my_local_dominos.get_menu()
order = Order.begin_customer_order(customer, my_local_dominos, "ca")    

while True:
    searchMenu(menu)
    addToOrder(order)
    answer = input("Would you like to add more items (y/n) ?")
    if answer.lower() not in ['yes','y']:
        break

total = 0
print("\nyour order is as follows")
for item in order.data["Products"]:
    price = item['Price']
    print(item['Name']+ " $ "+ price)
    total += float(price)

print('Your order total is: $' + str(total)+ " + TAX")

payment = input('\nWill you be paying CASH or CREDIT CARD? (CASH, CREDIT CARD)')
if payment.lower() in ['card','credit card']:
    card = ConsoleInput.get_credit_card()
else:
    card = False


ans = input("Would you like to place this store? (Y/N)")
if ans.lower() in ['yes','y']:
    order.place(card)
    my_local_dominos.place_order(order, card)
    print('Order Placed!')
else:
    print('Goodbye!')








