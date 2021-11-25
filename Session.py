import requests, random, json, colorama
from colorama import init

colorama.init(autoreset=True)
init()

ERROR = "[\x1b[31m-\x1b[39m]"
WHITE = "\033[1;37;40m"
BLUE = "\033[1;36;40m"
THREADSUCCESS = "[\033[1;36;40m!\033[1;37;40m]"
SUCCESS = "[\x1b[32m+\x1b[39m]"
CLAIMED = "[\x1b[32m!\x1b[39m]"
INPUT = "[\x1b[33m?\x1b[39m]"
INFO = "[\x1b[35m*\x1b[39m]"
spinners = ["/", "-", "\\", "|"]

class twitter_login():
    def __init__(self) -> None:
        print('{}'.format(INFO), end='');username = input(' Username: ')
        print('{}'.format(INFO), end='');password = input(' Password: ')
        c = self.login(username,password)
        if c is False:
            print(f"\n{ERROR} Bad Password Or Blocked")
        else:
            ct0 = str(c["ct0"])
            auth = str(c["auth_token"])	
            print("[SUCCESS] Grabbed Main Auth...")
            with open("Main_Account.txt","w") as wr:
                info = {"ct0":ct0,"auth":auth}
                json.dump(info,wr)
        print(f"\n{INFO} Loading Other Account...\n")
        print('{}'.format(INFO), end='');username = input(' Username: ')
        print('{}'.format(INFO), end='');password = input(' Password: ')
        c = self.login(username,password)
        if c is False:
            print(f"\n{ERROR} Bad Password Or Blocked")
        else:
            ct0 = str(c["ct0"])
            auth = str(c["auth_token"])	
            print(f"{SUCCESS} Grabbed Fresh Auth...")
            with open("Fresh_Account.txt","w") as wr:
                info = {"ct0":ct0,"auth":auth}
                json.dump(info,wr)
    def login(self,Username,Password):
        letters = 'qwertyuiopasdfghjklzxcvbnm123456790qwertyiobuzxcvbasdfr142'
        token = ''.join(random.choice(letters) for x in range(23)) 
        session = requests.Session()
        url = "https://twitter.com/sessions"
        session.headers = {
        "Host": "twitter.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }
        cookies = {
        "_mb_tk":token
        }
        data = {
        "authenticity_token":token,
        "session[username_or_email]":Username,
        "session[password]":Password
        }
        response = session.post(url, data=data , cookies=cookies)
        y = session.cookies.get_dict()
        try:

            c = str(y["ct0"])
            v = str(y["auth_token"])	
            return y
        except:
            return False
if __name__ == "__main__":
    print(f"{SUCCESS} Twitter Session Grabber\n")
    twitter_login()

