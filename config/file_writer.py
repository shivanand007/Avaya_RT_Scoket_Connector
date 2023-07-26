''' this file can be executed manually if required '''

import configparser
import os

config = configparser.ConfigParser()

# SQL database section
config['SQLDatabase'] = {
    'host': '',
    'port': '',
    'database': '',
    'username': '',
    'password': ''
}


config['Log'] = {
    'log_level': 'INFO',
    'log_file_path': "/Logs"
}

# Ports section with multiple options
config['Ports'] = {
    'csplit_port': '',
    'cvdn_port': '',
    'custom_port': ''
}

with open('config.ini', 'w') as configfile:
    config.write(configfile)
