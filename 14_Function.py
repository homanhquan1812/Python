def Function(name):
    print("This is a function.")
    print("My name is " + name)

Function("Quan")
print()

lastName = "Ho"

Function(lastName)
print()

def Function2(name, age):
    print("Hello", name + ".")
    print("Your age is", str(age) + ".")

Function2("Quan", 23)
print()

def MathFunction(a, b):
    return a * b

x = MathFunction(2, 3)
print(x)
print()

# Keyword Arguments
def KeywordArguments(firstName, middleName, lastName):
    print("Hello", firstName + ". Your full name is", lastName, middleName, firstName)

KeywordArguments("Quan", "Manh", "Ho")
KeywordArguments(firstName="Thi", middleName="Dieu", lastName="Ho Nguyen")