# Integer should convert to string to add both of them
name = "surendra"
age = 28

print("my name is", name + "and age is " + str(age))


# F string

first_name = "surendra"
last_name = "Veeramallu"
age = 28
print(f"My first name is {first_name} and last name is {last_name} and I am {age}" )



# strings using the format keyword
first_name = 'surendra'
last_name = 'goud'
age = 28
print("my name is {} {} and age is {} years old ".format(first_name, last_name, age))

fname = "kanthi kiran"
age = "30"
lname = "gandi"
print("{} {} is {} years old".format(fname, lname, age))


# Replacing variable inside the format
name = "surendra"
greeting = "How are you {name}?"
final_greeting = greeting.format(name = "Goud")
print(final_greeting)

# usually f strings are using in the programming
