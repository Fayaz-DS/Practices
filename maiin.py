import datetime, bday_messages
today = datetime.date.today()
print(f"Today's date is: {today}")
next_birthday = datetime.date(2025, 10, 2)
days_until_birthday = (next_birthday - today).days
if days_until_birthday == 0:
    print(bday_messages.random_message)
else:
    print(f"There are {days_until_birthday} days until my next birthday.")