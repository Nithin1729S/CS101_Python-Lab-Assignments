def togglecase(word):
    toggle=str()
    for i in word:
        if i.isupper():
            i=i.lower()
            toggle=toggle+i
        else:
            i=i.upper()
            toggle+=i

    return toggle

print(togglecase("GuDDuBHaiyA"))



