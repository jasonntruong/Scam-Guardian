import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

#this works as a python file. I could not implement it into the website though! Clicking the submit button on textGuardian.html is supposed to run this py file but I couldn't get it to work.
#In essence Twilio -> python works but python -> HTML I couldn't get to work.
message = client.messages \
                .create(
                     body="Jason,   It has been brought to our attention that you have an outstanding bill of $300.00!   You must pay this bill at the link below in 24 hours!   Failure to do so will result in an increase of $500 to your bill resulting in you owing Bernie Officiary a total of $800.00!   Complete ASAP or else, Bernie Officiary   Pay here: https://1187Y.trk.elasticemail.com/tracking/click?d=M51_GG4qm-QeKZ_5JIRBgB9mrjOR9MQQzgXxGfQD2BTNWn_VsyKJ-YyMy7bez12Yg8nXzyil133GjwHb10qDbIov1OsdZPWfl4v2hnPvXYwnrYgHToZ0NUQMr8BJOeipUL-RMQoz6rz-2kIk6lGgiiU1",
                     from_='+16475572971',
                     to='+16479045812'  
                 )

print(message.sid)