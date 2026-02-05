import time
import random
import os
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
    users = os.open(path=path,flags=os.O_RDONLY)
    
    os.lseek(users,0,0)
    infostr = os.read(users, os.path.getsize(path))
    decinf = infostr.decode()
    print(decinf)




    if cmdupper == "LOGIN":
        try:
            name = int(input("Hello. Welcome to Athena-zero What is your code? : "))
            rname = str(name)
            rrname = "||" + rname + "||"
            print("Proccessing...")
            time.sleep(random.randint(2,7))
            if  str(rrname) in decinf:
                print(f"Welcome {name} \nNow logging in to your account")
            else:
                print(f"User {name} not found. \nReopen the program if you used the wrong code. \nOtherwise just forget about this program...")
        except:
            print("I'm sorry. I DO NOT accept codes that are NOT an integer.")
    elif cmdupper == "SIGNUP":
        try:
            name = int(input("Enter a code as your username please: "))
            
        except:
            print("not an int or smth else happened")
    elif cmdupper == "KILL":
        killed = True
        ultrakill()
    elif cmdupper == "SIGNUP":
        reguser()
    else:
        print(f"Sorry! {cmdupper} is not a valid command.")
def reguser():
    username = str(input("name"))
    stringer == "||" + username + "||"
    path = './userlist.txt'
    flags = os.O_RDWR | os.O_CREAT
    fd = os.open(path, flags, mode)
    os.write(fd, stringer.encode())
while __name__ == "__main__":
    if killed == True:
        quit()
    command = input("Welcome to Athena-zero, what can i do for you? : ")
    Login(command)

