
from flask import Flask, render_template, request

app = Flask(__name__)

# Currency pip values (custom pip values for major instruments)
pip_values = {
    'EURUSD': 10, 'USDJPY': 9.13, 'GBPUSD': 10, 'XAUUSD': 1,
    'US30': 1, 'NAS100': 1, 'SPX500': 1
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    warning = ""
    if request.method == 'POST':
        account_balance = float(request.form['account_balance'])
        risk_percent = float(request.form['risk_percent'])
        pair = request.form['pair']
        stop_loss_pips = float(request.form['stop_loss_pips'])

        risk_amount = (risk_percent / 100) * account_balance

        pip_value = pip_values.get(pair.upper(), 10)
        lot_size = risk_amount / (stop_loss_pips * pip_value)
        potential_loss = stop_loss_pips * pip_value * lot_size

        if risk_percent > 5:
            warning = "⚠️ Warning: Risking more than 5% of your account!"

        result = {
            'risk_amount': round(risk_amount, 2),
            'lot_size': round(lot_size, 2),
            'potential_loss': round(potential_loss, 2)
        }

    return render_template('index.html', result=result, warning=warning)

if __name__ == '__main__':
    app.run(debug=True)
