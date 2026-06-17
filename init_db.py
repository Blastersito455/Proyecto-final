import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "diccionario.db")

WORDS = [
    (
        "piola",
        "En Argentina y Uruguay, significa 'bueno', 'tranquilo' o 'buena onda'.",
        "Argentina / Uruguay",
        "chévere (Colombia, Venezuela, Puerto Rico), bacán (Chile, Perú, Ecuador), chido / padre (México)"
    ),
    (
        "chévere",
        "En Colombia, Venezuela y Puerto Rico, significa 'genial' o 'muy bueno'.",
        "Colombia / Venezuela / Puerto Rico",
        "piola (Argentina, Uruguay), bacán (Chile, Perú, Ecuador), chido / padre (México)"
    ),
    (
        "bacán",
        "En Chile, Perú y Ecuador, significa 'muy bueno', 'chévere' o 'excelente'.",
        "Chile / Perú / Ecuador",
        "chévere (Colombia, Venezuela, Puerto Rico), piola (Argentina, Uruguay), chido (México)"
    ),
    (
        "chido",
        "En México significa 'bueno', 'genial' o 'agradable'.",
        "México",
        "chévere (Colombia, Venezuela, Puerto Rico), bacán (Chile, Perú, Ecuador), piola (Argentina, Uruguay)"
    ),
    (
        "bo",
        "En Paraguay se usa como muletilla para llamar la atención de alguien, similar a 'oye'.",
        "Paraguay",
        "oye (España, México), che (Argentina, Uruguay, Paraguay)"
    ),
    (
        "castellano",
        "En España, se usa como sinónimo de 'español' y no es común en la mayoría de América Latina.",
        "España",
        ""
    ),
    (
        "malparido",
        "En Argentina y Uruguay se usa como insulto fuerte similar a 'hijo de puta'.",
        "Argentina / Uruguay",
        "hijo de puta (varios países), cabrón (México), malnacido (España)"
    ),
    (
        "ñero",
        "En Colombia, se usa para referirse a un amigo cercano o compañero de confianza.",
        "Colombia",
        "parcero (Colombia), cuate (México), pana (Caribe)"
    )
]


def iniciar_base_de_datos():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS palabras (
            palabra TEXT PRIMARY KEY,
            significado TEXT NOT NULL,
            region TEXT,
            equivalente TEXT
        )
        """
    )
    cursor.executemany(
        "INSERT OR REPLACE INTO palabras (palabra, significado, region, equivalente) VALUES (?, ?, ?, ?)",
        WORDS
    )
    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    iniciar_base_de_datos()
    print(f"Base de datos inicializada en: {DB_PATH}")
