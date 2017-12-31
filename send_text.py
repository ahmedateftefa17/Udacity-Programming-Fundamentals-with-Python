from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2af7a5d1bc72617f7f66f45f046d1fdf"
# Your Auth Token from twilio.com/console
auth_token  = "514c8e7398c3c20080dcdec466b2f552"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+201141424513", 
    from_="+13137778623",
    body="Hello from Python!")

print(message.sid)
