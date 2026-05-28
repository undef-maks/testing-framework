import requests
from utils.logger import logger

class APIClient:
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }

    def get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"API GET request to: {url}")
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def post(self, endpoint: str, data: dict = None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"API POST request to: {url}")
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def put(self, endpoint: str, data: dict = None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"API PUT request to: {url}")
        response = requests.put(url, headers=self.headers, json=data)
        return response

    def delete(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"API DELETE request to: {url}")
        response = requests.delete(url, headers=self.headers)
        return response
