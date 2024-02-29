Dict = {'January': 31,
        'February': [28,29],
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

month_name=input("Enter the month name:").capitalize()
if month_name in Dict:
        if month_name=='February':
                response=input("Is this a leap year(Y/N): ").capitalize()
                if response=='Y':
                        print(f"The number of days in {month_name} in a leap year are {Dict[month_name][1]}")
                else:
                        print(f"The number of days in {month_name} in a non leap year are {Dict[month_name][0]}")
        else:
                print(f"The number of days in {month_name} are {Dict[month_name]}")
else:
        print("Enter a valid month")

