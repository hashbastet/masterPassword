import hashlib

def generate_password(username, domain, master, len):
    hashed_password = hashlib.sha512((master + domain + username).encode()).hexdigest()
    return hashed_password[:len]

def main():
    while True:
        username = input("username: ")
        domain = input("domain: ")
        master = input("master: ")
        len = str(input("length: "))
        
        if len.isdigit():
            len = int(len)
        else:
            len = 2147483647
      
        print(generate_password(username, domain, master, len))
        print()

main()
