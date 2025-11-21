import requests
import json

def get_server_time():
    url = "http://localhost:8000/time"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"Time: {data['current_time']}")
        else:
            print(f"Error: {response.status_code}")
    except:
        print("Couldn't connect")

if __name__ == '__main__':
    get_server_time()