from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"translated_text": "Please enter some text to translate."})
    try:
        translated = GoogleTranslator(source="auto", target="fr").translate(text)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"translated_text": f"Error: {e}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
