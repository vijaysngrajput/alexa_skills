from flask import Flask
from flask_ask import Ask, statement, question
import json
import time
import requests
import unidecode



from my_weather import give
from playyoutube import youtubeBot
from aws_watcher import extractPrice

app = Flask(__name__)
ask = Ask(app,"/app_name")

@app.route('/')
def homepage():
    return "hi bro...your time has begin"


@ask.launch
def start_skill():
    welcome_message = "*******msg*****"
    return question(welcome_message)

@ask.intent("nikal")
def nikalab():
    return statement("jara hu")


@ask.intent("your city")
def kashipurab():
    summ, temp = give("your city")
    mausam = "city ka {} scene hai and {} temperature hai".format(summ,temp)
    return question(mausam).reprompt("aur kuch")


@ask.intent("playYoutube")
def videomy():
    ex = youtubeBot("https://www.youtube.com/watch?v=QEkk5QyO-c0")
    ex.playvideo()
    return statement("enjoy video")

@ask.intent("watcher")
def awswatcher():
    extractPrice()
    return statement("email sent")

if __name__ == "__main__":
    app.run(debug=True)