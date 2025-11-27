import requests
import json
from typing import Dict, Any, Optional

def get_server_time() -> None:
    url: str = "http://localhost:8000/time"
    
    try:
        response: requests.Response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data: Dict[str, Any] = response.json()
            time: Optional[str] = data.get('current_time')
            
            if time:
                print(f"Server time: {time}")
            else:
                print("Error: Missing 'current_time' field")
        else:
            print(f"Server error: {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("Error: Connection timeout")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON response")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == '__main__':
    print("Time client started")
    get_server_time()
