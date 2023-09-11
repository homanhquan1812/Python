try:
    numerator = int(input("Enter a number to divide: "))
    deonominator = int(input("Enter a number to divide by: "))
    result = numerator / deonominator
    print(result)

except ZeroDivisionError:
    print("This number can't be divided by 0.")

except Exception:
    print("Please check the calculation again.")