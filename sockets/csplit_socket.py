import socket
from config import get_configuration
from Helper import Logger, csplit_table_variables_extraction
from models import insert_into_db,table_check


# setting config
config = get_configuration()
port = config.csplit_port

# setting logger
logger = Logger()
csplit_logger = logger.csplit_logger()

def start_csplit_socket():
    # Create a TCP socket
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_socket.bind(('0.0.0.0', port))
    listener_socket.listen(1)

    print(f"CS_PLIT is started listening on port {port} \n")
    csplit_logger.info(f"CS_PLIT is started listening on port {port} \n")

    while True:
        # Accept incoming connections
        client_socket, client_address = listener_socket.accept()
        print(f"Received connection on CS_PLIT from {client_address}")
        csplit_logger.debug(f"Received connection on CS_PLIT from {client_address}")

        try:
            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break
                received_data = data.decode()
                print(f"Received data from client: {received_data}")
                csplit_logger.debug(f"Received data from client: {received_data}")

                ''' parsing function to parse the string, 
                    string will return a object dict '''

                object_dict = csplit_table_variables_extraction(received_data)
                print("object created : - ", object_dict)
                csplit_logger.debug(f"object created : - {received_data}")

                ''' checking availablity of tables in database'''
                table_check(csplit_logger)

                ''' database insertion operation using models interface '''
                insert_sql = '''
                            INSERT INTO csplit_table (
                                F1, SPLIT, INQUEUE_INRING, AVAILABLE, ANSTIME_ACDTALKCALLS,
                                ABNCALLS, ACD, OLDESTCALL, ACD_CALLS, ACDTIME_ACD_CALLS,
                                ABNTIME_ABNCALLS, AGINRING, ONACD, INACW, OTHER, IN_AUX,
                                STAFFED, EWTHIGH, EWTMEDIUM, EWTLOW, DA_INQUEUE_DA_INRING,
                                ACCEPTABLE_CALLSOFFERED, SERVICELEVEL, CALLSOFFERED
                            )
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        '''
                insert_into_db(object_dict,insert_sql,csplit_logger)

        except Exception as e:
            print("Error occurred:", str(e))
            csplit_logger.error("Error occurred:", str(e))
            client_socket.close()


