import requests
import concurrent.futures

url = "http://127.0.0.1:8080"
num_requests = 100  
concurrent_requests = 10  

def make_request(_):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request successful. Status Code: {response.status_code}")
        else:
            print(f"Request failed. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Exception: {e}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(make_request, range(num_requests))
