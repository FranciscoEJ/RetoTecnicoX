import mysql.connector
import json
import logging
from .queries import config


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
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        return {json.dumps(result)}
    except Exception as e:
        logging.error(e)
        return "Not able to connect or query to DB"
    finally:
        cursor.close()
        connection.close()
        return {}
