
import operation
import message
import billing

def valid_id_return(maindata):
    valid_id = False
    while valid_id == False:
        try:
            id = int(input("Enter equipment id you wanna return:"))
            if 1 <= id <= len(maindata):
                valid_id = True
                return id
            else:
                message.notvalid()
        except ValueError:
            message.notvalid()

def valid_quantity_return(maindata, id):
    valid_quantity = False
    while valid_quantity == False:
        try:
            quantity = int(input("Enter a number of equipment you wanna return"))
            if quantity > 0:
                valid_quantity = True
                return quantity
            else:
                message.notvalid()
        except ValueError:
            message.notvalid()

def generate_single_item_invoice(item, customer_name, customer_phone, rental_days):
    single_item_data = {
        item[0]: [item[0], item[1], item[2], '1']  # Create a temporary dictionary for the selected item
    }
    billing.generate_return_invoice(single_item_data, customer_name, customer_phone, rental_days)


def returning():
    print("\n Conferm returning equipment. \n")

    file_content = operation.read_file()
    maindata = operation.dictionary(file_content)

    add_to_cart = []
    thirdloop = True
    while thirdloop == True:
        operation.display_items(file_content, maindata)
        id = valid_id_return(maindata)
        fn = int(valid_quantity_return(maindata, id))
        maindata[id][3] = str(int(maindata[id][3]) + fn)
        add_to_cart.append([id, fn])

        operation.write_file(maindata)
        operation.display_items(file_content, maindata)

        again = True
        while again == True:
            customer_input = input("Want to return more equipments?(yes/no)")
            if customer_input.lower() == "no":
                thirdloop = False
                again = False
                print('Bill please return')
                selected_item = maindata[id]
                customer_name = input("Enter the customer's name: ")
                customer_phone = input("Enter the customer's phone number: ")
                rental_days = int(input("Enter the number of rental days: "))
                generate_single_item_invoice(selected_item, customer_name, customer_phone, rental_days)

            elif customer_input.lower() == "yes":
                thirdloop = True
                again = False

            else:
                message.notvalid()
                again = True
    print()
    

    if __name__ == "__main__":
        returning()