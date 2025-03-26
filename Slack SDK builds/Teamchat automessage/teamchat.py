import os
import datetime
import calendar
from datetime import date
from datetime import timedelta
from random import randint
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def gen_random_time(_date, _hour, _minute, rand_offset):
    return datetime.datetime.combine(
        _date,
        datetime.time(hour=_hour, minute=_minute+randint(0,rand_offset))
        ).timestamp()

def cal_abbr(month):
    return calendar.month_abbr[month]

OAUTH_TOKEN = "SLACK_SDK_OAUTH_TOKEN"
CHANNEL_NAME = "#slack_sdk_bot_testing"

client = WebClient(token=os.environ[OAUTH_TOKEN])

if __name__ == '__main__':
    try:
        for i in range(1,6):
            sch_date= date.today() + timedelta(days=i)
            if sch_date.weekday() <= 4:
                response = client.chat_scheduleMessage(
                    channel= CHANNEL_NAME,
                    post_at= gen_random_time(_date=sch_date, _hour=17, _minute=50, rand_offset=9),
                    as_user= True,
                    text= "{0} {1} PDY".format(sch_date.day, cal_abbr(sch_date.month))
                    )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
        # Also receive a corresponding status_code
        assert isinstance(e.response.status_code, int)
        print(f"Received a response status_code: {e.response.status_code}")