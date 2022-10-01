#!/usr/bin/env python3

import iris

def connect_SQL():
    connection_string = "k8s-1f0326d6-a9371e85-62cedf778a-d673c0745dc0a7c5.elb.us-east-2.amazonaws.com:1972/USER"
    username = "SQLAdmin"
    password = "HackMIT22!"

    connection = iris.connect(connection_string, username, password)
    return connection

def query_SQL(query, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except:
        print("Invalid query\n")
        return

    results = cursor.fetchall()

    for item in results:
        print(item)
    print()

def main():
    connection = connect_SQL()
    cols = ['timestamp', 'userId', 'platform', 'x', 'y', 'z', 'country', 'event_name', 'event_num']
    
    while True:
        print("columns in DAWN_EVENT: ", ', '.join(cols), '\n')
        query = input("mysql> ")
        if query == 'exit':
            break
        query_SQL(query, connection)


if __name__ == "__main__":
    main()
