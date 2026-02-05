# global varariable and local variable

length = 5  # global


def calculate_square_area1():
    area = length * length  # local
    print("面積是", area)


calculate_square_area1()

print("-" * 30)

length = 10  # global


def calculate_square_area2():
    area = length * length  # local
    print("面積是", area)


length = 10  # global
calculate_square_area2()

print("-" * 30)

# length = 5  # global


# def calculate_square_area3():
#     area = length * length  # local


# length = 10  # global
# calculate_square_area2()
# print("面積是", area)

# print("-" * 30)

# length = 5  # global
# area = 3.14 * 10**2  # global


# def calculate_square_area1():
#     area = length * length  # local


# calculate_square_area1()
# print("面積是", area)

# print("-" * 30)

# length = 5
# area = 3.14 * 10**2


# def calculate_square_area5():
#     print("面積是", area)
#     area = length * length
#     print("面積是", area)


#     calculate_square_area5()

print("-" * 30)

length = 5
area = 3.14 * 10**2


def calculate_square_area6():
    area = length * length
    return area


area = calculate_square_area6()
print("面積是", area)

print("-" * 30)

length = 5
area = 3.14 * 10**2


def calculate_square_area7():
    global area
    area = length * length


calculate_square_area7()
print("面積是", area)
