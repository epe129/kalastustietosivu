import mysql.connector

# yhteys tietokantaan
mydb = mysql.connector.connect(
    host="localhost",
    user="kalastustietosivu",
    password="2007",
    database="kalastustietosivu"
)

cursor = mydb.cursor()

# luodaan taulut
cursor.execute("CREATE TABLE IF NOT EXISTS kalastaja (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS viehe (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, viehe TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS vapa (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, vapa TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS kala (id INT AUTO_INCREMENT NOT NULL, tarppi_id INT NOT NULL, pituus FLOAT, paino FLOAT, laji TEXT, PRIMARY KEY (id, tarppi_id))")

cursor.execute("CREATE TABLE IF NOT EXISTS tarppi (id INT AUTO_INCREMENT NOT NULL, aika DATETIME, kalastaja_id INT NOT NULL, viehe_id INT NOT NULL, vapa_id INT NOT NULL, paikka TEXT, PRIMARY KEY (id, kalastaja_id, viehe_id, vapa_id))")
