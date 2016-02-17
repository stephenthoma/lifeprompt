from twilio.rest import TwilioRestClient
import os, sys

VARS = {}
BASE = '/var/www/lifeprompt/'
if os.path.exists(BASE + 'env-vars'):
    for line in open(BASE + 'env-vars'):
        var = line.strip().split('=')
        if len(var) == 2:
            VARS[var[0]] = var[1]

client = TwilioRestClient(VARS['ACCT_SID'], VARS['AUTH_TOK'])

def send_call():
    """Dispatch an outbound call to the user."""
    client.calls.create(to=VARS['PHONE_NUM'],
                        from_=VARS['TWILIO_NUM'],
                        url="http://96.126.126.190/outbound")
def clear_records():
    for record in client.recordings.list()[1:]:
        client.recordings.delete(record.sid)

if __name__ == "__main__":
    if sys.argv[1] == 'send_call':
        send_call()
    elif sys.argv[1] == 'clear_records':
        clear_records()
