import sqlite3, secrets, qrcode

def agregar_persona(codigo, nombres, apellidos, cedula, rango, area, sangre, dependencia, estado):
    token = secrets.token_urlsafe(16)

    conn = sqlite3.connect("acceso.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO personal
    (token, codigo, nombres, apellidos, cedula, rango, area_autorizada, tipo_sangre, dependencia, estado)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (token, codigo, nombres, apellidos, cedula, rango, area, sangre, dependencia, estado))

    conn.commit()
    conn.close()

    link = f"http://127.0.0.1:5000/verificar/{token}"
    img = qrcode.make(link)
    img.save(f"QR_{codigo}.png")

    print("Persona agregada")
    print("Link:", link)
    print("QR creado:", f"QR_{codigo}.png")

if __name__ == "__main__":
    agregar_persona(
        codigo="FL001",
        nombres="Francis Andres",
        apellidos="Leon Anangono",
        cedula="1004616429",
        rango="SUBTENIENTE",
        area="RESTRINGIDA/LIBRE",
        sangre="A+",
        dependencia="INTELIGENCIA",
        estado="ACTIVO"
    )
