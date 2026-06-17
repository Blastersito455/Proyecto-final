from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "diccionario.db")


def get_db_connection():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/buscar", methods=["POST"])
def buscar():
    palabra = request.form["palabra"].strip()
    if not palabra:
        return redirect(url_for("inicio"))
    return redirect(url_for("resultado", palabra=palabra))


@app.route("/resultado/<palabra>")
def resultado(palabra):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT palabra, significado, region, equivalente FROM palabras WHERE lower(palabra) = lower(?)",
        (palabra,)
    )
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        return render_template(
            "resultado.html",
            palabra=resultado["palabra"],
            significado=resultado["significado"],
            region=resultado["region"],
            equivalente=resultado["equivalente"]
        )

    return render_template(
        "resultado.html",
        palabra=palabra,
        significado=None,
        region=None,
        equivalente=None
    )


if __name__ == "__main__":
    app.run(debug=True)
