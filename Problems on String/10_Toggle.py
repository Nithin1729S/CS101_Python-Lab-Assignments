def toggle_case(s):
    swapped=""
    for char in s:
        if char.islower():
            swapped+=char.upper()
        elif char.isupper():
            swapped+=char.lower()
        else:
            swapped+=char
    return swapped

print(toggle_case("Hi there HellO"))

