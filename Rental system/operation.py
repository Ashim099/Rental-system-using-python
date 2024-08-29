import datetime

def read_file():
    data = []
    with open("equip.txt","r") as file:
        data = file.readlines()
    return data

def date_time():
    return datetime.datetime.now().strftime("%y-%m-%d %H:%M")

def date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def display_items(container, main_data):
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("|{:<5}|{:<45}|{:22}|{:12}|{:<10}|".format("id","Equipments Name", "Brand", "Prise", "Quantity"))
    print("------------------------------------------------------------------------------------------------------------------------------------------")
    for key, Value in main_data.items():
        print("|{:<5}|{:<45}|{:22}|{:12}|{:<10}|".format(key, Value[0], Value[1], Value[2], Value[3]))
    print("------------------------------------------------------------------------------------------------------------------------------------------")

def write_file(maindata):
    with open("equip.txt", "w") as file:
        for value in maindata.values():
            write_data = str(value[0])+ "," + str(value[1])+ "," + str(value[2])+ "," + str(value[3])
            file.write(write_data)

def dictionary(container):
    data = {}
    for index in range(len(container)):
        data[index + 1] = container[index].replace("\n", "").split(",")
    return data    