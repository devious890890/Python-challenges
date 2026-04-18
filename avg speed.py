Cyclist1 = int(input("Enter value1 here:"))
Cyclist2 = int(input("Enter value2 here:"))
Cyclist3 = int(input("Enter value3 here:"))


cyclistspeed_sum = Cyclist1 + Cyclist2 + Cyclist3

avg_speed = cyclistspeed_sum/3
print("avarage speed is =", avg_speed)

if avg_speed >= Cyclist1:
    print("Cyclist1 is the fastest")
elif avg_speed >= Cyclist2 <Cyclist1:
    print("Cyclist2 is slower than Cyclist 1")
else:
    print("Cyclist3 the slowest")