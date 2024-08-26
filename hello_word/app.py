from flask import Flask # Importamos la libreria flask

app = Flask(__name__) # creacion de la instancia

@app.route('/') # Definicion de ruta
def hello_world(): # Funcion a ejecutarse, al coincidir la ruta
    return {'message' : 'Hello, World!'} # Aqui se retorna un diccionario - A este Flask lo convierte automaticamente a JSON

if __name__ == '__main__': # La app se ejecuta si el archivo es el principal (no importado como modulo)
    app.run(debug=True) # esta linea es la empieza a correr el servidor, "debug=True" reinicia automaticamente el servidor al detectar cambios en el codigo

"""
Para levantar el servidor 
bash
python app.py
"""


