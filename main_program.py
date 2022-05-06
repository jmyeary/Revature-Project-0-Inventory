import mymenu
from pymongo import MongoClient

#selecting the proper mongoDB
cluster = MongoClient("mongodb://localhost:27017/")
db = cluster["ProjectZero"]

#collection 1 is on-hand inventory
collection1 = db["inventory_onhand"]

#collection2 is master collection
collection2 = db["master"]

#collection 3 is inventory on-order
collection3 = db["inventory_onorder"]

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
    elif menu_option == 3:
         mymenu.onorder_menu()     #call our menu
         menu_option3 = int(input("Enter your option: "))
         while menu_option3 != 0:
             if menu_option3 == 1:
                 # Run through the entire collection, extract each sku number and product name from the document, print them in an f-string for readability
                 for x in collection3.find():
                     print(f"SKU: {x['sku']} | Product Name: {x['product_name']} | Quantity: {x['quantity_onorder']}")
                 exit()
             elif menu_option3 == 2:
                 temp_sku = int(input('Enter a SKU number: '))
                 temp_qty = int(input('Enter quantity on order: '))
                 collection3.update_one({'sku': temp_sku}, {"$set": {'quantity_onorder': temp_qty}})
                 print(f"You have successfully ordered {temp_qty} units of SKU # {temp_sku}")
                 exit()

    else:
        print("Invalid option.\n")
    mymenu.main_menu()
    menu_option = int(input('Enter your option: '))