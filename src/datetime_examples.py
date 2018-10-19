# --------------------------------------------------------
# Some examples of how to use datetime functions in Python
# --------------------------------------------------------
import datetime

now = datetime.datetime.now()

print("-" * 25)
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print("-" * 25)
print("1 week ago it was: ", now - datetime.timedelta(weeks=1))
print("100 days ago it was: ", now - datetime.timedelta(days=100))
print("1 week from now is will be: ",  now + datetime.timedelta(weeks=1))
print("In 1000 days from now is will be: ", now + datetime.timedelta(days=1000))

print("-" * 25)
birthday = datetime.datetime(2019, 6, 12)

print("My birthday is in ... ", birthday - now)
print("-" * 25)