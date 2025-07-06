# def area(l,w):
#     area = l * w
#     print(area)

# area(10,30)

# def check_grade(score):
#     if score > 50:
#         return "pass"
#     else:
#         return "fail"
    
# number = int(input("Enter scores"))

# grade = check_grade(number)
# print(grade)

# def rectangle_area(length,width):
#     area = length * width
#     return area

# length = int(input("Enter length"))
# width = int(input("Enter width"))

# rectangle = rectangle_area(length,width)
# print(rectangle) 

def circle_area(radius,pi=3.142):
    area = pi * radius**2
    return area

radius = float(input("Enter radius:"))

calculation = circle_area(radius)
print(calculation, "squared-metres")
