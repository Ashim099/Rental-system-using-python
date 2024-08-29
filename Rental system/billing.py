import datetime
import message
import billing

def read_file():
    data = []
    with open ("equip.txt","r") as file:
        date = file.readline()
    return data

def read_updated_file(list_d):
    file = open("equip.txt","w")
    for i in list_d.values():
        file.write(i[0]+","+i[1]+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5]))
        file.write("\n")
    file.close()

def billing_address( maindata , Gross_total ,delevery_charge, grandTotal):
    current = datetime.datetime.now()
    dateTimeForInv = current.strftime("%H-%M-%S")
    dateTimeForBill = current.strftime("%Y-%m-%d-%H-%M-%S")

    fileName = "THis is name" + dateTimeForInv + ".txt"
    file = open(fileName,"w")
    file.write("*******************************************************************************************************************************************************************" + "\n")
    file.write("\t\t\t\t Invoice" + "\n")
    file.write("*******************************************************************************************************************************************************************" + "\n")
    file.write("\n")
    file.write("equipment Details are displayed below : ")
    file.write("\n")
    file.write("\n")
    file.write("Date and Time of the purchase : " + dateTimeForBill + "\n")
    file.write("\n")
    file.write("Details of the purchase : ")
    file.write("\n")
    file.write("===============================================================================================================" + "\n")
    file.write("equipment name \t\t equipment brand \t\t Quantity \t\t Unit Price \t\t   Total" + "\n")
    file.write("================================================================================================================" + "\n")
    file.write("\n")
    for item in maindata:
        file.write(str(item[0]) +  str(item[1]) + "\t     " +str(item[2]) + "\t\t         " +str(item[3]) + "\t\t    " + "$"+str(item[4]) + "\n")
    file.write("\n")
    file.write("===============================================================================================================" + "\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t" + "Gross Total is   : " + str(Gross_total) + "\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t" + "Shipping cost is : " + str(delevery_charge) + "\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t" + "Grand Total  is  : " + str(grandTotal) + "\n")
    file.write("\n")
    file.close()

    #printing the invoice 
    print("*****************************************************************************************************************************************************************************")
    print("\t\t\t\t Invoice" + "\n")
    print("*****************************************************************************************************************************************************************************")
    print("\n")
    print("equipment Details are displayed below : ")
    print("\n")
    print("Date and Time of the purchase : " + dateTimeForBill + "\n")
    print("Details of the purchase : ")
    print("\n")
    print("===============================================================================================================" + "\n")
    print("equipment name \t\t       equipment brand \t\t       Quantity \t\t Unit Price \t\t Total" + "\n")
    print("===============================================================================================================" + "\n")
    print("\n")
    for item in maindata:
        print(str(item[0]) + "\t\t" +str(item[1]) + "\t\t"+str(item[2]) + "\t\t  " +str(item[3]) + "\t\t   " + "$"+str(item[4]) + "\n")
    print("\n")
    print("==============================================================================================================" + "\n")
    print("\n")
    print(" \t\t\t\t\t\t\t\t\t\t\t    Gross Total is   : " + str(Gross_total) + "\n")
    print(" \t\t\t\t\t\t\t\t\t\t\t    Shipping cost is   : " + str(delevery_charge) + "\n")
    print(" \t\t\t\t\t\t\t\t\t\t\t    Grand Total  is : " + str(grandTotal) + "\n")
    print("\n")


def generate_invoice(maindata, customer_name, customer_phone, delivery_charge):
    total = 0  # Initialize the total to zero
    current = datetime.datetime.now()
    dateTimeForInv = current.strftime("%H-%M-%S")
    dateTimeForBill = current.strftime("%Y-%m-%d-%H-%M-%S")

    fileName = f"Invoice_{customer_name}_{dateTimeForInv}.txt"
    file = open(fileName, "w")

    file.write("****************************************************************************************************" + "\n")
    file.write(f"\t\t\t\t Date: {dateTimeForBill}\n")
    file.write(f"\t\t\t\t Invoice for {customer_name}\n")
    file.write(f"\t\t\t\t Phone Number: {customer_phone}\n")
    file.write("****************************************************************************************************" + "\n")
    file.write("\n")
    file.write("Details of the purchase:\n")
    file.write("====================================================================================================\n")
    file.write("{:<45}{:<10}{:<15}{:<10}\n".format("Equipment name", "Quantity", "Unit Price", "Total"))
    file.write("====================================================================================================\n")

    # Iterate over items in maindata and write item details
    for item in maindata.values():
        product_name = item[0]
        quantity = item[3]
        unit_price = item[2]
        total_price = int(quantity.replace('$', '').replace(',', '')) * int(unit_price.replace('$', '').replace(',', ''))

        # Write each item's details
        file.write("{:<45}{:<10}{:<15}${:.2f}\n".format(product_name, quantity, unit_price, total_price))

        # Add the total price of this item to the overall total
        total += total_price

    # Calculate grand total by adding the delivery charge
    grand_total = total + delivery_charge

    file.write("====================================================================================================\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tGross Total: ${:.2f}\n".format(total))
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tDelivery Charge: ${:.2f}\n".format(delivery_charge))
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tGrand Total: ${:.2f}\n".format(grand_total))
    file.write("\n")
    file.close()

    print("Invoice generated successfully.")


def generate_return_invoice(maindata, customer_name, customer_phone, rental_days):
    total = sum(int(item[2].replace('$', '').replace(',', '')) * int(item[3]) for item in maindata.values())
    additional_charge = 0

    if rental_days > 5:
        additional_charge = 50 * (rental_days - 5)

    grand_total = total + additional_charge

    current = datetime.datetime.now()
    dateTimeForInv = current.strftime("%H-%M-%S")
    dateTimeForBill = current.strftime("%Y-%m-%d-%H-%M-%S")

    fileName = f"Invoice_{customer_name}_{dateTimeForInv}.txt"
    file = open(fileName, "w")

    file.write("****************************************************************************************************" + "\n")
    file.write(f"\t\t\t\t Date: {dateTimeForBill}\n")
    file.write(f"\t\t\t\t Invoice for {customer_name}\n")
    file.write(f"\t\t\t\t Phone Number: {customer_phone}\n")  # Include the customer's phone number
    file.write("****************************************************************************************************" + "\n")
    file.write("\n")
    file.write("Details of the purchase:\n")
    file.write("====================================================================================================\n")
    file.write("{:<5}{:<45}{:<22}{:<12}{:<10}\n".format("Product name", "Brand", "Quantity", "Unit Price", "Total"))
    file.write("====================================================================================================\n")

    for item in maindata.values():
        product_name = item[0]
        brand = item[1]
        quantity = item[3]
        unit_price = item[2]
        total_price = "${:.2f}".format(int(item[2].replace('$', '').replace(',', '')) * int(item[3]))
        
        file.write("{:<5}{:<45}{:<22}{:<12}{:<10}\n".format(product_name, brand, quantity, unit_price, total_price))

    file.write("====================================================================================================\n")
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tGross Total: ${:.2f}\n".format(total))
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tAdditional Charge (if applicable): ${:.2f}\n".format(additional_charge))
    file.write("\n")
    file.write("\t\t\t\t\t\t\t\t\t\tGrand Total: ${:.2f}\n".format(grand_total))
    file.write("\n")
    file.close()

    print("Invoice generated successfully.")
    message.greading()




def write_file(maindata):
    with open("equip.txt","w") as file:
        for value in maindata.values():
            write_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n"
            file.write(write_data)

def date_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def date():
    return datetime.datetime.now().strftime("%Y-%m_%d")

