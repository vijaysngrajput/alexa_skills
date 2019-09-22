import requests

def give(city):

    data1 = requests.get("https://api.opencagedata.com/geocode/v1/json?q={city}&key=get_your_key_from_login_to_this_website".format(city=city))
    a = data1.json()
    lat = a['results'][0]['geometry']['lat']
    lng = a['results'][0]['geometry']['lng']
    data = requests.get("https://api.darksky.net/forecast/get_your_key_from_login_to_this_website/{lat},{lng}?$format=JSON".format(lat=lat,lng=lng))
    a = data.json()
    summary = a['currently']['summary']
    temp = a['currently']['temperature']
    return summary,temp
