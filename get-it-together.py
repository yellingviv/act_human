from twilio.rest import Client
from dotenv import load_dotenv
import os
from time import localtime
from random import choice
import msgs
import sched

load_dotenv()
# account_sid = os.getenv('SID')
# auth_token = os.getenv('TOKEN')
# sender = os.getenv('TW_NUMBER')
to = os.getenv('USER_NUMBER')
test_sid = os.getenv('SID_TEST')
test_token = os.getenv('TOKEN_TEST')
test_send = os.getenv('TW_TEST')

client = Client(test_sid, test_token)
current_time = localtime()

while True:
    """loop to keep generating a new daily schedule"""

    if current_time.tm_wday < 5:
        """check that it's a weekday"""
        today_sched = sched.get_daily_sched()
        for event in today_sched:
            while time.strftime("%H:%M", current_time) < today_sched[event]['today']:
                sleep(today_sched[event]['today'] - time.strftime("%H:%M", current_time))
            send_text(time.strftime("%H:%M", current_time))


def check_time(time_window):
    """check to determine which set of messages to draw from"""

        if time_window == today_sched['am']['today']:
            msg_list = msgs.am_reminders
        elif time_window == today_sched['am']['today']:
            msg_list = msgs.lunch_reminders
        elif time_window == today_sched['am']['today']:
            msg_list = msgs.pm_reminders
        elif time_window == today_sched['am']['today']:
            msg_list = msgs.eod_reminders

        return msg_list

def send_text(time_window):
    """Send text reminding me to be a human"""

    msg_list = check_time(time_window)
    body_text = choice(msg_list)

    message = client.messages.create(
        to=to,
        from_=test_send,
        body=body_text)

    print(message.sid)
    print(message.body)
    print(message.error_message)
