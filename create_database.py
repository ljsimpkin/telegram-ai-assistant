import sqlite3

def insert_article(url, article, summary):
    conn = sqlite3.connect('telegram_uat.db')
    c = conn.cursor()
    c.execute("INSERT INTO articles (url, article, summary) VALUES (?, ?, ?)", (url, article, summary))
    conn.commit()
    conn.close()

def update_article_feedback(url, feedback):
    conn = sqlite3.connect('telegram_uat.db')
    c = conn.cursor()
    c.execute("UPDATE articles SET article_feedback = ? WHERE url = ?", (feedback, url))
    conn.commit()
    conn.close()

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
            chat_id INTEGER,
            url TEXT,
            article TEXT,
            summary TEXT,
            article_feedback BOOLEAN
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
