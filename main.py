from flask import flask, render_template, request
import boto3


app = flask(__name__)

# db server settings

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY,
                          aws_session_token=SESSION_TOKEN)

@app.route('/')
    def index():
        return(render_template('index.html'))