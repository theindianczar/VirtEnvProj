days=int(input("enter the numberof days"))
years = days//365
weeks = (days%365)//7
days_remaining = days-years*365-weeks*7
print(years)
print(weeks)
print(days_remaining)