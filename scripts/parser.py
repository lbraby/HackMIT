import pandas as pd
import ijson
import connections


def import_data(path: str):
    fd = open(path, "r")
    result = ijson.items(fd, 'item')
    return result

def load_man(data_gen, conn):
    cursor = conn.cursor()
    fieldnamesql = "INSERT INTO DAWN_EVENT (timestamp, userId, platform, x, y, z, country, event_name, event_num) "
    for item in data_gen:
        try:
            valsql = fieldnamesql + "VALUES ("
            valsql += str(item.get("time")) + ", "
            valsql += str(item.get("userId")) + ", "
            valsql += "'" + item.get("platform") + "', "
            valsql += str(item.get("position")[0]) + ", "
            valsql += str(item.get("position")[1]) + ", "
            valsql += str(item.get("position")[2]) + ", "
            valsql += "'" + item.get("country") + "', "
            valsql += "'" + list(item.get("events", {"NONE": "NONE"}).keys())[0] + "', "
            valsql += str(list(item.get("events", {"NONE": "NONE"}).values())[0]) + ")"
            cursor.execute(valsql)
        except Exception as exp:
            print(exp)
            print(item)
            continue
        conn.commit()
    return None


def main():
    result = import_data("./data/dawn-event-data.json")
    connection = connections.run()
    load_man(result, connection)

main()
