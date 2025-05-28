from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    result = None
    if request.method == "POST":
        Caesar = CaesarCipher()
        action = request.form.get("action")
        if action == "encrypt":
            text = request.form.get("inputPlainText", "")
            key = int(request.form.get("inputKeyPlain", 0))
            result = {
                "type": "encrypt",
                "text": text,
                "key": key,
                "result": Caesar.encrypt_text(text, key)
            }
        elif action == "decrypt":
            text = request.form.get("inputCipherText", "")
            key = int(request.form.get("inputKeyCipher", 0))
            result = {
                "type": "decrypt",
                "text": text,
                "key": key,
                "result": Caesar.decrypt_text(text, key)
            }
    return render_template("caesar.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
