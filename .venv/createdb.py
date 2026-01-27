import pymysql, dbinfo
connection = pymysql.connect(host=dbinfo.data["HOST"], port=dbinfo.data["PORT"], user=dbinfo.data["USER"], password=dbinfo.data["PASSWORD"], database=dbinfo.data["DBNIMI"])
cursor = connection.cursor()
def db():
    # luodaan taulut
    cursor.execute("CREATE TABLE IF NOT EXISTS integraatiot (diaNopeus INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS kalastaja (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, nimi TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS viehe (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, viehe TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS vapa (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, vapa TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS laji (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, laji TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS tarppi (id INT AUTO_INCREMENT NOT NULL, aika DATETIME, kalastaja_id INT NOT NULL, viehe_id INT NOT NULL, vapa_id INT NOT NULL, paikka TEXT, PRIMARY KEY (id, kalastaja_id, viehe_id, vapa_id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS kala (id INT AUTO_INCREMENT NOT NULL, tarppi_id INT NOT NULL, pituus FLOAT, paino FLOAT, laji_id INT NOT NULL, PRIMARY KEY (id, tarppi_id))")
db()