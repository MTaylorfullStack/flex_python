import random

print(round(random.random()*100))




# print("Hello World")

# dissecting functions

## write a function that prints a greeting to the terminal

def print_greeting(person):
    print(person)
    print("Hello! This is my wonderful greeting!")
    return 10

# current_health=print_greeting("Ronnie")
# print(current_health, " This is the 'current health'")

## CHALLENGE: Update that function to say a personalized greeting in the terminal




x = [ [5,2,3], [10,8,9] ]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# change the 10 in x to a 15
x[1][0]=15

# change value 2 to 4
x[0][1] = 4
# print(x)

# change Jordan in students to Taylor?
students[0]['last_name']  ="Taylor"
# print(students)

# change Ronaldo to Ronnie
sports_directory['soccer'][1] = "Ronnie"
# print(sports_directory)










