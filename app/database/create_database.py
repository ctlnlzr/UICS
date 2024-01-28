import sqlite3


def execute_sql_file(file_path, conn):
    try:
        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()
            cursor = conn.cursor()
            cursor.executescript(sql_script)
            conn.commit()
            cursor.close()
            print("Table imported successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    conn = sqlite3.connect(r"conversions.db")
    print(sqlite3.version)
    execute_sql_file(r"schema.sql", conn)
    conn.close()
