def checkleap(year):
    if year%400==0 or year%100!=0 and year%4==0:
        return 1
    else:
        return 0


Dict = {'January': 31,
        'February': 29,
        'March': 31,
        'April':30,
        'May':31,
        'June':30,
        'July':31,
        'August':31,
        'September':30,
        'October':31,
        'November':30,
        'December':31}


year=int(input("Enter the year: "))
month=input("Enter the month: ").capitalize()

if checkleap(year):
    if month=='February':
        print(f"The number of days in {month} in a leap year is 29")
    else:
        print(f"The number of days in {month} in a leap year is {Dict[month]}")
else:
    print(f"The number of days in {month} in a leap year is {Dict[month]}")