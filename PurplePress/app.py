from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/pricesheets')
def pricesheets():
    return render_template('pricesheets.html')

@app.route('/mydesigns')
def mydesigns():
    return render_template('mydesigns.html')

@app.route('/shoppingcart')
def shoppingcart():
    return render_template('shoppingcart.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/fullfillment')
def fullfillment():
    return render_template('fullfillment.html')

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')



if __name__ == '__main__':
    app.run(debug=True)




