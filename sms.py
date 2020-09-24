from twilio.rest import Client


account_sid = '........'
auth_token = '.........'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Guess who?",
                     from_='+0000000000',
                     to='+0000000000'
                 )

print(message.sid)
