import logging
from flask import Flask, render_template, request
from chatterbot import ChatBot
from FatequinoChatBot import FatequinoChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


bot = ChatBot('Fatequino Chat Bot',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[ 'chatterbot.logic.BestMatch' ],
    filters=[ 'chatterbot.filters.RepetitiveResponseFilter' ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)

#bot = ChatBot("Fatequino ChatBot")
fatequinoChatBot = FatequinoChatBot(bot, ChatterBotCorpusTrainer)
fatequinoChatBot.treinarBot("chatterbot.corpus.portuguese")


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/get", methods=['GET'])
def get_bot_response():
    userText = request.args.get('msg')
    return str(fatequinoChatBot.mensagemEnviada(userText))

if __name__ == "__main__":
    app.run()

