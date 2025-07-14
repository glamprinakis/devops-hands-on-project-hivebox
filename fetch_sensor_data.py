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
        logging.error(f"Error fetching box {box_id}: {err}")
    return None

if __name__ == "__main__":
    box_ids = [
        "67a6583c4ef45d000857ddb4", 
        "67be1f59003189000779808a",
        "67be0c77003189000759263a"
    ]

    for box_id in box_ids:
        data = fetch_sensor_data(box_id)
        if data and "sensors" in data and data["sensors"]:
            print(f"Box {box_id} - First sensor: {data['sensors'][0]['title']}")
        else:
            print(f"Failed to fetch data for box {box_id}")
