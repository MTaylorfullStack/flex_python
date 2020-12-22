# print("Hello World")

# variables and data types

# strings
kitchen = "pots and pans"

string_of_numbers= '123u4234389394'

print(len(kitchen))

# numbers
# operators; +, -, *, /

print("*"*100)

# lists

students=["Emily",6,7,8, "Ronnie", "Stan", "James"]

print(len(students))

# booleans

result = True 

# dictionaries

ninja={
    'name':"Michael",
    'fav_lang':"Python",
    'skills': ["nunchuck", "bowstaff"]
}

print(ninja['skills'][0])

# conditionals

timmy_takes_trash="10"


# if timmy_takes_trash==True:
#     print("Timmy gets allowance")
# elif timmy_takes_trash=="10":
#     print("What happened?")
# else:
#     print("Timmy gets grounded")


## loops

# for(var i=0; i<100; i++){
#     //do some stuff
# }

# for iterator in range(100):
#     print(iterator)


ninja={
    'name':"Michael",
    'fav_lang':"Python",
    'skills': ["nunchuck", "bowstaff"]
}

# for...in loops


for attribute in ninja:
    print(attribute)
    print(ninja[attribute])

# functions

def say_hello(name):
    print(f"Hello {name}!!")


for i in range(10):
    say_hello("James")

