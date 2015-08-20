from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Hi!!",
    to="+XXXXXXXX",    # Replace with your phone number
    from_="+XXXXXXXX") # Replace with your Twilio number
print (message.sid)
