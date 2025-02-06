import sqlite3
import os

def create_database():
    # Get the absolute path to the database directory
    db_path = os.path.join(os.path.dirname(__file__), 'adventureworks.db')
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    
    # Remove database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Create a new database connection
    conn = sqlite3.connect(db_path)
    
    try:
        # Read schema file
        with open(schema_path, 'r') as schema_file:
            schema_script = schema_file.read()
        
        # Execute schema script
        conn.executescript(schema_script)
        
        print(f"Database created successfully at {db_path}")
        
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    create_database() 