#first class practice
#print hello world
print("Hello World")


#pycahe example h ye
def greet(name):
    return f"Hello, {name}!"

print(greet("MukanKhan"))

def greet(name):
    return f"Hello what do you do,{name}!"

print(greet("MuskanSirajkhan"))


# data types

# string
name = "muskan"

# integer
age = 21

# float
height = 5.7

# boolean
is_student = True

# list
#list ek asa structure h jismy hm multiple values ko ek hi variable m  store krskty hen
grades = [95, 83, 90, 87, 74]

# tuple
#  tuple bh ek asa structure h jismy hm multiple values ko ek hi variable m  store krskty hen mgr value change nh hoga ismy fixed hota h
# Python me coordinate ka matlab kisi bhi point ki exact position ko define karna hota hai, jo aksar (x, y) ya (x, y, z) ke form me hota hai.


coordinates = (3, 5)

# dictionary
person = {"name": "muskan", "age": 19, "height": 5.7}

# set
unique_numbers = {1, 2, 3, 4, 5}

print(name, age, height, is_student, grades, coordinates, person, unique_numbers)
