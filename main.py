
def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed == "y":
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedrooms that allow pets, all within a budget of ${max_rent} per month.")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds}, all within a budget of ${max_rent} per month.")


city = input("What city would you like to live in? ")
max_rent = int(input("What is your max rent? "))
min_beds = int(input("At least how many bedrooms do you need? "))
pets_allowed = input("Do you have pets? y/n ")

apt_search1(city, max_rent, min_beds, pets_allowed)

def apt_search2(city, max_rent, min_beds = 2, pets_allowed = "y"):
    if pets_allowed == "y":
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedrooms that allow pets, all within a budget of $ {max_rent} per month.")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds}, all within a budget of $ {max_rent} per month.")


city = input("What city would you like to live in? ")
max_rent = int(input("What is your max rent? "))

apt_search2(city, max_rent)
apt_search2(city, max_rent, min_beds = 4)
apt_search2(city, max_rent, pets_allowed = "n")

x = int(input("Enter a number: "))
plus_one_hundred = lambda x: x + 100
result1 = plus_one_hundred(x)
print(result1)

y = int(input("Enter a number: "))
square_num = lambda y: y ** 2
result2 = square_num(x)
print(result2)

word = input("Enter a word: ")
concatenate = lambda word: "- " + word
result3 = concatenate(word)
print(result3)

z = int(input("Enter a number: "))
divide_by_three = lambda z: z / 3
result4 = divide_by_three(z)
print(result4)