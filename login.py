db = {
   'kenneth': 'password123' 
}

def checkPassword(username, password):
    if not (username in db or password in db):
        print("Incorrect Username or Password.")
        return
    print("You have successfully logged in.")

username = (input("Username: ")).lower() # you can add .lower() to make the input all lowercase.
password = input("Password: ")

checkPassword(username, password)


