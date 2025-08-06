from flask import Flask, render_template, request

app = Flask(__name__)
inventory = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        item = request.form['item']
        qty = request.form['qty']
        price = request.form['price']
        inventory.append({'item': item, 'qty': qty, 'price': price})
    return render_template('index.html', inventory=inventory)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
