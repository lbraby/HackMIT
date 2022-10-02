#!/usr/bin/env python3

import re
import os
import ijson
import getpass
import datetime
import subprocess
import mysql.connector
import time

def MySQL_connect(hostname, db):
    usernameInput = input('Enter username: ')
    passwordInput = getpass.getpass('Enter password: ')
    connection = mysql.connector.connect(user=usernameInput, password=passwordInput, host=hostname, database=db)
    return connection

def MySQL_query(query, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except:
        return None
    queryFields = [i[0] for i in cursor.description]
    queryResults = cursor.fetchall()
    numFields = len(queryFields)

    return [[results[i] for i in range(numFields)] for results in queryResults]

def import_data(path: str):
    fd = open(path, "r")
    result = ijson.items(fd, 'item')
    return result
