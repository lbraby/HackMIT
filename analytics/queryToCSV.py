#!/usr/bin/env python3

from queryFunctions import *
import csv

cols = ['timestamp', 'userId', 'platform', 'x', 'y', 'z', 'country', 'event_name', 'event_num']

def main():
    connection = MySQL_connect('localhost', 'HackMIT2')
    print()
    print("columns in dawn_event: ", ', '.join(cols))
    filename = input("Enter filename: ")
    query = input("mysql> ")

    result = MySQL_query(query, connection)
    if result:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for item in result: 
                writer.writerow(item)
    else: print("invalid query")


if __name__ == "__main__":
    main()
