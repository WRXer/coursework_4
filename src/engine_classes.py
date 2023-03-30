from abc import ABC, abstractmethod
import requests


class Engine(ABC):
    def __init__(self, search_text="python", per_page=10):
        self.search_text = search_text
        self.per_page = per_page

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):
    def get_request(self):
        url = "https://api.hh.ru/vacancies"
        params = {"text": self.search_text,"per_page": self.per_page}

        response = requests.get(url, params=params)

        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                print(vacancy["name"], vacancy["url"])
        else:
            print("Error:", response.status_code)

class SuperJob(Engine):
    def get_request(self):
        pass

hh = HH()
hh.get_request()