



# asking users for the name
user_name = input('Enter your name: ')
my_name = "surendra"
print(f'Hi {user_name}, my name is {my_name}')

# convert integer to String
# Every out come of input method is string
# If string multipled by string results addion of strings
# eg- =str3*str2 results 33
try:
 user_name = input('Enter your name: ')
 user_age = int(input('Enter your age: '))
 print(f'Hi {user_name}, your {user_age * 12} months old')
except: print('Invalid entry')