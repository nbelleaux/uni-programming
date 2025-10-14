"""
This program does something or other
"""
celsius = 50 # temparature in celsius
fahrenheit = (celsius * 9/5) + 32 # convert to fahrenheit
print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit") # prints the temperature in Celsius and Fahrenheit
"""
Changing the value of celsius to see the effect on fahrenheit. 
Celsius can be changed to any value and the program will still work.
"""

print(type(celsius)) # prints the type of the variable celsius

is_raining = False # boolean variable to indicate if it is raining
print(type(is_raining))

weather_condition = "Sunny" # string variable to indicate the weather condition
print(type(weather_condition))

question = "Why does python allow you to change a variable type later?" # string variable to store a question
print(type(question))

answer = "Variables do not have fixed types, they are determined at the runtime." # string variable to store an answer

name = "nat"
course = "BSc Computer Science (Cybersecurity, Networks & Forenics)"
language = "Python"

cat = name + " is studying " + course + " and learning " + language
print(cat)

fmr1 = "My name is {fname}, I am studying {course} and learning {language}"
print(fmr1.format(fname=name, course=course, language=language))

while True:
    try:
        age = int(input("Please enter your age: "))
        break
    except ValueError:
        print("Please enter a valid age, try again")
if age < 18:
    print("You are a child.")
elif age >= 18 and age <= 21:
    print("You are a young adult.")
elif age > 130:
    print("Please enter a valid age, try again")
else:
    print("You are an adult.")

print(question + " — " + answer)
