import urllib.request
import json
import urllib.parse

URL = "http://vldb.gsi.go.jp/sokuchi/surveycalc/surveycalc/bl2st_calc.pl?"

def two_point(location,data):
    lat1 = location[0]#lat1="36.10377477777778"
    lng1 = location[1]#lng1="140.08785502777778"
    lat2 = data[3]#lat2="35.65502847222223"
    lng2 = data[4]#lng2="139.74475044444443"
    two_point_request = "outputType=json&ellipsoid=GRS80&latitude1={}&longitude1={}&latitude2={}&longitude2={}".format(lat1,lng1,lat2,lng2)
    two_point_request = urllib.parse.quote_plus(two_point_request, safe='=&')
    request = URL + two_point_request
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    return directions['OutputData']['geoLength']
