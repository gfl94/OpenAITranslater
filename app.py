import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        Sentence = request.form["Sentence"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=translate(Sentence),
            temperature=0.6,
        )
        return redirect(url_for("index", result= response.choices[0].text, sentence= Sentence))

    result = request.args.get("result")
    sentence = request.args.get("sentence")
    return render_template("index.html", result=result, sentence=sentence)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

def translate(sentence):
    res = """
    Translate this into English: 
    {}
    """.format(sentence)
    return res