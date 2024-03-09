import string

name = "D44d"

def is_ascii_letters_only(name):
    return all(char in string.ascii_letters for char in name)
print(is_ascii_letters_only(name))

if (char in string.ascii_letters for char in name):
    print(name)
else: print("&&&&")