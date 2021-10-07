# Programmers: Katie, Chris, Eleni
# CS151, Dr. Rajeev
# October 7, 2021
# Lab 4

plan = input("Enter your plan")
plan = plan.strip().lower()
data = input("Enter the amount of data(GB) used")
data = float(data)
import math

if plan == "green":
    if data > 2.0:
        price = 49.99 + 14.99 * (data - 2.0)
        coupon = input("Do you have a coupon?")
        coupon = coupon.strip().lower()
        if coupon == "yes" and price >= 75.0:
            price -= 20.0
    else:
        price = 49.99
elif plan == "orange":
    if data > 4.0:
        price = 69.99 + 9.99 * (data - 4.0)
    else:
        price = 69.99
elif plan == "purple":
    price = 99.99
else:
    print("Invalid entry")

print("Your bill is $ %.2f" %price, "for", data, "GBs", sep = " ")
