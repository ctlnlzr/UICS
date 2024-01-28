from database.database_connection import get_connection, close_connection


def insert_conversion(conversion_id, conversion):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO elements (id, generatedCode) VALUES (?, ?)', (conversion_id, conversion))
        conn.commit()

        conn.close()
        close_connection()

    except Exception as e:
        print(str(e))
        return str(e)


def retrieve_conversion(conversion_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM elements WHERE id = ?', (conversion_id, ))
        conversion = cursor.fetchone()

        conn.close()
        close_connection()

        return conversion
    except Exception as e:
        print(str(e))
        return {'error': str(e)}


def remove_conversion(conversion_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM elements WHERE id = ?', (conversion_id, ))
        conn.commit()

        conn.close()
        close_connection()
    except Exception as e:
        print(str(e))
        return {'error': str(e)}


def list_conversions():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM elements')
        conversions = cursor.fetchall()

        conn.close()
        close_connection()

        return [{'id': row[0], 'generatedCode': row[1]} for row in conversions]
    except Exception as e:
        print(str(e))
        return str(e)
