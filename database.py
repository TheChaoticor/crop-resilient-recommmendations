import sqlite3

def create_connection():
    conn = sqlite3.connect('crops.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS crops (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        soil_type TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_crop(name, soil_type):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO crops (name, soil_type) VALUES (?, ?)", (name, soil_type))
    conn.commit()
    conn.close()

def get_crops_by_soil(soil_type):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM crops WHERE soil_type = ?", (soil_type,))
    crops = cursor.fetchall()
    conn.close()
    return [crop[0] for crop in crops]

# Initialize the database
create_table()
