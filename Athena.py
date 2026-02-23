import time
import random
import os
import requests
from cryptography.fernet import Fernet

# Predefined encryption key
key = b'tRPcOLzl1H14tWs3akbjCz3KJT22O-HD0lnskTfbHco='
cipher_suite = Fernet(key)

global killed
killed = False
global started
started = False
global url
url = "example.com"
global current_user
current_user = ""
def ultrakill():
    try:
        quit()
    except:
        ultrakill()

def Login(cmd):
    global killed
    global current_user
    if killed == True:
        quit()
    path = './userlist.txt'
    cmdupper = cmd.upper()
    users = os.open(path=path, flags=os.O_RDONLY)

    os.lseek(users, 0, 0)
    infostr = os.read(users, os.path.getsize(path))
    os.close(users)

    decinf = ""
    if infostr:
        try:
            encrypted_entries = infostr.split(b'\n')
            for entry in encrypted_entries:
                if entry:
                    decinf += cipher_suite.decrypt(entry).decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            decinf = ""

    if cmdupper == "LOGIN":
        try:
            name = int(input("Hello. Welcome to Athena-zero What is your code? : "))
            rname = str(name)
            rrname = "||" + rname + "||"
            print("Processing...")
            time.sleep(random.randint(1, 3))
            resp = action_at_server(url=url,action="login",arg1=rname)
            if resp == f"loggedinas_{rname}":
                current_user = rname
            if str(rrname) in decinf:
                print(f"Welcome {name} \nNow logging in to your account")
                loggedInAs = name
            else:
                print(f"User {name} not found. \nReopen the program if you used the wrong code. \nOtherwise just forget about this program...")
        except:
            print("I'm sorry. I DO NOT accept codes that are NOT an integer. (Or something went wrong idk (:)")
    elif cmdupper == "SIGNUP":
        reguser()
    elif cmdupper == "KILL":
        killed = True
        ultrakill()
    elif cmdupper == "COMMAND" or cmdupper == "CMD":
        reguser() #change to command function later when exists!!!
    else:
        print(f"Sorry! {cmdupper} is not a valid command.")

def reguser():
    global url
    username = input("Enter code as name: ")
    action_at_server(url=url,action="reguser",arg1=username)
    stringer = "||" + username + "||"
    path = './userlist.txt'
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
        encrypted_string = cipher_suite.encrypt(stringer.encode('utf-8'))
        os.write(fd, encrypted_string + b'\n')  # Append a newline character as a delimiter
    except OSError as e:
        print(f"OS error occurred: {e}")
    finally:
        try:
            os.close(fd)
        except NameError:
            pass

def action_at_server(url="",action="",arg1="",arg2="",arg3=""):
    if action == "login":
        payload = {"username":arg1,"action":"login"}
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return response.text
    
        except requests.exceptions.MissingSchema:
            return "Invalid URL format."
        except requests.exceptions.Timeout:
            return "Request timed out."
        except requests.exceptions.HTTPError as e:
            return f"HTTP Error {e}"
        except requests.exceptions.RequestException as e:
            return f"Network Error {e}"
    elif action == "reguser":
        payload = {"username":arg1,"action":"signup"}
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return response.text
    
        except requests.exceptions.MissingSchema:
            return "Invalid URL format."
        except requests.exceptions.Timeout:
            return "Request timed out."
        except requests.exceptions.HTTPError as e:
            return f"HTTP Error {e}"
        except requests.exceptions.RequestException as e:
            return f"Network Error {e}"
    else:
        payload = {"arg1":arg1,"arg2":arg2,"arg3":arg3,"action":action}
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return response.text
    
        except requests.exceptions.MissingSchema:
            return "Invalid URL format."
        except requests.exceptions.Timeout:
            return "Request timed out."
        except requests.exceptions.HTTPError as e:
            return f"HTTP Error {e}"
        except requests.exceptions.RequestException as e:
            return f"Network Error {e}"

while __name__ == "__main__":
    global killed
    global started
    global url
    if killed == True:
        quit()
    if started == False:
        url = input("What server do you want to log in to? (N for no server (ran locally)")
        if url == "N":
            print("Not logging in to a server! (ran locally)")
            url = "no_url"
        else:
            print(f"Your actions will be executed at {url}!")
    command = input("Welcome to Athena-zero, what can I do for you? : ")
    Login(command)


