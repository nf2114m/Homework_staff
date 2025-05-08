import datetime
time = datetime.datetime.now()
time = time.year
name=str(input("name:"))
year=int(input("birth of year:"))
year=time-year
print(f"{name} is {year} years old")
