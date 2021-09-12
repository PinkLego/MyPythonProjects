# string x = "Adedayo" # String
# int x = 21 # int/number -21,21, 21.22

#dateOfBirth = "09-August-2010"

#import random
from twilio.rest import Client

account_sid = 'ACfd869b2858830c8b888d04a36c299191'
auth_token = 'd10c6625a44c728f2a8305469265b616'
client = Client(account_sid, auth_token)

# SID = software ID
# daysOfWeek = {1 : "Sunday",
#              2 : "Monday",
#              3 : "Tuesday",
#              4 : "Wednesday",
#              5 : "Thursday",
#              6 : "Friday",
#              7 : "Saturday"}

myFamilyLol = {"Dad": "+447766087860",
               "Ademola": "+447931944137",
               "Bambam": "+447950696557",
               }

message = client.messages \
                .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_=+447400064399,
                    to=myFamilyLol["Bambam"]
                )

print(message.sid)

# print(daysOfWeek[random.randint(1, 7)])
