# It's a paramater that will pack all arguments into a tuple so that a function can accept
# varying amount of variables

def Total(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(Total(1, 2, 3, 4, 5, 6, 7, 8, 9))

def TotalEdited(*arg2):
    sum = 0
    arg2 = list(arg2)
    arg2[0] = 0 # This code won't work if the above code isn't there
    for i in arg2:
        sum += i
    return sum

print(TotalEdited(1, 2, 3, 4, 5, 6, 7, 8, 9))

# kwargs

def PrintName(**kwarg):
    # print("Hello", kwarg['surname'], kwarg['middlename'], kwarg['firstname'])
    print("Hello", end=" ") # Without end=" ", it will end line
    for key, value in kwarg.items():
        print(value, end=" ")

PrintName(surname="Ho", middlename="Manh", firstname="Quan")