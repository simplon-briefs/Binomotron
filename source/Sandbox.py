import mysql.connector

crew = {1: [3, 14], 2: [2, 6], 3: [4, 9], 4: [19, 11], 5: [20, 18], 6: [16, 10], 7: [7, 15], 8: [12, 1], 9: [8, 5], 10: [13, 17]}
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "binomotron",
    )
cursor = db.cursor()
cursor.execute("DELETE FROM `apprenant_groupe`;")
for groupe in crew:
    for apprenant in crew[groupe]:
        sql = """INSERT INTO apprenant_groupe(id_apprenants, id_projet, id_groupe) VALUES (%s,%s,%s)"""
        value = (apprenant,1,groupe)
        cursor.execute(sql, value)
    db.commit()
db.close()


