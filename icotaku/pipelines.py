from itemadapter import ItemAdapter
import mysql.connector

class IcotakuPipeline:
    def process_item(self, item, spider):
        return item


class Database:
    def connectDb():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS icotaku")

    def createTablePlanning():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="icotaku"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS Planning (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, title VARCHAR(255), description TEXT, origin VARCHAR(255), distribution VARCHAR(255), editor VARCHAR(255), releaseDate DATE, category VARCHAR(255), season VARCHAR(255), link VARCHAR(255));")

    def createTablePlanningContent():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="icotaku"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS PlanningContent (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, titleFr VARCHAR(255), titleJp VARCHAR(255), origin VARCHAR(255), genre VARCHAR(255), public VARCHAR(255), nbEpisode VARCHAR(255), durationEpisode VARCHAR(255), editor VARCHAR(255), officialWebsite VARCHAR(255), story TEXT(5000) , img VARCHAR(255));")


    def addRowPlanning(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="icotaku"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO Planning (title, description, origin, distribution, editor, releaseDate, category, season, link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s , %s)"
        val = (item['title'], item['description'], item['origin'], item['distribution'], item['editor'], item['releaseDate'], item['category'], item['season'], item['link'])
        mycursor.execute(sql, val)
        mydb.commit()

    def addRowPlanningContent(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="icotaku"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO PlanningContent (titleFr, titleJp, origin, genre, public, nbEpisode, durationEpisode, editor, officialWebsite, story, img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (item['titleFr'], item['titleJp'], item['origin'], item['genre'], item['public'], item['nbEpisode'], item['durationEpisode'], item['editor'], item['officialWebsite'], item['story'], item['img'])
        mycursor.execute(sql, val)
        mydb.commit()

    def getPlanningUrls():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="icotaku"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT link FROM Planning")
        myresult = mycursor.fetchall()
        return myresult
