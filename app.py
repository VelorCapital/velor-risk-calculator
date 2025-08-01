from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    warning = None

    if request.method == "POST":
        try:
            account_balance = float(request.form["account_balance"])
            risk_percent = float(request.form["risk_percent"])
            stop_loss_pips = float(request.form["stop_loss_pips"])
            pair = request.form["pair"]

            risk_amount = (risk_percent / 100.0) * account_balance

            # Default pip value per lot (approximate, varies by pair)
            pip_value = 10
            if pair == "XAUUSD":
                pip_value = 1  # Gold
            elif pair in ["US30", "NAS100", "SPX500"]:
                pip_value = 1  # Indices

            lot_size = round(risk_amount / (stop_loss_pips * pip_value), 2)
            potential_loss = round(lot_size * stop_loss_pips * pip_value, 2)

            result = {
                "risk_amount": round(risk_amount, 2),
                "lot_size": lot_size,
                "potential_loss": potential_loss
            }

            if risk_percent > 5:
                warning = "⚠️ You are risking more than 5% of your account. This is not recommended."

        except ValueError:
            warning = "Please enter valid numeric values."

    return render_template("index.html", result=result, warning=warning)

if __name__ == "__main__":
    app.run(debug=True)
            
