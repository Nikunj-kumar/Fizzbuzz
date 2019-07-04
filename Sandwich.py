print("Welcome to the Cafe")
x = input("What are you looking for sir  - ")
if x == 'cheese':
    che_type = input("In che which type 'cheddar' or 'machango'  - ")
    if che_type == 'cheddar':
        print("Here is your cheddar")
    elif che_type == 'machango':
        print("Here is your machango")
    else:
        print("We don't have this in che")
elif x == 'veg':
    print("here is your veggie")
else:
    print("Sorry sir, we don't have this")




