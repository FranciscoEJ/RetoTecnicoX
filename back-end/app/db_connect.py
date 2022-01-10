import mysql.connector


def query_mysql(query):
    """
    Create a conection to a MySQL database to query information
    Args:
        query (string): The query to execute
    Returns:
        answer (List[Dict]): Query's result
    """
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute(query)
        for row in cursor:
            yield row
    except Exception as e:
        logging.error(E)
        return "Not able to connect or query to DB"
    finally:
        cursor.close()
        connection.close()
