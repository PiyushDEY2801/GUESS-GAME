from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize the jackpot and attempt count if not already set
    if "jackpot" not in session or "count" not in session:
        session['jackpot'] = random.randint(1, 100)
        session['count'] = 0

    message = ""
    if request.method == "POST":
        guess = int(request.form["guess"])
        session['count'] += 1
        jackpot = session.get('jackpot')

        if guess < jackpot:
            message = "Guess Higher!"
        elif guess > jackpot:
            message = "Guess Lower!"
        else:
            message = f"Congratulations! You guessed it in {session['count']} attempts!"
            # Reset the game
            session['jackpot'] = random.randint(1, 100)
            session['count'] = 0

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
