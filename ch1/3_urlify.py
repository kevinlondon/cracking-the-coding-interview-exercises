def urlify(string, length):
    index = 0
    characters = []
    for char in string:
        if char == " ":
            characters += ["%", "2", "0"]
        else:
            characters.append(char)

        index += 1
        if index == length:
            return "".join(characters)

print(urlify("Mr John Smith    ", 13))
print(urlify("Rob Dog  ", 7))
