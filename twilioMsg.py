from twilio.rest import Client
from datetime import datetime
def sendMsg(name):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg = name + " has been spotted at " + current_time + " in live cam "
    account_sid = "AC74757cdf275cf0e1b7c1f8a4d964572d"
    auth_token = "31c59a32be01ef01c1907bb3ecd8de9f"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+91 9636133373", 
        from_="+13185368782",
        body=msg)

    print(message.sid)