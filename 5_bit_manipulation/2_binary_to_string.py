def decimal_to_binary(d):
    string = ["."]
    while d:
        if len(string) > 32:
            print("ERROR")
            return

        d *= 2
        if d >= 1:
            string.append(1)
            d -= 1
        else:
            string.append(0)

    return "".join([str(char) for char in string])


print(decimal_to_binary(0.25))
