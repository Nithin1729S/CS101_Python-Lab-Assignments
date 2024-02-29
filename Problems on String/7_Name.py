name=input("Enter your full name: ")
abbr=str()  #way to declare empty string
name=name.split()
last_name=name.pop(-1)
for i in name:
    abbr=abbr+" "+i[0]
abbr=abbr+" "+last_name
print(abbr)


