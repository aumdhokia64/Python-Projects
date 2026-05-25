delivery_time = int(input("Enter Your Delivery Time"))
if delivery_time <= 30:
    print("On Time")
elif delivery_time >= 30:
    print("Delayed!")
else:
    print("Error")
