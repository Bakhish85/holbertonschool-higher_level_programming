def uppercase(str):
    for index, char in enumerate(str):
        if index == len(str) - 1:
            char = chr(ord(char) - 32)
            print(char)
        else:
            if ord(char) >= 97:
                char = chr(ord(char) - 32)
                print(char, end="")
