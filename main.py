from flask import Flask, render_template, request
import math

app = Flask(__name__)

server = app.server

def calculate_monthly_payment(principal, annual_interest, years):
    monthly_interest = annual_interest / 100 / 12
    number_of_payments = years * 12

    math_power = math.pow(1 + monthly_interest, number_of_payments)
    monthly_payment = principal * (monthly_interest * math_power / (math_power - 1))

    return monthly_payment


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        annual_interest = float(request.form['annual_interest'])
        years = int(request.form['years'])

        monthly_payment = calculate_monthly_payment(principal, annual_interest, years)

        return render_template('index.html', monthly_payment=monthly_payment)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
