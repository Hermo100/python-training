speed_limit = 70
demerit_points = 0


speed = float(input("Enter the speed of the car: "))

if speed <= speed_limit:
    print("Ok")
elif(speed>speed_limit):
    demerit_points=1
else:
    demerit_points = round((speed - speed_limit))*5
   
if demerit_points > 12:
        print("License suspended.")
else:
    print(f"Points: {demerit_points}")
    print(demerit_points)
