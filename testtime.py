import datetime


a = datetime.datetime.now()
print(a.astimezone())
print(datetime.datetime.now())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.now().timetz())
# datetime.microsecond
print(datetime.datetime.now().microsecond)
