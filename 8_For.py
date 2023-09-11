import time

for i in range(10): # i starts from 0 to 9
    print(i)

for j in range(50, 100): # j starts from 50 to 99
    print(j)

for k in range(0, 10, 2): # k starts from 0 to 9, distance = 2
    print(k)

print("")

for countDown in range(10, 0, -1):
    print(countDown)
    time.sleep(1)
print("Happy New Year!")

print("")

column = int(input("Enter the number of column: "))
row = int(input("Enter the number of row: "))
symbol = input("Enter your desired symbol: ")

for i in range(row):
    for j in range(column):
        print(symbol, end="")
    print()
