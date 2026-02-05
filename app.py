from flask import Flask, abort
import sqlite3

app = Flask(__name__)
DB = "acceso.db"

@app.route("/verificar/<token>")
def verificar(token):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM personal WHERE token=?", (token,))
    p = cur.fetchone()
    conn.close()

    if not p:
        abort(404)

    estado = p["estado"].upper()
    color = "green" if estado == "ACTIVO" else "red"
    texto = "AUTORIZADO" if estado == "ACTIVO" else "NO AUTORIZADO"

    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: Arial; background:#f2f2f2; }}
            .card {{
                max-width: 420px;
                background: white;
                margin: 40px auto;
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 0 15px #999;
            }}
            .estado {{
                background:{color};
                color:white;
                padding:10px;
                border-radius:20px;
                text-align:center;
                font-weight:bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>CONTROL DE ACCESO</h2>
            <div class="estado">{texto}</div>
            <p><b>ID:</b> {p["codigo"]}</p>
            <p><b>Nombres:</b> {p["nombres"]}</p>
            <p><b>Apellidos:</b> {p["apellidos"]}</p>
            <p><b>Cédula:</b> {p["cedula"]}</p>
            <p><b>Rango:</b> {p["rango"]}</p>
            <p><b>Área autorizada:</b> {p["area_autorizada"]}</p>
            <p><b>Dependencia:</b> {p["dependencia"]}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
