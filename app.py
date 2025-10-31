from flask import Flask, render_template, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

# English → French model (you can change 'en-fr' to 'en-hi', 'en-de', etc.)
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


@app.route("/")
def home():
    return render_template("index.html")  # serves the UI page


@app.route("/translate", methods=["POST"])
def translate():
    # get JSON data from frontend
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"translated_text": "Please enter some text to translate."})

    # process translation
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    output = tokenizer.decode(translated[0], skip_special_tokens=True)

    return jsonify({"translated_text": output})


if __name__ == "__main__":
    app.run(debug=True)
