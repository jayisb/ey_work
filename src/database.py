import MySQLdb

class Database:
    
    # Configration for database connection
    host = 'localhost'
    user = 'root'
    password = 'root'
    db = 'ey'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    # Query for insertion      
    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except MySQLdb.Error as e:
            print e
            self.connection.rollback()

    # Query for selection        
    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
