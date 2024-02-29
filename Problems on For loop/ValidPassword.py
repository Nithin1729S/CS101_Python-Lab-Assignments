capital="QWERTYUIOPASDFGHJKLZXCVBNM"
small="qwertyuiopasdfghjklzxcvbnm"
digit="1234567890"
cap=0
small_=0
digit_=0
password=input("Enter a password: ")
if 8<=len(password)<=16:
    for i in password:
        if i.isupper():
            cap+=1
        elif i.islower():
            small_+=1
        elif i.isdigit():
            digit_+=1
    if cap>0 and small_>0 and digit_>0 and small_+digit_+cap==len(password):
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password")










