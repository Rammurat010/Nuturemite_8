from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the products page
@app.route('/products')
def products():
    return render_template('products.html')

# Route for the vendor registration page
@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True , port=5003)  
            
