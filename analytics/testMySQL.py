#!/usr/bin/env python3

from queryFunctions import *

cols = ['timestamp', 'userId', 'platform', 'x', 'y', 'z', 'country', 'event_name', 'event_num']

def main():
    connection = MySQL_connect('localhost', 'HackMIT2')
    print()
    query = 'N/A'
    while True:
        print("columns in dawn_event: ", ', '.join(cols))
        print("last query: ", query)
        query = input("mysql> ")
        if query == 'exit':
            break
        result = MySQL_query(query, connection)
        if result:
            for item in result: print(item)
        else: print("invalid query")
        print()


if __name__ == "__main__":
    main()
