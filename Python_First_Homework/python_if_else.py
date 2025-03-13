get_number = int(input(""))

if (get_number%2 != 0):
    print("Weird")

elif ((get_number%2 == 0) and (2<=get_number<=5)):
    print("Not Weird")
    
elif ((get_number%2 == 0) and (6<=get_number<=20)):
    print("Weird")

elif ((get_number%2 == 0) and (get_number>20)):
    print("Not Weird")
    
