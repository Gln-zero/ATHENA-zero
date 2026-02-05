import time
import random
import os
from cryptography.fernet import Fernet

# Predefined encryption key
key = b'tRPcOLzl1H14tWs3akbjCz3KJT22O-HD0lnskTfbHco='
cipher_suite = Fernet(key)

global killed
killed = False

def ultrakill():
    try:
        quit()
    except:
        ultrakill()

def Login(cmd):
    global killed
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
            if str(rrname) in decinf:
                print(f"Welcome {name} \nNow logging in to your account")
            else:
                print(f"User {name} not found. \nReopen the program if you used the wrong code. \nOtherwise just forget about this program...")
        except:
            print("I'm sorry. I DO NOT accept codes that are NOT an integer.")
    elif cmdupper == "SIGNUP":
        reguser()
    elif cmdupper == "KILL":
        killed = True
        ultrakill()
    else:
        print(f"Sorry! {cmdupper} is not a valid command.")

def reguser():
    username = input("Enter code as name: ")
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

while __name__ == "__main__":
    if killed == True:
        quit()
    command = input("Welcome to Athena-zero, what can I do for you? : ")
    Login(command)

