#python3
import mysql.connector

debug = 0
menu = "This is the main menu, please select an option\n  1:Show Tables\n  2:"

def mySQL_select(mydb,table,selector="*"):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT {} FROM {}".format(selector,table))
    myresult = mycursor.fetchall()
    if debug:
        for x in myresult:
            print(x)
    return myresult

def mySQL_wildcard(mydb,wildcard):
    mycursor = mydb.cursor()
    mycursor.execute(wildcard)
    myresult = mycursor.fetchall()
    if debug:
        for x in myresult:
            print(x)
    return myresult

def mainMenu(menu):
    # using the while loop to print menu list    
    print(menu)
    try:
        users_choice = int(input("\nEnter your Choice: ")) 
    except ValueError:
        print("Invalid choice")

def checkForCreds(mydb):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if debug:
        print("your inputs {}-{}".format(username,password))
    values = mySQL_select(mydb,"members","login,password")
    for x in values:
        if x[0] == username:
            if x[1] == password:
                print("welcome to the mainframe {}".format(username))
                return
        # print (x)
    print("invalid creds ... bye")
    exit(0)

def getDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Qpalzm226!",
        database="mydb"
    )
    return mydb

def main():
    mydb = getDatabase()
    # checkForCreds(mydb)
    menu = "menu"
    while 1:
        mainMenu(menu)

if __name__ == "__main__":
    main()