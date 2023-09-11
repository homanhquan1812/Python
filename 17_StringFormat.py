fullname = "Ho Manh Quan"
university = "HCMUT"

print(fullname, "is studying at", university)
print("{} hates {}".format(fullname, university)) # Number inside {} will be assigned in order (0, 1, 2...)
print("{1} hates {0}".format(fullname, university))

text = "{} loves {}"
print(text.format(fullname, university))