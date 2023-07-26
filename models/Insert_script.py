import pypyodbc
from config import get_configuration


# Setting config
config = get_configuration()


def insert_into_db(object_dict, query_payload,logger_instance):
    # Initialize cursor to None
    cursor = None
    connection = None

    try:
        # Connect to the SQL Server database using pypyodbc
        connection_string = f"Driver={{SQL Server}};Server={config.host};Database={config.database};UID={config.username};PWD={config.password};"
        connection = pypyodbc.connect(connection_string)

        logger_instance.info(f"Database Information from config file: {config.host} | {config.database} | {config.username} | {config.password}")

        # Create a cursor to execute SQL statements
        cursor = connection.cursor()

        cursor.execute(query_payload, tuple(object_dict.values()))
        connection.commit()
        logger_instance.debug("Data inserted successfully into 'csplit_table'.")
        print("Data inserted successfully into 'csplit_table'.")

    except pypyodbc.Error as error:
        logger_instance.error(f"Error occurred while connecting to SQL Server:, {error}")
        print("Error occurred while connecting to SQL Server:", error)

    finally:
        # Close the cursor and the SQL Server connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

        if 'connection' in locals() and connection is not None:
            connection.close()
            print("SQL Server connection is closed.")

