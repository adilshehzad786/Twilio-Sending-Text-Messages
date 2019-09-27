from twilio.rest import Client

account_sid="AC1f52d69fc*************"
AuTH_Token="732468c63138*************"

client=Client(account_sid,AuTH_Token)
call=client.messages.create(

 to="****************",
from_="*************",

body="Hello There"

)
print(call.sid)
print("Done")