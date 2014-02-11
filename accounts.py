# accounts class
# contains classes used to interact with gamer profiles

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_SSLv3)

class Xbox():
    def __init__(self, gamertag):
        if type(gamertag) != str:
            raise Exception("Non-string Xbox Gamertag!")
        
        try:
            path = "https://www.xboxapi.com/v1/json/profile/" + gamertag
            session = requests.Session()
            session.mount('https://', MyAdapter())
            response = session.get(path)
            
            self.__json_dict = response.json()
            self.__player = self.__json_dict["Player"]
        except:
            raise Exception("Fetching Xbox profile failed!")

    def __str__(self):
        return str(self.get_gamertag() + " " + str(self.get_gamerscore()))
    
    def get_json(self):
        # Used for debugging purposes
        return str(self.__json_dict)

    def get_gamertag(self):
        return self.__player["Gamertag"]

    def get_gamerscore(self):
        return self.__player["Gamerscore"]

class Playstation():
    def __init__(self, username):
        pass

    def __str__(self):
        pass
