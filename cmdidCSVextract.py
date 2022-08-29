"""
    convert cmdid.csv to packetIds.json
    usage:
        py cmdidCSVextract.py <csv-file> <(optional)output json file>
"""

import csv
import json
from sys import argv

def convert(csv_path: str, json_path='./packetIds.json'):
    result = {'13371337': 'PacketHead'}

    with open(csv_path, 'r') as csv_cmdid:
        csv_rows = csv.reader(csv_cmdid)
        for row in csv_rows:
            packetName = row[0]
            cmdid = row[1]
            result[cmdid] = packetName

    with open(json_path, 'w') as json_cmdid:
        json.dump(result, json_cmdid, indent=4)

if __name__ == "__main__":
    if len(argv) == 2:
        convert(argv[1])
    elif len(argv) == 3:
        convert(argv[1], argv[2])
    else:
        print("Invalid arguments")
