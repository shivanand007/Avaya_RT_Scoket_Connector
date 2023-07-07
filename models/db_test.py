import pypyodbc

# Database connection details
server = '172.18.80.123'
database = 'cms_realtime'
username = 'sa'
password = 'Dev@123'

try:
    # Construct the connection string
    conn_str = f"Driver={{SQL Server}};Server={server};Database={database};UID={username};PWD={password};"

    # Establish a database connection
    connection = pypyodbc.connect(conn_str)

    # Create the csplit_table table
    create_table_query = """
    CREATE TABLE csplit_table (
        F1 VARCHAR(255),
        SPLIT INT,
        INQUEUE_INRING INT,
        AVAILABLE INT,
        ANSTIME_ACDTALKCALLS VARCHAR(255),
        ABNCALLS INT,
        ACD INT,
        OLDESTCALL VARCHAR(255),
        ACD_CALLS INT,
        ACDTIME_ACD_CALLS VARCHAR(255),
        ABNTIME_ABNCALLS VARCHAR(255),
        AGINRING INT,
        ONACD INT,
        INACW INT,
        OTHER INT,
        IN_AUX INT,
        STAFFED INT,
        EWTHIGH VARCHAR(255),
        EWTMEDIUM VARCHAR(255),
        EWTLOW VARCHAR(255),
        DA_INQUEUE_DA_INRING INT,
        ACCEPTABLE_CALLSOFFERED INT,
        SERVICELEVEL INT,
        CALLSOFFERED INT
    )
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()

    # Print success message if the table is created successfully
    print("csplit_table created successfully.")

except pypyodbc.Error as error:
    # Handle exceptions
    print("Error occurred while connecting to the SQL Server database:", error)

finally:
    # Close the database connection
    if 'connection' in locals() and connection is not None:
        connection.close()
        print("SQL Server database connection is closed.")
