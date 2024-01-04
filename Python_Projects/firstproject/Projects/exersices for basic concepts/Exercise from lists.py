num = str(input("Phone: "))
skaiciai = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in num:
    output += skaiciai.get(ch, "!") + " "
print(output)