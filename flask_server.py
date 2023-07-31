import json
from command import getOutputText
from data import BotToken, BotUserId, AdminUserId, missions
from flask import Flask, request, make_response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime, timedelta, timezone

client = WebClient(token=BotToken)
app = Flask(__name__)

def make_log(text):
    print(datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초") + text)

def schedule_messages(userId):
    korea_timezone = timezone(timedelta(hours=9))
    korea_now = datetime.now().astimezone(korea_timezone)
    korea_today = korea_now.replace(hour=0, minute=0, second=0, microsecond=0)
    for mission in missions:
        post_datetime = korea_today + timedelta(days=mission["post_day"], hours=mission["post_time"])
        post_at = int(post_datetime.timestamp())
        sendMessage(AdminUserId, "미션" + mission["idx"] + "이 " + post_datetime.strftime("%Y년 %m월 %d일 %H시 %M분") + "에 예약되었습니다.")
        try:
            client.chat_scheduleMessage(channel=userId, text=mission["text"], post_at=post_at)
            make_log("schedule mission " + mission["idx"])
        except SlackApiError as e:
            print(f"Error posting message: {e}")

def sendMessage(channel, text):
    try:
        client.chat_postMessage(
            channel=channel,
            text=text
        )
        make_log("send message " + text + " to " + channel)
    except SlackApiError as e:
        print(f"Error posting message: {e}")

def event_handler(event_type, slack_event):
    if event_type == "message":
        inputText = slack_event["event"]["text"]
        userId = slack_event["event"]["user"]
        onHandleMessage(inputText, userId)
    elif event_type == "member_joined_channel":
        userId = slack_event["event"]["user"]
        onHandleMemberJoin(userId)
    return make_response(slack_event["event"], 200, {"content_type": "application/json"})

def onHandleMessage(inputText, userId):
    outputText = getOutputText(inputText)
    if userId != BotUserId:
        sendMessage(userId, outputText)

def onHandleMemberJoin(userId):
    sendMessage(AdminUserId, "ted bot에 신규 입사자가 등록되었습니다.")
    schedule_messages(userId)

@app.route('/', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    print(slack_event)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler (event_type, slack_event)
    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
