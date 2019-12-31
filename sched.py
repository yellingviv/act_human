import random
import time

sched = {'am': {'lower': 10, 'upper': 11, 'today': ''},
        'pm': {'lower': 14, 'upper': 17, 'today': ''},
        'eod': {'lower': 17, 'upper': 18, 'today': ''},
        'lunch': {'lower': 12, 'upper': 12, 'today': ''}}

sched_list = []

def get_daily_sched():
    """generate a daily schedule of randomized time windows within constraints
    append each time to a list, to keep an ordered set of times for later"""

    for window in sched:
        sched_item = get_time(sched[window]['lower'], sched[window]['upper'])
        sched[window]['today'] = sched_item
        sched_list.append(sched_item)

    return sched


def get_time(lower, upper):
    """generates random time between lower and upper bounds and returns time str"""

    hour = random.randint(lower, upper)
    minute = random.randint(0, 60)
    go_time = str(hour) + ':' + str(minute)

    return go_time
