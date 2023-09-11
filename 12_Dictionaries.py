capitals = {"USA": "Washington DC", 
            "Vietnam": "Ha Noi",
            "Japan": "Tokyo"}

print(capitals.get("Thailand"))
print(capitals.keys()) # Country
print(capitals.values()) # Capital
print(capitals.items())
print()

for keys, values in capitals.items():
    print(keys + ": " + values)