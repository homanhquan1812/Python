name = "ho manh quan"

if (name[0].islower()):
    name = name.capitalize()

print(name)
capitalizedLastName = name[8:12].upper() # 12 - 8 = 4 letters, still counts from 0
capitalizedSurName = name[:3].upper()
capitalizedLastName2 = name[8:].upper()

print(capitalizedLastName)
print(capitalizedSurName)
print(capitalizedLastName2)