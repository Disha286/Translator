from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

LANGUAGES = GoogleTranslator.get_supported_languages(as_dict=True)

@app.route("/")
def index():
    return render_template("index.html", languages=LANGUAGES)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "").strip()
    target = data.get("target", "kn")
    if not text:
        return jsonify({"translated": "", "error": "No text provided."})
    try:
        translated = GoogleTranslator(source="en", target=target).translate(text)
        return jsonify({"translated": translated})
    except Exception as e:
        return jsonify({"translated": "", "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)