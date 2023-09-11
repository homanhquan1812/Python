import random

x = random.randint(1, 10)
y = random.random() # 0 <= y <= 1

print(x)
print(y)

menu = ["KFC", "Pizza Hut", "Lotteria"]
z = random.choice(menu)

print(z)

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(cards)

print(cards)