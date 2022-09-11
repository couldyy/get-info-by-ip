import requests
from pyfiglet import Figlet

def get_info_by_ip(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            '[IP]': response.get('query'),
            '[COUNTRY]': response.get('country'),
            '[COUNTRY CODE]': response.get('countryCode'),
            '[REGION]': response.get('region'),
            '[REGION NAME]': response.get('regionName'),
            '[CITY]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[LAT]': response.get('lat'),
            '[LON]': response.get('lon'),
            '[TIMEZONE]': response.get('timezone'),
            '[ISP]': response.get('isp'),
            '[ORGANISATION]': response.get('org'),
        }
        for k,v in data.items():
            print(f"{k}: {v}")

    except requests.exceptions.ConnectionError:
        print("[*]Check your internet connection!")

def main():
    text1 = Figlet(font='slant')
    print(text1.renderText("IP INFO"))
    ip = input("Input ip: ")
    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()