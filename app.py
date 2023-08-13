#!/usr/bin/env python
# coding: utf-8


from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    translation = None
    if request.method == "POST":
        english_text = request.form["english_text"]
        target_language = request.form["target_language"]
        translation = translate_text(english_text, target_language)
    return render_template("index.html", translation=translation)

def translate_text(input_text, target_language):
    prompt = f"Translate the following English text to {target_language}:\n\n{input_text}\n\nTranslation:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    translation = response.choices[0].text.strip()
    return translation

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




