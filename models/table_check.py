import pypyodbc
from config import get_configuration
from Helper import Logger


def table_check(logger_instance):
    # Setting config
    config = get_configuration()
    connection_string = f"Driver={{SQL Server}};Server={config.host};Database={config.database};UID={config.username};PWD={config.password};"
    connection = pypyodbc.connect(connection_string)
    cursor = connection.cursor()

    cursor.execute("SELECT "
                   "CASE WHEN EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'csplit_table') "
                   "THEN 1 ELSE 0 END AS csplit_table_exists, "
                   "CASE WHEN EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'cvdn_table') "
                   "THEN 1 ELSE 0 END AS cvdn_table_exists")
    tables_exist = cursor.fetchone()

    csplit_table_exists = tables_exist[0]
    cvdn_table_exists = tables_exist[1]


    if not csplit_table_exists:
        # Create the csplit_table table if it doesn't exist
        logger_instance.info("csplit table does not exist")
        create_table_query_csplit = """
        CREATE TABLE csplit_table (
            ID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
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
        cursor.execute(create_table_query_csplit)
        connection.commit()
        logger_instance.info("Table 'csplit_table' created successfully.")

    elif not cvdn_table_exists:
        logger_instance.info("CVDN table does not exist")
        create_table_query_cvdn = """
                               CREATE TABLE cvdn_table (
                                   ID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
                                   F1 VARCHAR(255),
                                   VDN INT,
                                   VDN_SYNONYM VARCHAR(255),
                                   INPROGRESS_ATAGENT INT,
                                   OLDESTCALL VARCHAR(255),
                                   AVG_ANSWER_SPEED VARCHAR(255),
                                   ABNCALLS INT,
                                   AVG_ABANDON_TIME VARCHAR(255),
                                   ACDCALLS INT,
                                   AVG_ACD_TALK_TIME VARCHAR(255),
                                   ACTIVECALLS INT
                               )
                               """
        cursor.execute(create_table_query_cvdn)
        connection.commit()
        logger_instance.info("CVDN Table created successfully.")

