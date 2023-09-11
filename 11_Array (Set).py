# Set is a collection which is unordered, unindexed and contains no duplicate values

menu = {"KFC", "Pizza Hut", "Kichi Kichi"}
drinks = {"Pepsi", "Coca Cola", "7-UP", "KFC"}

menu.add("Boiled Chicken")
menu.update(drinks)

for x in menu:
    print(x)

print(menu.difference(drinks))