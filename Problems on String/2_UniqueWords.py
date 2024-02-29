word=input("Enter a string: ")
# word="Hi there Hello hi"
word=word.lower()
set_of_words=list(set(word.split()) )    #split converts string to a list and we convert list to a set
for i in set_of_words:
    print(i)

