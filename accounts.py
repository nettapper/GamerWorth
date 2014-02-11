# accounts class
# contains classes used to interact with gamer profiles

class Xbox():
    def __init__(self, gamertag):
        if type(gamertag) != str:
            raise Exception("Non-string gamertag!")
        self.__gamertag = gamertag

    def __str__(self):
        return str(self.__gamertag)
