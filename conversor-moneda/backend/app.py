from flask import Flask , request, jsonify, render_template # importacion libreria
from dotenv import load_dotenv
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
base_url = 'https://api.exchangerate-api.com/v4/latest/'


def fecth_data():
    response = requests.get(f'https://v6.exchangerate-api.com/v6/{api_key}/codes')
    if response.status_code != 200:
        return jsonify({'error': 'Invalid currency code or API request failed.'}), 400
    data = response.json()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Renderiza documentos html


@app.route('/convert', methods=['POST'])
def convert_currency():
    # Obtenemos los parametros de la solicitud

    data = request.get_json()
    from_currency = data['from'] #Obtiene el codigo de la moneda de origen desde los parametros de la URL
    to_currency = data['to'] #Equivale el valor de la moneda a convertir
    amount = float(data['amount']) #La cantidad
    
    #Solicitud a la API
    response = requests.get(f'{base_url}{from_currency}', params={'apikey': api_key})  # Solicitud a la API
    #response = requests.get(base_url)
    data = response.json() # Convertimos la informacion recivida a JSON

    #Ver si la solicitud fue exitosa
    if response.status_code != 200 or to_currency not in data['rates']: # Si el codigo en la respuesta del servidor no es 200 o si la moneda que queremos convertir mo figura en la respuesta
        return jsonify({'error': 'Invalid currency code or API request failed.'}), 400
    
    #Calculo de la cantidad convertida
    rate = data['rates'][to_currency]
    convert_amount = amount * rate

    #Debolucion de los resultados en JSON

    return jsonify({
        'from_currency': from_currency,
        'to_currency' : to_currency,
        'original_amount' : amount,
        'converted_amount' : convert_amount,
        'rate' : rate
    })


if __name__ == '__main__':
    fecth_data()
    app.run(debug=True)