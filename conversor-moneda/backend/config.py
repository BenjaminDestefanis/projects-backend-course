from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os

ipapi_key = os.getenv('API_KEY_IPAPI')
url_ipapi = os.getenv('URL_IPAPI')

app = Flask(__name__)

# Obtener info del usuario

def get_location():
    ip_adress = request.remote_addr # Obtiene la direccion IP del cliente

    response = requests.get(f'{url_ipapi}{ip_adress}?access_key={ipapi_key}')
    data = response.json()

    return jsonify({
        'ip':       data.get('ip'),
        'country':  data.get('country_name'),
        'region':   data.get('region_name'),
        'city': data.get('city')
    })