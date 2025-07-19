import sqlite3

# Sample companies list
companies = [
    ('AAPL', 'Apple Inc.'),
    ('GOOGL', 'Alphabet Inc.'),
    ('MSFT', 'Microsoft Corporation'),
    ('AMZN', 'Amazon.com'),
    ('TSLA', 'Tesla Inc.'),
    ('META', 'Meta Platforms'),
    ('NFLX', 'Netflix'),
    ('NVDA', 'NVIDIA'),
    ('IBM', 'IBM Corp'),
    ('ORCL', 'Oracle')
]

# Connect or create database
conn = sqlite3.connect('database.db')

# Create table if not exists
conn.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        symbol TEXT PRIMARY KEY,
        name TEXT NOT NULL
    );
''')

# Insert company data
conn.executemany('INSERT OR IGNORE INTO companies (symbol, name) VALUES (?, ?)', companies)

conn.commit()
conn.close()

print("✅ Database and 'companies' table created successfully.")
