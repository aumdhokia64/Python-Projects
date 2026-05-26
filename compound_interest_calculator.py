principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter Your Principle Amount: "))
    if principle <= 0:
        print("Principle Can't Be Less Than Or Equal To Zero")

while rate <= 0:
    rate = float(input("Enter Your Interest Rate: "))
    if rate <= 0:
        print("Interest Rate Can't Be Less Than Or Equal To Zero")

while time <= 0:
    time = int(input("Enter Your Time In Years: "))
    if time <= 0:
        print("Time Can't Be Less Than Or Equal To Zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total}")