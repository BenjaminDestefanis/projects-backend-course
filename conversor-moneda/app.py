from flask import Flask , request, jsonify # importacion libreria
import requests
app = Flask(__name__) # Instancia

"""
En esta App vamos a necesitar consumir una API
para acceder a los valores de monedas de manera
actualizada segun el mercado de valores.
Para este caso vamos a tener 2 ocpiones en cuenta:
https://www.exchangerate-api.com/ o https://openexchangerates.org/
"""

api_key = 'e278246514e613608d97c59f'
base_url = 'https://api.exchangerate-api.com/v4/latest/'
#base_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

@app.route('/convert', methods=['GET'])
def convert_currency():
    # Obtenemos los parametros de la solicitud
    from_currency = request.args.get('from')  #Obtiene el codigo de la moneda de origen desde los parametros de la URL
    to_currency = request.args.get('to') #Equivale el valor de la moneda a convertir
    amount = float(request.args.get('amount')) #La cantidad
    
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
    app.run(debug=True)