from twilio.rest import Client
from dotenv import load_dotenv
import os
import time
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


def get_sleep_time(actual_time, event_time):
    """calculate the amount of time between now and a given event, in seconds"""

    actual = actual_time.split(':')
    now_hour = int(actual[0])
    now_min = int(actual[1])
    now_in_seconds = ((now_hour * 60) * 60) + (now_min * 60)
    event = event_time.split(':')
    event_hour = int(event[0])
    event_min = int(event[1])
    event_in_seconds = ((event_hour * 60) * 60) + (event_min * 60)

    time_difference = event_in_seconds - now_in_seconds

    return time_difference


def check_time(time_window):
    """check to determine which set of messages to draw from"""

    msg_list = []
    window = time_window
    if window == today_sched['am']['today']:
        msg_list = msgs.am_reminders
    elif window == today_sched['am']['today']:
        msg_list = msgs.lunch_reminders
    elif window == today_sched['am']['today']:
        msg_list = msgs.pm_reminders
    elif window == today_sched['am']['today']:
        msg_list = msgs.eod_reminders

    return msg_list


def send_text(time_window):
    """Send text reminding me to be a human"""

    window = time_window
    msg_list = check_time(window)
    body_text = choice(msg_list)

    message = client.messages.create(
        to=to,
        from_=test_send,
        body=body_text)

    print(message.sid)
    print(message.body)
    print(message.error_message)


while True:
    """loop to keep generating a new daily schedule"""

    if current_time.tm_wday < 5:
        """check that it's a weekday"""
        today_sched = sched.get_daily_sched()
        for event in today_sched:
            if time.strftime("%H:%M", current_time) > today_sched[event]['today']:
                break
            """for each event, check if time to run. if not, sleep until go time"""
            while time.strftime("%H:%M", current_time) < today_sched[event]['today']:
                sleeptime = get_sleep_time(time.strftime("%H:%M", current_time), today_sched[event]['today'])
                time.sleep(sleeptime)
            send_text(time.strftime("%H:%M", current_time))
