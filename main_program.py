import mymenu
from pymongo import MongoClient
from pprint import pprint

#selecting the proper mongoDB
cluster = MongoClient("mongodb://localhost:27017/")
db = cluster["ProjectZero"]

#collection 1 is on-hand inventory
collection1 = db["inventory_onhand"]

#collection2 is master collection
collection2 = db["master"]

mymenu.main_menu()
menu_option = int(input('Enter your option: '))
while menu_option != 0:
    if menu_option == 1:      #SKU check option
        sku_input = int(input('Enter a SKU number: '))
        sku = collection1.find_one({'sku': sku_input})
        print("\nProduct name: " + sku['product_name'])
        print("Quantity on hand: " + str(sku['quantity']))
        break
    elif menu_option == 2:          #Master inventory option
        mymenu.master_menu()     #call our menu
        menu_option2 = int(input("Enter your option: "))
        while menu_option2 != 0:
            if menu_option2 == 1:
                #Run through the entire collection, extract each sku number and product name from the document, print them in an f-string for readability
                for x in collection2.find():
                    print(f"SKU: {x['sku']} | Product Name: {x['product_name']}")
                exit()
            elif menu_option2 == 2:
                #game plan is to create two local variables temp_sku and temp_name, create a new document in the collection with those values as key:val pair
                #In my collection I have made SKU field a unique index to prevent duplicate entries. Program will produce an error in the event of duplications
                temp_sku = int(input('Enter a SKU number: '))
                temp_name = str(input('Enter a product name: '))
                collection2.insert_one({'sku': temp_sku, 'product_name': temp_name})
                exit()
            elif menu_option2 == 3:
                #game plan is to prompt the user for a SKU number, and then delete the document associated with that SKU
                print('WARNING - This will permanently erase the chosen document!')
                temp_sku = int(input('Enter a SKU number : '))
                collection2.delete_one({'sku': temp_sku})
                exit()
 #   elif menu_option == 3:
 #       mymenu.master_menu()     #call our menu
 #       menu_option3 = int(input("Enter your option: "))
 #       while menu_option3 != 0:

    else:
        print("Invalid option.\n")
    mymenu.main_menu()
    menu_option = int(input('Enter your option: '))

#idea - a fourth option that allows the user to display a list of all items in on-hand inventory, then prompts the user
#to see if they'd like to restock. If yes, then place an order for 1000 units and update on-order inventory to reflect that