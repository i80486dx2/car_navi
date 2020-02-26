import read
import json

def get_arrow_icon(data):
    for direction in data:
        if len(direction) == 6:
            print(direction[5])

data = read.get_info()
get_arrow_icon(data)