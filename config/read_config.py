import configparser
import os


class Configuration:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
        print(config_path)
        config_path = config_path

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

        # Read and store configuration variables
        # Ports section
        self.csplit_port = int(self.config.get('Ports', 'csplit_port'))
        self.cvdn_port = int(self.config.get('Ports', 'cvdn_port'))
        #self.custom_port = int(self.config.get('Ports', 'custom_port'))

        # SQL database section
        self.host = self.config.get('SQLDatabase', 'host')
        self.username = self.config.get('SQLDatabase', 'username')
        self.password = self.config.get('SQLDatabase', 'password')
        self.database = self.config.get('SQLDatabase', 'database')
        self.port = self.config.get('SQLDatabase', 'port')

        # Log section
        self.log_level = self.config.get('Log', 'log_level')
        self.log_file_path = self.config.get('Log', 'log_file_path')


def get_configuration():
    return Configuration()
