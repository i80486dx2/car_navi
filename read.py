import urllib.request
import json
import urllib.parse
import datetime

URL = 'https://maps.googleapis.com/maps/api/directions/json?'
API = 'AIzaSyBAj96WeOENghNJKLJVDoKldxRni1s5Mdo'


def get_info():
    # Google Maps Platform Directions API endpoint
    endpoint = URL
    api_key = API

    # 出発地、目的地を入力
    origin = "郡山駅"
    destination = "会津大学"
    dep_time = "2020/03/01 09:00"

    # UNIX時間の算出
    dtime = datetime.datetime.strptime(dep_time, '%Y/%m/%d %H:%M')
    unix_time = int(dtime.timestamp())

    nav_request = 'language=ja&origin={}&destination={}&departure_time={}&key={}'.format(
        origin, destination, unix_time, api_key)
    nav_request = urllib.parse.quote_plus(nav_request, safe='=&')
    request = endpoint + nav_request
    # Google Maps Platform Directions APIを実行
    #response = urllib.request.urlopen(request).read()
    response  = open('response.json', 'r')
    directions = json.load(response)
    data = []
    for key in directions['routes']:
        for key2 in key['legs']:
            tmp = []
            tmp.append(key2['distance']['value'])  # 距離
            tmp.append(key2['duration_in_traffic']['value'])  # 所用時間
            data.append(tmp)
            for key3 in key2['steps']:
                tmp = []
                tmp.append(key3['distance']['value'])  # distance (m)
                tmp.append(key3['duration']['value'])  # time (second)
                tmp.append(key3['html_instructions'])
                tmp.append(key3['end_location']["lat"])
                tmp.append(key3['end_location']["lng"])
                if 'maneuver' in key3:
                    tmp.append(key3['maneuver'])
                data.append(tmp)
    return data


data = get_info()
#print(data[0])  # ['0.2 km', '1分', '<b>南東</b>に進む', 37.3978083, 140.3873085]
#print(data[0][0])  # 0.2 km
#print(data[0][1])  # 1分
#print(data)
#print(len(data))
