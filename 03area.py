def rectangle_area(length, width):
    return length * width
def square_area(side):
    return side ** 2
def circle_area(radius):
    return 3.14 * radius ** 2
def triangle_area(base, height):
    return 0.5 * base * height
user_imp = int(input("Enter shape (rectangle =0, square = 1, circle = 2, triangle = 3): "))
if user_imp == 0:
    shape="Rectangle"
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = rectangle_area(length, width)
elif user_imp == 1:
    shape = "Square"
    side = float(input("Enter side length: "))
    area = square_area(side)
elif user_imp == 2:
    shape = "Circle"
    radius = float(input("Enter radius: "))
    area = circle_area(radius)
elif user_imp == 3:
    shape="Triangle"
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    area = triangle_area(base, height)
else:
    print("Invalid shape entered")
    area = 0
print("The area of the", shape, "is", area)
