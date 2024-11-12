import datetime
YYYY = 2000
MM = 7
DD = 7
today = datetime.datetime.now()
print(f"Today is {today.strftime('%A')}, {today.strftime('%B')}  {today.day}, {today.year} ")

#Define birthday
birthday = datetime.date(YYYY, MM, DD)
print(f"My birthday is {birthday.strftime('%m/%d/%Y')}")


#Date 90 days from today
ninety_d = today + datetime.timedelta(days=90)

#Define dinner time
dinner_time = datetime.time(18, 30)
print(f"Let's meet for dinner at {dinner_time.strftime('%I:%M %p')}")



