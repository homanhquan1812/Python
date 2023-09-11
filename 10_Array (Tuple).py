# Tuple is a collection which is ordered and unchangeable used to group related data together

# 1D Array
menu = ["KFC", "Pizza Hut", "Kichi Kichi"] # Có thể dùng menu = ()

print(menu)
print(menu[0])
print()

for i in menu:
    print(i)

print()
# Check out some commands: append(), remove(), pop(), insert(), sort(), clear(),...

# 2D Array
drinks = ["Pepsi", "Coca Cola", "7-UP"]
food = ["Medium-Rare Beef", "Fried Chicken"]

menu = [drinks, food]

print(menu)
print(menu[1][1]) # Fried Chicken