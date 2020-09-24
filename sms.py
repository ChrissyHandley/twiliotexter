from twilio.rest import Client


account_sid = 'AC83b951475648b98859265d4ec686b1cd'
auth_token = 'b20592bdebf3ceff1581328b4ee381fd'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Guess who Hank?",
                     from_='+19712479952',
                     to='+13522995988'
                 )

print(message.sid)
