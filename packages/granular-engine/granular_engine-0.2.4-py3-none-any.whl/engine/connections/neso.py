import requests 


__all__ = ["Neso"]


class Neso:
    def __init__(self, callisto=None, org=None):
        self.callisto = callisto 
        self.org = org 

    def get_sensors(self):
        if self.org:
            sensor_url = f'{self.callisto.host}/neso/api/v1/sensors?orgId={self.org}'
        else:
            sensor_url = f'{self.callisto.host}/neso/api/v1/sensors'

        response  = requests.get(sensor_url, headers=self.callisto.headers)

        if response.status_code == 200:
            sensors = response.json()['data']
            return {sensor["id"]: sensor for sensor in sensors}

        else:
            print(f"Sensor details cannot be retrieved")
            return None
        
    def get_sensor_by_id(self, sensor_id):
        if self.org:
            sensor_url = f'{self.callisto.host}/neso/api/v1/sensors/{sensor_id}?orgId={self.org}'
        else:
            sensor_url = f'{self.callisto.host}/neso/api/v1/sensors/{sensor_id}'

        response  = requests.get(sensor_url, headers=self.callisto.headers)

        if response.status_code == 200:
            sensor = response.json()['data']
            return sensor

        else:
            print(f"Sensor does not exist")
            return None