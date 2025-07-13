from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message", "").lower()

    if "hello" in user_input or "hi" in user_input:
        response = "Hi there! How can I help you today?"
    elif "name" in user_input:
        response = "I am SmartBot, your virtual assistant."
    elif "how are you" in user_input:
        response = "I am just code, but I am running perfectly!"
    elif "bye" in user_input:
        response = "Goodbye! Have a great day!"
    elif "thank you" in user_input:
        response = "Your Welcome!Is there anything else I can help you with?"
    elif "kiet" in user_input:
        response = ("Sure! Kakinada Institute of Engineering and Technology is nearly located to Kakinada. "
                    "The first college in South India. It is the only one college that offers only Emerging courses. "
                    "This college believes in innovation, leadership, and building real-world skills.")
    else:
        response = "Sorry, I didn't understand that. Can you rephrase?"

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
