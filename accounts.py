# accounts class
# contains classes used to interact with gamer profiles

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
import json

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
        self.__gamertag = gamertag
        
        try:
            path = "https://www.xboxapi.com/v1/json/profile/" + self.__gamertag
            session = requests.Session()
            session.mount('https://', MyAdapter())
            self.__response = session.get(path)
        except:
            raise Exception("Fetching Xbox profile failed!")
    
    def __str__(self):
        #return str(self.__gamertag)
        return str(self.__response)
