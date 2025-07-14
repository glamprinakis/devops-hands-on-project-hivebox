import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def fetch_sensor_data(box_id):
    url = f"https://api.opensensemap.org/boxes/{box_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched data for box: {box_id}")
        return data
    except requests.exceptions.RequestException as err:
        logging.error(f"Error: {err}")
    return None

if __name__ == "__main__":
    box_id = "67a6583c4ef45d000857ddb4"
    data = fetch_sensor_data(box_id)
    if data:
        print("First sensor:", data["sensors"][0]["title"])
    else:
        print("Failed to fetch data.")
