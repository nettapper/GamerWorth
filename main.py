# main.py
import accounts

def main():
    user_in = input("Please enter in Xbox Gamertag:")
    test = accounts.Xbox(user_in)
    print(test)

if __name__ == "__main__":
    main()
