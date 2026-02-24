import bcrypt
import sys

def verify_password(hash, password):
    return bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: pw-check.exe <hash> <password>")
        sys.exit(1)

    hash = sys.argv[1]
    password = sys.argv[2]

    if verify_password(hash, password):
        print("Password is correct")
    else:
        print("Password is incorrect")
