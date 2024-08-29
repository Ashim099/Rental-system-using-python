import rentequip
import message
import returnequip
import billing

message.firstscreen()
run = True

while run:
    message.sellect()
    
    correct_option = False
    while not correct_option:
        try:
            option = int(input("chhose an option:"))
            correct_option = True
        except ValueError:
            message.notvalid()
            message.firstscreen()

    if option == 1:
        rentequip.rent()

    elif option == 2:
        returnequip.returning()

    elif option == 3:
        message.greading()
        run = False

    else:
        message.notvalid()
        


