import sqlite3

def inicializar_base_de_datos():
    # Conecta y crea el archivo de la base de datos en la misma carpeta
    conexion = sqlite3.connect('tp2_base.db')
    cursor = conexion.cursor()

    # Activar el soporte para claves foráneas en SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Crear la tabla 'categorias' (debe ir primero por la relación)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categorias (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_categoria TEXT NOT NULL
    )
    ''')

    # 2. Crear la tabla 'productos' con la clave foránea
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL DEFAULT 0,
        categoria_id INTEGER,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria)
    )
    ''')

    # 3. Insertar categorías iniciales si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM categorias")
    if cursor.fetchone()[0] == 0:
        categorias_ejemplo = [
            ('Electrónica',), 
            ('Hogar y Muebles',), 
            ('Indumentaria',), 
            ('Alimentos',), 
            ('Ferretería',)
        ]
        cursor.executemany("INSERT INTO categorias (nombre_categoria) VALUES (?)", categorias_ejemplo)
        print("Categorías iniciales insertadas.")

    conexion.commit()
    conexion.close()
    print("Base de datos 'tp2_base.db' y tablas creadas exitosamente.")

if __name__ == '__main__':
    inicializar_base_de_datos()