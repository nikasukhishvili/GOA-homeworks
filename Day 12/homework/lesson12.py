first_name = input("Enter your first name: ")
surname = input("Enter your last name: ")
age = input("Enter your age: ")
residence = input("Enter your place of residence: ")
list = []
list.append(first_name)
list.append(surname)
list.append(age)
list.append(residence)
print("1:", list[:2])
print("2:", list[1:3])
print("3:", list[:3])
print("4:", list[1:])

negative_number = int(input("enter a negative number: "))
negative_numbers_to_zero = []
for i in range(negative_number, 0):
    negative_numbers_to_zero.append(i)
print("list of negative numbers:", negative_numbers_to_zero)

full_name = "nika sukhishvili"
print("first name:", full_name[:4])
print("last name:", full_name[5:])

favorite_movies = ["saving private ryan", "barbie", "Nika keshelava the movie", "Pirates of the Shavi sea", "Fight clan"]
print("Combination 1:", favorite_movies[:3])
print("Combination 2:", favorite_movies[2:])
print("Combination 3:", favorite_movies[1:4])
print("Combination 4:", favorite_movies[:-2])

# Task 5
academy_name = input("Enter the name of the academy: ")
if academy_name.startswith("G"):
    print("Goa is the best choice.")
else:
    print("You made a wrong decision.")
