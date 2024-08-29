import operation
import message
import billing


def valid_id_rent(maindata):
    valid_data = False
    while not valid_data:
        try:
            id = int(input("Enter equipment id, you want to rent"))
            if 1 <= id <= len(maindata):
                if int(maindata[id][3])>0:
                    valid_data = True
                    return id
                else:
                    message.not_in_stock()
            else:
                message.notvalid()
        except ValueError:
            message.notvalid()

def valid_quantity_rent(maindata, id):
    valid_quantity = False
    while not valid_quantity:
        try:
            quantity = int(input("What quantity do you want to rent?"))
            if quantity > 0 and quantity <= int(maindata[id][3]):
                valid_quantity = True
                return quantity
            else:
                message.variety()
        except ValueError:
            message.notvalid

def generate_single_item_invoice(item, customer_name, customer_phone,delevery_charge):
    single_item_data = {
        item[0]: [item[0], item[1], item[2], '1']  # Create a temporary dictionary for the selected item
    }
    billing.generate_invoice(single_item_data, customer_name, customer_phone,delevery_charge)


def rent():
    print("\n Rent equipment. \n")

    file_content = operation.read_file()
    maindata =operation.dictionary(file_content)

    add_to_cart = []
    operation.display_items(file_content, maindata)
    secondloop = True
    while secondloop: 
        id = valid_id_rent(maindata)
        message.availability()
        fn = int(valid_quantity_rent(maindata, id))
        maindata[id][3] = str(int(maindata[id][3]) - fn)
        add_to_cart.append([id, fn])

        operation.write_file(maindata)
        operation.display_items(file_content, maindata)

        next_action = True
        while next_action == True:
            user_input = input("Wanna rent more?(yes/no)")

            if user_input.lower() == "yes":
                secondloop = True
                next_action = False

            elif user_input.lower() == "no":
                selected_item = maindata[id]
                customer_name = input("Enter the customer's name: ")
                customer_phone = input("Enter the customer's phone number: ")
                generate_single_item_invoice(selected_item, customer_name, customer_phone,100)
                secondloop:False
                next_action = False
            else:
                message.notvalid()
                next_action = True
    print()