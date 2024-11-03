from flask import Flask, request
import boto3
import uuid
from datetime import datetime
import markdown
import os

app = Flask(__name__)


def save_data(markdown, html):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    id = str(uuid.uuid4())
    table.update_item(
        Key = {'ID': id},
        UpdateExpression = "set message_markdown=:markdown, message_html=:html, request_date=:sts",
        ExpressionAttributeValues = {
            ':markdown': markdown,
            ':html': html,
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        }
    )


@app.route("/", methods=["GET", "POST"])
def to_markdown():
    if request.method == "GET":
        return "ok"
    elif request.method == "POST":
        if "text" in request.form:
            input_markdown = request.form["text"]
            html = markdown.markdown(input_markdown)
            save_data(input_markdown, html)
            return html


if __name__ == "__name__":
    app.run(host="0.0.0.0", port=8080)
