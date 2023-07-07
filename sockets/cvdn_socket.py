import socket
from config import get_configuration
from Helper import Logger,cvdn_table_variables_extraction
from models import insert_into_db,table_check

# setting config
config = get_configuration()
port = config.cvdn_port

# setting logger
logger = Logger()
cvdn_logger = logger.cvdn_logger()


def start_cvdn_socket():
    # Create a TCP socket
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_socket.bind(('0.0.0.0', port))
    listener_socket.listen(1)

    print(f"CVDN is started listening on port {port} \n")
    cvdn_logger.info(f"CVDN is started listening on port {port} \n")

    # Accept incoming connection
    client_socket, client_address = listener_socket.accept()
    print(f"Received connection on CVDN from {client_address}")
    cvdn_logger.debug(f"Received connection on CVDN from {client_address}")

    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            received_data = data.decode()
            print(f"Received data from client: {received_data}")
            cvdn_logger.debug(f"Received data from client: {received_data}")
            ''' parsing function to parse the string, 
                string will return a object dict '''

            object_dict = cvdn_table_variables_extraction(received_data)
            print("object created : - ", object_dict)
            cvdn_logger.debug(f"object created : - {received_data}")

            ''' checking availablity of tables in database'''
            table_check(cvdn_logger)

            ''' database insertion operation using models interface '''
            insert_sql = '''
                        INSERT INTO cvdn_table (
                                   F1,
                                   VDN,
                                   VDN_SYNONYM,
                                   INPROGRESS_ATAGENT,
                                   OLDESTCALL,
                                   AVG_ANSWER_SPEED,
                                   ABNCALLS,
                                   AVG_ABANDON_TIME,
                                   ACDCALLS,
                                   AVG_ACD_TALK_TIME,
                                   ACTIVECALLS
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    '''
            insert_into_db(object_dict, insert_sql, cvdn_logger)

    except Exception as e:
        print("Error occurred:", str(e))
        cvdn_logger.error("Error occurred:", str(e))
        # Close the client socket
        client_socket.close()


