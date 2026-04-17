from flask import Flask, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Connessione al database
mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="ROBOT_DB"
)
mycursor = mydb.cursor()

# --- STILE CSS GLOBALE CONDIVISO ---
css_globale = """
<style>
    :root {
        --primary-color: #0f172a;
        --accent-color: #2563eb;
        --accent-hover: #1d4ed8;
        --bg-color: #f8fafc;
        --text-color: #334155;
        --card-bg: #ffffff;
    }
    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        margin: 0; padding: 0;
        background-color: var(--bg-color);
        color: var(--text-color);
        line-height: 1.6;
    }
    /* NAVBAR */
    .navbar {
        background-color: var(--primary-color);
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        position: sticky; top: 0; z-index: 100;
    }
    .nav-logo {
        color: white; font-size: 24px; font-weight: 800; letter-spacing: 1px; text-decoration: none;
    }
    .nav-logo span { color: var(--accent-color); }
    .nav-links a {
        color: #cbd5e1; text-decoration: none; margin-left: 30px; font-weight: 500; font-size: 15px; transition: color 0.3s;
    }
    .nav-links a:hover { color: white; }
    
    /* FOOTER */
    .footer {
        background-color: var(--primary-color);
        color: #94a3b8; text-align: center; padding: 40px 20px; margin-top: 50px; font-size: 14px;
        border-top: 4px solid var(--accent-color);
    }
    .footer-grid { display: grid; grid-template-columns: repeat(3, 1fr); max-width: 1200px; margin: 0 auto 30px; text-align: left; gap: 30px;}
    .footer-col h4 { color: white; font-size: 16px; margin-bottom: 15px; }
    .footer-col p { margin: 5px 0; }
    .footer a { color: var(--accent-color); text-decoration: none; font-weight: bold; }
    .footer a:hover { text-decoration: underline; }
</style>
"""

