from flask import Flask, jsonify
from processing import process_missions, process_donjons
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/missions', methods=['GET'])
def get_missions():
    missions =  process_missions()
    return jsonify(missions.to_dict())

@app.route('/donjons', methods=['GET'])
def get_donjons():
    donjons =  process_donjons()
    return jsonify(donjons.to_dict())

if __name__ == '__main__':
    app.run(debug=True)