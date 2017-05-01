import urllib.parse
import requests

url = 'https://api.uber.com/v1.2/estimates/price?server_token=3asL0NWI8SLgpvPOHI3XK-O1TvgQUAw1OTD53LXH&'

def getrideestimate(lat,long,endlat,endlong):
    url2=url+urllib.parse.urlencode({'start_latitude':lat,'start_longitude':long,'end_latitude':endlat,'end_longitude':endlong})
    
    json_data = requests.get(url2).json()
    for x in json_data['prices']:
        print("Vehicle Type:"+x['display_name'])
        print("Distance:"+repr(x['distance'])+"km")
        print("Cost Estimation:"+x['estimate'])
        print("Duration:"+repr(x['duration']/60)+"min")
        print('\n')

def getgeo(addr):
    main_api  = 'https://maps.googleapis.com/maps/api/geocode/json?'
    u1 = main_api + urllib.parse.urlencode({'address': addr})
    json_data1 = requests.get(u1).json()
    print(json_data1['results'][0]['formatted_address'])
    geo = json_data1['results'][0]['geometry']['location']
    return geo

src=input("enter source");
des=input("enter destination");
geo1=getgeo(src)
geo2=getgeo(des)
getrideestimate(geo1['lat'],geo1['lng'],geo2['lat'],geo2['lng'])

