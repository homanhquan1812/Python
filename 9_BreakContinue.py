# Break
while True:
    name = input("Enter your name: ")
    if name != "":
        break
print("Hello, " + name)

# Continue
phoneNumber = "090-687-75-81"

for i in phoneNumber:
    if i == "-":
        continue
    print(i, end="")

# Pass