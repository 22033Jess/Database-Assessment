'''This is a simple SQL and Python program that allows users to explore a bunch of different dog breeds to determine which would be best for them
By Jess Williams on 20/5/24'''
# imports
import sqlite3

# constants and variables
DATABASE = "dogs.db"

# functions
def print_all_dogbreeds():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT breed_id, breed_name FROM dog_breeds;"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("\nBreed id  Name")
    #loop through all of the results
    for breed in results:
        print(f"{breed[0]:<9} {breed[1]:<5}")
    db.close()

def print_all_data():
    '''print all data about the dog breeds in the database'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT dog_breeds.breed_id, dog_breeds.breed_name, dog_breeds.energy, walkies.duration, bigness.size, dog_breeds.barkness, dog_breeds.shedding, dog_breeds.cost FROM dog_breeds JOIN walkies ON dog_breeds.walkies_id = walkies.walkies_id JOIN bigness ON dog_breeds.size_id = bigness.size_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\nBreed id Name                      Energy   Walk Duration   Size       Barkness  Shedding  Cost Range")
    #loop through all of the results
    for breed in results:
        print(f"{breed[0]:<8} {breed[1]:<25} {breed[2]:<8} {breed[3]:<15} {breed[4]:<10} {breed[5]:<9} {breed[6]:<9} {breed[7]:<15}")
    db.close()

def print_dog_walkies():
    '''print the walk durations for all dog breeds'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT dog_breeds.breed_name, walkies.duration FROM dog_breeds JOIN walkies ON dog_breeds.walkies_id = walkies.walkies_id ORDER BY dog_breeds.walkies_id ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
   
    print("\nName                    Walk Duration")
    #loop thorugh all of the results
    for breed in results:
        print(f"{breed[0]:<23} {breed[1]:<5}")


#main code
while True:
    user_input = input("\nWhat would you like to do? \n1 List of all the Dog Breeds\n2 Print everything in the database\n3 List ")
    if user_input == "1":
        print_all_dogbreeds()
    elif user_input == "2":
        print_all_data()
    elif user_input == "3":
        print_dog_walkies()
    else:
        print("That was not an option\n")