from twilio.rest import Client
from dotenv import load_dotenv
import os
from time import localtime
from random import choice
import msgs

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

def get_daily_sched():
    sched = {'am': '', 'pm': '', 'eod': '', 'lunch': ''}

def check_time(current_time):
    """check the time to determine which set of messages to draw from
    morning messages: between 10 and noon
    lunch messages: between 12:20 and 1
    afternoon messages: between 2:30 and 4:30
    go home messages: after 5:30"""

    if current_time.tm_wday < 5:
        if current_time.tm_hour > 10 and current_time.tm_hour < 12:
            msg_list = msgs.am_reminders
        elif current_time.tm_hour > 12 and current_time.tm_min > 20
        and current_time.tm_hour < 13:
            msg_list = msgs.lunch_reminders
        elif current_time.tm_hour > 14 and current_time.tm_min > 30
        and current_time.tm_hour < 16 and current_time.tm_min < 30:
            msg_list = msgs.pm_reminders
        elif current_time.tm_hour > 17 and current_time.tm_min > 30:
            msg_list = msgs.eod_reminders
        else:
            return False

if msg_list:
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


the_schedule = [ get_epochtime(radar.random_datetime(start=window_start, stop=window_end))
for t in range(randint(runs_per_day[0], runs_per_day[1])) ]
