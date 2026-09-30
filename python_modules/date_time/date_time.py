print("\nDate and Time:- THE datetime module allows us to work with dates. To use datetime module,import it first:\n")
import datetime

# Using : Current Date and Time 

x = datetime.datetime.now()             # now current Date and Time 
print("Now current Date and Time:",x)

print("\nTHE Date Object represenats a date (year, month and date)."\
      "To  create a date object, import it from the datetime module first: from datetime import date\n")



from datetime import date

# Using : Current Date
today = date.today()                # module.function/method()
print("\nToday current Date:",today) # to get the current date, use the date.today()

import datetime

# Using : Current DateTime, 
x2 = datetime.datetime.today() # module.function/method()
print("\nToday current DateTime:",x2) # to get the current dateTime, use the datetime.datetime.today()

# Using : Arguments for datetime
print( "\nCreate a Custom Datetime Object:- The datetime.datetime() constructor takes the following arguments: (year, month, day, hour,minute, second, microseconnd)\n")
import datetime

x3 = datetime.datetime(2027,8,15,22,45,18,564578)
print("\nCustom Datetime with arguments:",x3)

print("\nFormating Datetime String: The strftime() method allow us to do that. it take one parameter, that format.")
import datetime


# Using : Formating Datetime String
d = datetime.datetime.today()
print("Formating datetime:",d.strftime("%B %D %Y")) 
