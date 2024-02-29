vowels={'a','e','i','o','u'}
word=input("Enter a string: ")
# word="aeiou32366"
count=0
for i in word:
    if i in vowels:
        count+=1
print(count)