# word=input("Enter a string: ")
word="Hi There Hello 45 y"
word_list=word.split()
print(word_list)
min_len=1000
small=""
for i in word_list:
    if len(i)<min_len:
        min_len=len(i)
        small=i
print(small)
