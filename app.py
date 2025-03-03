# app.py
import os
from flask import Flask, render_template, request, jsonify
from ai_operator import process_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le rotte

@app.route('/')
def index():
    """Renderizza la pagina principale"""
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    """Endpoint API per processare le query dell'utente"""
    data = request.json
    user_prompt = data.get('prompt', '')
    
    if not user_prompt:
        return jsonify({'error': 'Prompt vuoto'}), 400
    
    # Processa la query usando il modulo ai_operator
    results = process_query(user_prompt)
    
    return jsonify(results)

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint per verificare che il server sia attivo"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # Ascolta sulla porta definita nella variabile d'ambiente PORT
    # Questa è una convenzione standard di Cloud Run
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
