from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jobs')
def jobs():
        # Assuming df is your DataFrame
    df = pd.DataFrame({
        'A': [51, 22, 32],
        'B': [4, 455, 6],
        'C': [67, 5, 6],
        'D': [56, 75, 3]
    })

    # Convert the DataFrame to HTML
    table = df.to_html()
    return render_template('jobs.html', table=table)

@app.route('/pricesheets')
def pricesheets():
    df = pd.DataFrame({
        'Pricesheet': ['Pricesheet1', 'Pricesheet2', 'Pricesheet3', 'Pricesheet4'],
        'cost': [100, 200, 300, 1000],
        'picture_quantity': [1, 3, 5, 100],
        'pricture Quality': ['meh', 'okay', 'great', 'amazing']
    })

    # Convert the DataFrame to HTML
    table = df.to_html()
    return render_template('pricesheets.html', table=table)

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




