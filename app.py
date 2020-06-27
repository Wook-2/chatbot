# import files
import os
from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app = Flask(__name__)


pairs = [
    ['(Hi|Hello)', ['Hello! nice to meet you!', 'Hi! Nice to meet you!']],
    ['(.*)where(.*)you(.*)liv(.*)', ["I'm living in Bundang!"]],
    ['what(.*)you(.*)name(.*)', ["My name is Byungwook Son!"]],
    ['what(.*)your(.*)hobby(.*)', ['my hobby is playing game!', 'I like to playing soccer!']],
    ['how old(.*)you(.*)', ["I'm 23 years old!"]],
    ['where(.*)you(.*)located(.*)', ["I'm located in Bundang!"]],
    ['do you have(.*)dream(.*)', ['I want to be a person who makes funny game!']],
    ['(.*)you(.*)work hard(.*)', ['Sure, I will do my best!']],
    ['(.*)thank(.*)|(.*)bye(.*)', ["Thank you for talking to me! Have a nice day!"]],
    ['what(.*)ask(.*)you(.*)', ['you can ask me about hobby, age, area ..']]
]

chat = Chat(pairs)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    reply = chat.respond(userText)
    if reply is not None:
        return str(chat.respond(userText))
    else:
        return "I can`t understand. Another question plz."


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
