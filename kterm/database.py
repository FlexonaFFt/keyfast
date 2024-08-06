import sqlite3

class Database:
    def __init__(self, db_name='typing_test_results.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time REAL,
                errors INTEGER,
                wpm REAL
            )
        ''')
        self.connection.commit()

    def add_result(self, time, errors, wpm):
        self.cursor.execute('''
            INSERT INTO results (time, errors, wpm) VALUES (?, ?, ?)
        ''', (time, errors, wpm))
        self.connection.commit()

    def get_results(self):
        self.cursor.execute('SELECT * FROM results')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()