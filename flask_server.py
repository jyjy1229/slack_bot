# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

import json
from command import getOutputText
from flask import Flask, request, make_response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
 
client = WebClient(token="xoxb-634749716256-5522766081990-qxvQNTW7NsT9y5olUQvXNgg3")
app = Flask(__name__)

def event_handler(event_type, slack_event):
    outputText = ""
    if event_type == "message":
        inputText = slack_event["event"]["text"]
        userId = slack_event["event"]["user"]
        outputText = getOutputText(inputText)
        try:
            result = client.chat_postMessage(
                channel=userId,
                text=outputText
            )
        except SlackApiError as e:
            print(f"Error posting message: {e}")
    return make_response(slack_event["event"], 200, {"content_type": "application/json", 'ngrok-skip-browser-warning': '69420'})
 
@app.route('/', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json", 'ngrok-skip-browser-warning': '69420'})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler (event_type, slack_event)
    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})
 
 
if __name__ == '__main__':
    app.run(debug=True, port=5002)
