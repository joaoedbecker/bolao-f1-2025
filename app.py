from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)

# Inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('bolao.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS palpites 
                 (id INTEGER PRIMARY KEY, usuario TEXT, pole TEXT, p1 TEXT, p2 TEXT, p3 TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/palpite', methods=['POST'])
def palpite():
    usuario = "amigo1"  # Fixo por enquanto
    pole = request.form['pole']
    p1 = request.form['p1']
    p2 = request.form['p2']
    p3 = request.form['p3']
    conn = sqlite3.connect('bolao.db')
    c = conn.cursor()
    c.execute("INSERT INTO palpites (usuario, pole, p1, p2, p3) VALUES (?, ?, ?, ?, ?)", 
              (usuario, pole, p1, p2, p3))
    conn.commit()
    conn.close()
    return "Palpite salvo com sucesso!"

@app.route('/ultima-corrida')
def ultima_corrida():
    url = "http://ergast.com/api/f1/current/last/results.json"
    response = requests.get(url)
    data = response.json()
    race = data['MRData']['RaceTable']['Races'][0]
    podium = [f"{r['Driver']['givenName']} {r['Driver']['familyName']}" for r in race['Results'][:3]]
    return {"corrida": race['raceName'], "podium": podium}

if __name__ == '__main__':
    init_db()
    app.run(debug=True)