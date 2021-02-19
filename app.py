from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_url_path='')
app.config['JSON_SORT_KEYS'] = False # no ordenar propiedades de los JSON 

#
# Rutas del Website
###########################

# Home
@app.route("/", methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')

#
# Rutas del API
###########################

# Devolver una lista de transacciones
@app.route("/api/transaccion", methods=['GET'])
def getTransaccionList():
  
  # Simulamos que las sacamos de la bsae de datos
  transacciones = [ { "id": 1, "desc": 'compra1'}, { "id": 2, "desc": 'venta'} ]
  
  # Devolvemos en formato JSON
  return jsonify(transacciones)

# Ejecutar app
if __name__ == "__main__":
  app.run(debug=True)
