db = {
   'kenneth': 'password123',
   'kenneth1': 'password'
}

def checkPassword(username, password):
    if not (username in db):
        print("Username not found")
        return
    for i, v in db.items():
        if (i == username):
            if not(v == password):
                print("Incorrect Password")
                return
    print("You have successfully logged in.")

username = (input("Username: ")).lower() # you can add .lower() to make the input all lowercase.
password = input("Password: ")

checkPassword(username, password)
