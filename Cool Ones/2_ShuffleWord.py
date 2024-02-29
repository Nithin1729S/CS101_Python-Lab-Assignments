import itertools

def retained(a):
    count=0
    for i in range(len(wrd)):
        if wrd[i]==a[i]:
            count+=1
    return count

def word_shuffle(word):
    global wrd
    wrd=word
    lst = []
    for s in itertools.permutations(word):
        if s not in lst:
            lst.append(''.join(s))

    lst = sorted(lst, key=retained)
    result=f"{word},{lst[0]},({retained(lst[0])})"
    return result

print(word_shuffle("grrrr"))

