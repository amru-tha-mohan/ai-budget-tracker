from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    salary = int(request.form['salary'])
    food = int(request.form['food'])
    rent = int(request.form['rent'])
    travel = int(request.form['travel'])

    total_expense = food + rent + travel
    savings = salary - total_expense

    
    if savings < 0:
        advice = "⚠ You are spending more than your salary!"
    elif food > salary * 0.4:
        advice = "🍔 Your food expense is too high. Try reducing outside food."
    elif rent > salary * 0.5:
        advice = "🏠 Rent is very high compared to salary. Consider cheaper options."
    elif savings > salary * 0.3:
        advice = "🎉 Excellent! You are saving a large portion of your income."
    else:
        advice = "👍 Your budget looks balanced. Keep tracking expenses regularly."

    return render_template(
        "result.html",
        salary=salary,
        total_expense=total_expense,
        savings=savings,
        food=food,
        rent=rent,
        travel=travel,
        advice=advice
    )

if __name__ == '__main__':
    app.run(debug=True)