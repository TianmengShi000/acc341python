import psycopg2

# Paste your Neon connection string here (keep the quotes)
CONNECTION_STRING = "postgresql://YOUR_STRING_HERE"

# Open a connection to the database
conn = psycopg2.connect(CONNECTION_STRING)

# A cursor lets you send SQL commands
cursor = conn.cursor()

# Run a query
cursor.execute("SELECT * FROM customer;")

# Fetch and print every row returned
rows = cursor.fetchall()
for row in rows:
    print(row)

# Always close when finished
cursor.close()
conn.close()