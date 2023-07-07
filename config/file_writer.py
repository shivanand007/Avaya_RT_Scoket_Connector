''' this file can be executed manually if required '''

import configparser
import os

config = configparser.ConfigParser()

# SQL database section
config['SQLDatabase'] = {
    'host': '172.18.80.123',
    'port': '1433',
    'database': 'cms_db',
    'username': 'sa',
    'password': 'Dev@123'
}


config['Log'] = {
    'log_level': 'INFO',
    'log_file_path': "/Logs"
}

# Ports section with multiple options
config['Ports'] = {
    'csplit_port': '9000',
    'cvdn_port': '9001',
    'custom_port': ''
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
