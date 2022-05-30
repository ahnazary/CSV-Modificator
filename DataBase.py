import psycopg2

# Create connection to postgres
con = psycopg2.connect(
                host="172.18.0.2",
                database="SparkConsumer",
                user="user",
                password="admin")
cur = con.cursor()
