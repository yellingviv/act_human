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
current_time = time.localtime()

today_sched = sched.get_daily_sched()

def check_time(current_time):
    """check the time to determine which set of messages to draw from"""

    if current_time.tm_wday < 5:
        """check if it's a weekday"""
        if current_time.tm_hour == today_sched['am']['today'].tm_hour
        and current_time.tm_min == today_sched['am']['today'].tm_min:
            msg_list = msgs.am_reminders
        elif current_time.tm_hour == today_sched['lunch']['today'].tm_hour
        and current_time.tm_min == today_sched['lunch']['today'].tm_min:
            msg_list = msgs.lunch_reminders
        elif current_time.tm_hour == today_sched['pm']['today'].tm_hour
        and current_time.tm_min == today_sched['pm']['today'].tm_min:
            msg_list = msgs.pm_reminders
        elif current_time.tm_hour == today_sched['eod']['today'].tm_hour
        and current_time.tm_min == today_sched['eod']['today'].tm_min:
            msg_list = msgs.eod_reminders

body_text = choice(msg_list)

message = client.messages.create(
    to=to,
    from_=test_send,
    body=body_text)

print(message.sid)
print(message.body)
print(message.error_message)


# time.localtime() returns:
# year, month, day of the month - month day
# tm_wday is 0-6, monday is 0 (saturday = 5, sunday = 6) - week day
# yday is year day
# hours, minutes, second - hour is 0-23
