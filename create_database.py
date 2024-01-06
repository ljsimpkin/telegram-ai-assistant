import sqlite3

def create_database():
    # Connect to SQLite database (this will create the database if it does not exist)
    conn = sqlite3.connect('telegram_uat.db')

    # Create a cursor object
    c = conn.cursor()

    # Execute SQL commands to create necessary tables
    # For example, a table to store user information
    c.execute('''
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY,
            url TEXT,
            article TEXT,
            summary TEXT,
            article_feedback TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
