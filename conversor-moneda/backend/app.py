from flask import Flask , request, jsonify, render_template # importacion libreria
from routes import api_bp, basic_data
from config import ipapi
from dotenv import load_dotenv
from config import get_location
import requests
import os
app = Flask(__name__) # Instancia
load_dotenv()

"""
En esta App vamos a necesitar consumir una API
para acceder a los valores de monedas de manera
actualizada segun el mercado de valores.
Para este caso vamos a tener 2 ocpiones en cuenta:
https://www.exchangerate-api.com/ o https://openexchangerates.org/
"""


# http://127.0.0.1:5000/convert?from=USD&to=EUR&amount=100 URL de prueba 

api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
app.register_blueprint(api_bp)
app.register_blueprint(ipapi)
app.register_blueprint(basic_data)

#api_inicial_data = None


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Renderiza documentos html

""" def test():
    return jsonify({
        'data_test': 'data_test'
    }) """

if __name__ == '__main__':
    app.run(debug=True)