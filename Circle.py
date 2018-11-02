import math

def circle_data(r):
    areaCircle = (math.pi * r**2)
    circumference = ((2 * math.pi) * r)
    tup1 = (areaCircle, circumference)
    return tup1



while True:
    r = int(input("Enter a radius length: "))
    if r <= 0:
        print("Enter a positive integer: ")
    else:
        solution = circle_data(r)
        print(f"Area of a your Circle: {solution[0]:.3f} and Circumference: {solution[1]:.3f}")
        break