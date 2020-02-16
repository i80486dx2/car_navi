import read
import gps

mode = input()
if mode == '1':
    print("button pushed")
    mode = 0
    data = read.get_info()
    # ['0.2 km', '1分', '<b>南東</b>に進む', 37.3978083, 140.3873085]
    print(data[0])
    print(data[0][0])  # 0.2 km
    print(data[0][1])  # 1分
    print(len(data))
    i = 1
    while(i < (len(data)-1)):
        location = []
        location.append(37.397869)  # lat
        location.append(140.387056)  # lng
         ans = gps.two_point(location, data[i])
          print(ans)
           if (data[i][0]*0.2) > float(ans):
                print("goal")
                i = i+1
            else:
                print("not yet")
                print(ans)
            print(data[i])
