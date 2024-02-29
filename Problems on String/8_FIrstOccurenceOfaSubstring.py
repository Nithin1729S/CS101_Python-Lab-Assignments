



s = "the is dude is a cool dude"
print(s.find('dude'))   #returns the first index of dude...ie d
print(s.find('t'))
print(s.find('z'))   #returns -1 if the character is not found
#print(s.index('z'))
print(s.rfind('dude'))   #searches from right to left

#index and find are the same just that find returs -1 if character not found but index return a value error