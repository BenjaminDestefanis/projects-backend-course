from flask import Blueprint, jsonify, request
import requests
import os

api_bp = Blueprint('api', __name__)
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')


# Conversion
@api_bp.route('/convert', methods=['POST'])
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

