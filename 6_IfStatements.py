yourAge = int(input("How old are you? "))
legalAge = 18

if yourAge >= 18:
    print("OK, you can buy beer here.")
elif yourAge < 18 and yourAge > 0: # We can use "or"
    print("Sorry, you can't buy beer at this age.")
else:
    print("You're funny.")

# If not()
temperature = int(input("What's the current temperature? "))

if not(temperature >= 25 and temperature <= 35): # -> temperature < 25 or temperature > 35
    print("Ah shit!")
elif not(temperature < 25 or temperature > 35): # -> 25 <= temperature <= 35
    print("Cool!")