# --- FUNZIONE PER LE PAGINE DEI REPARTI (TABELLE) ---
def crea_pagina_reparto(titolo, descrizione, dati_robot):
    oggi = datetime.now().strftime("%d/%m/%Y - %H:%M")
    
    html_tabella = ""
    for r in dati_robot:
        html_tabella += f"<tr><td><strong>SYS-{r[0]}</strong></td><td>{r[1]}</td><td><span class='badge'>{r[2]}</span></td><td>{r[3]}</td><td>{r[4]} Ore</td></tr>"
    
    return f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <title>{titolo} | Nexus Robotics</title>
        {css_globale}
        <style>
            .page-header {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; padding: 60px 50px; text-align: center; border-bottom: 5px solid var(--accent-color); }}
            .page-header h1 {{ margin: 0; font-size: 36px; letter-spacing: -1px; }}
            .page-header p {{ margin-top: 15px; color: #94a3b8; font-size: 18px; max-width: 800px; margin-left: auto; margin-right: auto; }}
            .system-status {{ background-color: #dcfce7; color: #166534; padding: 10px; text-align: center; font-size: 14px; font-weight: bold; border-bottom: 1px solid #bbf7d0; }}
            .container {{ max-width: 1200px; margin: 40px auto; padding: 0 20px; }}
            .table-card {{ background: var(--card-bg); border-radius: 12px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); overflow: hidden; }}
            .table-header {{ padding: 20px 25px; border-bottom: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; }}
            .record-count {{ background: #f1f5f9; padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: bold; color: #475569; }}
            table {{ width: 100%; border-collapse: collapse; }}
            th, td {{ padding: 18px 25px; text-align: left; border-bottom: 1px solid #e2e8f0; }}
            th {{ background-color: #f1f5f9; color: #475569; font-weight: 600; text-transform: uppercase; font-size: 13px; letter-spacing: 0.5px; border-bottom: 2px solid #cbd5e1; }}
            tr:last-child td {{ border-bottom: none; }}
            tr:hover {{ background-color: #f8fafc; }}
            .badge {{ background-color: #e0f2fe; color: #0369a1; padding: 5px 12px; border-radius: 20px; font-size: 13px; font-weight: 600; border: 1px solid #bae6fd; text-transform: uppercase; }}
            .btn-back {{ display: inline-block; margin-top: 25px; padding: 12px 24px; background-color: white; border: 1px solid #cbd5e1; color: var(--text-color); text-decoration: none; border-radius: 6px; font-weight: 600; transition: 0.2s; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }}
            .btn-back:hover {{ background-color: #f1f5f9; border-color: #94a3b8; }}
            .status-online {{ color: #10b981; font-weight: bold; }}
        </style>
    </head>
    <body>
        <nav class="navbar">
            <a href="/" class="nav-logo">NEXUS <span>ROBOTICS</span></a>
            <div class="nav-links">
                <a href="/">Home Dashboard</a>
                <a href="/tutti_i_robot">API JSON</a>
            </div>
        </nav>

        <div class="system-status">
            🟢 SISTEMA OPERATIVO | Connessione al Database MariaDB stabilita | Ultima sincronizzazione: {oggi}
        </div>

        <header class="page-header">
            <h1>{titolo}</h1>
            <p>{descrizione}</p>
        </header>

        <main class="container">
            <div class="table-card">
                <div class="table-header">
                    <h3 style="margin: 0; color: #0f172a;">Registro Unità Operative</h3>
                    <span class="record-count">{len(dati_robot)} Record Trovati</span>
                </div>
                <table>
                    <tr>
                        <th>Serial ID</th><th>Designazione Modello</th><th>Classe</th><th>Anno di Entrata</th><th>Cella Energetica</th>
                    </tr>
                    {html_tabella}
                </table>
            </div>
            <a href="/" class="btn-back">← Disconnetti e Torna al Mainframe</a>
        </main>

        <footer class="footer">
            <p>&copy; 2026 Nexus Robotics Corporation. Tutti i diritti riservati.</p>
        </footer>
    </body>
    </html>
    """

# --- LA PAGINA PRINCIPALE (SITO VERO E PROPRIO) ---
@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <title>Nexus Robotics | Portale Aziendale Ufficiale</title>
        {css_globale}
        <style>
            .hero {{ background: linear-gradient(rgba(15, 23, 42, 0.92), rgba(15, 23, 42, 0.85)), url('https://images.unsplash.com/photo-1485827404703-89b55fcc595e?ixlib=rb-1.2.1&auto=format&fit=crop&w=1920&q=80') center/cover fixed; color: white; padding: 120px 20px; text-align: center; }}
            .hero h1 {{ font-size: 52px; margin: 0 0 20px 0; font-weight: 800; letter-spacing: -1px; text-shadow: 0 2px 10px rgba(0,0,0,0.5); }}
            .hero p.lead {{ font-size: 22px; color: #e2e8f0; max-width: 800px; margin: 0 auto 20px auto; }}
            .hero p.sub-lead {{ font-size: 16px; color: #94a3b8; max-width: 600px; margin: 0 auto 40px auto; }}
            
            .stats-bar {{ background-color: var(--accent-color); color: white; display: flex; justify-content: space-around; padding: 30px 20px; flex-wrap: wrap; }}
            .stat-item {{ text-align: center; padding: 10px 20px; }}
            .stat-item h3 {{ font-size: 36px; margin: 0; font-weight: 800; }}
            .stat-item p {{ margin: 5px 0 0 0; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9; }}

            .about-section {{ max-width: 1000px; margin: 60px auto; text-align: center; padding: 0 20px; }}
            .about-section h2 {{ font-size: 32px; color: var(--primary-color); margin-bottom: 20px; }}
            .about-section p {{ font-size: 18px; color: #475569; margin-bottom: 20px; text-align: justify; }}

            .divisions-container {{ max-width: 1200px; margin: 60px auto; padding: 0 20px; }}
            .divisions-header {{ text-align: center; margin-bottom: 50px; border-top: 1px solid #e2e8f0; padding-top: 60px; }}
            .divisions-header h2 {{ font-size: 32px; color: var(--primary-color); margin-bottom: 15px; }}
            
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; }}
            .card {{ background: white; border-radius: 12px; padding: 40px 30px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border: 1px solid #e2e8f0; transition: all 0.3s ease; text-decoration: none; color: inherit; display: flex; flex-direction: column; height: 100%; box-sizing: border-box; }}
            .card:hover {{ transform: translateY(-10px); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); border-color: var(--accent-color); }}
            .card-icon {{ font-size: 48px; margin-bottom: 20px; text-align: center; }}
            .card h3 {{ font-size: 22px; margin: 0 0 15px 0; color: var(--primary-color); text-align: center; }}
            .card p {{ color: #64748b; line-height: 1.6; margin-bottom: 20px; flex-grow: 1; text-align: justify; }}
            .card-btn {{ text-align: center; color: var(--accent-color); font-weight: bold; padding-top: 15px; border-top: 1px solid #f1f5f9; width: 100%; }}
            
            .api-banner {{ background: linear-gradient(to right, #0f172a, #1e293b); color: white; padding: 60px 20px; text-align: center; margin-top: 80px; }}
            .btn-primary {{ display: inline-block; background-color: var(--accent-color); color: white; padding: 14px 35px; border-radius: 6px; text-decoration: none; font-weight: bold; transition: background-color 0.3s; margin-top: 20px; border: 2px solid var(--accent-color); }}
            .btn-primary:hover {{ background-color: transparent; color: white; }}
        </style>
    </head>
    <body>
        <nav class="navbar">
            <a href="/" class="nav-logo">NEXUS <span>ROBOTICS</span></a>
            <div class="nav-links">
                <a href="#chi-siamo">Chi Siamo</a>
                <a href="#dipartimenti">Dipartimenti</a>
                <a href="/tutti_i_robot">Infrastruttura API</a>
            </div>
        </nav>

        <section class="hero">
            <h1>Sistemi Autonomi di Nuova Generazione</h1>
            <p class="lead">Dal 2012, Nexus Robotics Corporation progetta, sviluppa e gestisce le unità robotiche più avanzate per l'industria globale.</p>
            <p class="sub-lead">Questo portale è riservato agli amministratori di sistema per il monitoraggio in tempo reale dei dati operativi estratti dai nostri server centrali.</p>
            <a href="#dipartimenti" class="btn-primary">Accedi al Database Unità</a>
        </section>

        <section class="stats-bar">
            <div class="stat-item">
                <h3>15.000+</h3>
                <p>Unità Operative Attive</p>
            </div>
            <div class="stat-item">
                <h3>99.9%</h3>
                <p>Uptime dei Sistemi</p>
            </div>
            <div class="stat-item">
                <h3>3</h3>
                <p>Poli di Ricerca Globali</p>
            </div>
        </section>

        <section class="about-section" id="chi-siamo">
            <h2>La Nostra Missione Aziendale</h2>
            <p>In Nexus Robotics, crediamo che l'automazione sia la chiave per un futuro più sicuro ed efficiente. I nostri ingegneri lavorano quotidianamente per integrare intelligenza artificiale all'avanguardia con hardware di precisione. Dal settore della sicurezza globale fino all'esplorazione autonoma in ambienti ostili, le nostre macchine sono progettate per resistere dove l'essere umano non può arrivare.</p>
            <p>Tutti i dati sensibili delle nostre unità sono protetti dalla nostra architettura server proprietaria, basata su <strong>MariaDB</strong> e processata dinamicamente tramite cluster Python altamente ottimizzati.</p>
        </section>

        <main class="divisions-container" id="dipartimenti">
            <div class="divisions-header">
                <h2>Accesso Divisioni Operative</h2>
                <p style="color: #64748b; font-size: 18px; max-width: 800px; margin: 0 auto;">Seleziona il dipartimento di competenza per visualizzare i report generati in tempo reale dal nostro database centrale.</p>
            </div>
            
            <div class="grid">
                <a href="/combattimento" class="card">
                    <div class="card-icon">🛡️</div>
                    <h3>Divisione Difesa Strategica</h3>
                    <p>Questo dipartimento gestisce le unità tattiche e da combattimento. Questi robot sono progettati per operazioni di sicurezza avanzata, protezione perimetrale e missioni ad alto rischio.</p>
                    <div class="card-btn">Apri Registro Difesa →</div>
                </a>
                
                <a href="/super_batteria" class="card">
                    <div class="card-icon">⚡</div>
                    <h3>Sistemi ad Alta Autonomia</h3>
                    <p>Sezione dedicata al monitoraggio dei modelli equipaggiati con celle energetiche di Classe A. Queste unità sono capaci di superare le 8000 ore di operatività ininterrotta senza ricarica.</p>
                    <div class="card-btn">Apri Registro Efficienza →</div>
                </a>
                
                <a href="/modelli_storici" class="card">
                    <div class="card-icon">🏛️</div>
                    <h3>Archivio Storico (Pre-2000)</h3>
                    <p>Database di sola lettura contenente i registri di tutte le unità di prima generazione prodotte prima dell'anno 2000. Utilizzati per analisi predittive e machine learning.</p>
                    <div class="card-btn">Apri Archivio Storico →</div>
                </a>
            </div>
        </main>

        <section class="api-banner">
            <h2>Sviluppatori & Integrazioni di Rete</h2>
            <p style="max-width: 700px; margin: 0 auto 30px auto; color: #cbd5e1; font-size: 18px; line-height: 1.6;">La tua infrastruttura ha bisogno di comunicare direttamente con i nostri server? I dati completi del nostro catalogo robotico sono esposti in formato JSON puro.</p>
            <a href="/tutti_i_robot" class="btn-primary">{{}} Accedi all'Endpoint API (JSON)</a>
        </section>

        <footer class="footer">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>NEXUS Robotics HQ</h4>
                    <p>Via dell'Innovazione, 42</p>
                    <p>20126 Milano (MI), Italia</p>
                    <p>P.IVA: IT12345678901</p>
                </div>
                <div class="footer-col">
                    <h4>Supporto Tecnico</h4>
                    <p>Server Status: <strong>Online</strong></p>
                    <p>Database: <strong>MariaDB Cluster</strong></p>
                    <p>Backend: <strong>Python/Flask</strong></p>
                </div>
                <div class="footer-col">
                    <h4>Documentazione</h4>
                    <p><a href="#">Manuale Amministratore</a></p>
                    <p><a href="#">Policy Sicurezza Dati</a></p>
                    <p><a href="/tutti_i_robot">Documentazione API REST</a></p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """

# ROTTA 1: Tutti i robot (JSON puro)
@app.route("/tutti_i_robot")
def tutti_i_robot():
    mycursor.execute("SELECT * FROM Robots")
    row_headers = [x[0] for x in mycursor.description] 
    myresult = mycursor.fetchall()
    json_data = [dict(zip(row_headers, result)) for result in myresult]
    return jsonify(json_data)

# ROTTA 2: Combattimento
@app.route("/combattimento")
def combattimento():
    mycursor.execute("SELECT * FROM Robots WHERE tipo = 'Combattimento'")
    risultati = mycursor.fetchall()
    return crea_pagina_reparto("Divisione Difesa Strategica", "Registro ufficiale delle unità assegnate alle operazioni tattiche.", risultati)

# ROTTA 3: Storici
@app.route("/modelli_storici")
def modelli_storici():
    mycursor.execute("SELECT * FROM Robots WHERE anno_creazione < 2000")
    risultati = mycursor.fetchall()
    return crea_pagina_reparto("Archivio Storico", "Database consultivo dei modelli di prima generazione.", risultati)

# ROTTA 4: Alta Autonomia
@app.route("/super_batteria")
def super_batteria():
    mycursor.execute("SELECT * FROM Robots WHERE autonomia_ore > 8000")
    risultati = mycursor.fetchall()
    return crea_pagina_reparto("Sistemi Alta Autonomia", "Elenco operativo delle unità a lunga durata.", risultati)

if __name__ == "__main__":
    app.run(debug=True)