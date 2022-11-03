from urllib.request import urlopen
import urllib.error
import json
import sqlite3
import ssl
import twurl

conn = sqlite3.connect('py4e_manymany.sqlite')
cur = conn.cursor()
