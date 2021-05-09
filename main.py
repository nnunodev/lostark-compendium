from flask import Flask, render_template, request
import aws as aws
import boto3


app = Flask(__name__)

# db server settings

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=aws.ACCESS_KEY,
                          aws_secret_access_key=aws.SECRET_KEY,
                          region_name = aws.REGION
                          )


@app.route('/')
def index():
    return(render_template('index.html'))
 
