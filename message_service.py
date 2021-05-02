import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


message = client.messages \
    .create(
        messaging_service_sid='MG2a69deff965a7f2e5c92fd802489eb7b',
        body='VIRUS BELOW\nhttp://www.jason-truong.com/',
        to='+16479045812'
    )

print(message.sid)