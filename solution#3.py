names = input()
abbrev = ""

for name in names.split("-"):
    abbrev = abbrev + name[0]

print(abbrev)
