'''This is a simple SQL and Python program that allows users to explore a bunch of different dog breeds to determine which would be best for them
By Jess Williams on 15/05/24-current'''
# imports
import sqlite3

# constants and variables
DATABASE = "dogs.db"

# functions
def print_all_dogbreeds():
    '''print a list of all the dog breeds
    By Jess Williams on 20/05/24'''
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
    '''print all data about the dog breeds in the database
    By Jess Williams on 21/05/24'''
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
    '''print the walk durations for all dog breeds
    By Jess Williams on 25/05/2024'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT dog_breeds.breed_name, walkies.duration FROM dog_breeds JOIN walkies ON dog_breeds.walkies_id = walkies.walkies_id ORDER BY dog_breeds.walkies_id ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
   
    print("\nName                    Walk Duration")
    #loop thorugh all of the results
    for breed in results:
        print(f"{breed[0]:<23} {breed[1]:<5}")

def print_sheddness():
    '''print the walk durations for all dog breeds
    By Jess Williams on 26/05/24'''

    #find out what level of shedness the user wants
    shed_amount = input("What level of fur shedding would you like?\n1 A little\n2 Medium\n3 A lot of fur\n")
    while shed_amount not in ('1', '2', '3'):
        print("please enter 1 or 2 or 3\n")
        shed_amount = input("What level of fur shedding would you like?\n1 A little\n2 Medium\n3 A lot of fur\n")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT breed_name, shedding FROM dog_breeds WHERE shedding == {shed_amount} ORDER BY shedding ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
   
    print("\nName                    Shedness out of 3")
    #loop thorugh all of the results
    for breed in results:
        print(f"{breed[0]:<23} {breed[1]:<5}")

def print_sized_dogs():
    ''''''

def print_own_query():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = input("enter an sql query\n")
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    
#main code
while True:
    user_input = input("\nWhat would you like to do? \n1 List of all the Dog Breeds\n2 Print everything in the database\n3 List the walk needs for each dog breed\n4 List dog breeds based on shedding\n7 Exit the program\n")
    if user_input == "1":
        print_all_dogbreeds()
    elif user_input == "2":
        print_all_data()
    elif user_input == "3":
        print_dog_walkies()
    elif user_input == "4":
        print_sheddness()
    elif user_input == "5":
        print_
    elif user_input == "6":
        print_
    elif user_input == "7":
        break
    elif user_input == "secret duck":
        print_own_query()
    else:
        print("\nThat was not an option")