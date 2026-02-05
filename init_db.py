import sqlite3

conn = sqlite3.connect("acceso.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS personal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token TEXT,
    codigo TEXT,
    nombres TEXT,
    apellidos TEXT,
    cedula TEXT,
    rango TEXT,
    area_autorizada TEXT,
    tipo_sangre TEXT,
    dependencia TEXT,
    estado TEXT
)
""")

conn.commit()
conn.close()

print("Tabla personal creada correctamente")
