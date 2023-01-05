import mysql.connector
from configparser import ConfigParser

def do_connection():
    config = ConfigParser()
    config.read('config.ini')
    cfg = config['SESSION']
    connec = mysql.connector.connect(host='127.0.0.1', user=cfg["user"],passwd=cfg["psswd"], db=cfg["db"])
    return connec
