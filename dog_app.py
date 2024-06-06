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
    sql = "SELECT breed_name FROM dog_breeds;"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("\nBreed Name")
    #loop through all of the results
    for breed in results:
        print(f"{breed[0]:<9}")
    db.close()

def print_all_dogbreeds2():
    '''print a list of all the dog breeds with their id for all_about_one_dog function
    By Jess Williams on 30/05/24'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT breed_id, breed_name FROM dog_breeds;"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print("\nBreed ID Breed Name")
    #loop through all of the results
    for breed in results:
        print(f"{breed[0]:<9} {breed[1]}")
    db.close()

def print_all_data():
    '''print all data about the dog breeds in the database
    By Jess Williams on 21/05/24'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT dog_breeds.breed_name, dog_breeds.energy, walkies.duration, bigness.size, dog_breeds.barkness, dog_breeds.shedding, dog_breeds.cost FROM dog_breeds JOIN walkies ON dog_breeds.walkies_id = walkies.walkies_id JOIN bigness ON dog_breeds.size_id = bigness.size_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("\nName                      Energy   Walk Duration   Size       Barkness  Shedding  Cost Range")
    #loop through all of the results
    for breed in results:
        print(f"{breed[0]:<25} {breed[1]:<8} {breed[2]:<15} {breed[3]:<10} {breed[4]:<9} {breed[5]:<9} {breed[6]:<15}")
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
    '''print dogs that have the level of shedness 
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
   
    print("\nName")
    #loop thorugh all of the results
    for breed in results:
        print(f"{breed[0]:<23}")

def print_sized_dogs():
    '''print dogs that are the size the user wants
    By Jess Williams on 28/05/2024'''

    shed_amount = input("What size dog would you like?\n1 Small \n2 Medium\n3 Large\n4 Giant\n")
    while shed_amount not in ('1', '2', '3','4'):
        print("please enter 1, 2, 3, or 4\n")
        shed_amount = input("What size dog would you like?\n1 Small \n2 Medium\n3 Large\n4 Giant\n")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT dog_breeds.breed_name, bigness.size FROM dog_breeds JOIN bigness ON dog_breeds.size_id = bigness.size_id WHERE size_id = {shed_amount},"
    cursor.execute(sql)
    results = cursor.fetchall()
   
    print("\nName")
    #loop thorugh all of the results
    for breed in results:
        print(f"{breed[0]:<23}")

def all_about_one_dog():
    '''display all possible information about selected dog
    By Jess Williams on 28/05/2024'''
    
    # ask the user if they need a 
    while True:
        decision = input("\nWould you like to:\n1 look at a list of possible dogs to select from\n2 Select the dog you want information about\n")
        if decision == '1':
            decision = "0"
            print_all_dogbreeds2()
            break
        elif decision == '2':
            break
        else:
            print("please enter 1 or 2")

    while True:

        selected_dog = input("\nPlease enter the id for the dog you want information about\n")

        #try and input the selected dog into the query and print the results
        
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        sql = f"SELECT dog_breeds.breed_name, dog_breeds.energy, walkies.duration, bigness.size, dog_breeds.barkness, dog_breeds.shedding, dog_breeds.cost FROM dog_breeds JOIN walkies ON dog_breeds.walkies_id = walkies.walkies_id JOIN bigness ON dog_breeds.size_id = bigness.size_id WHERE dog_breeds.breed_id == {selected_dog};"
        cursor.execute(sql)
        results = cursor.fetchall()

        # if no results are returned (what was entered was not an option)
        if not results:
            print("\nplease enter a valid dog")
            continue
        #output results nicely
        print("\nName                      Energy   Walk Duration   Size       Barkness  Shedding  Cost Range")
        #loop through all of the results
        for breed in results:
            print(f"{breed[0]:<25} {breed[1]:<8} {breed[2]:<15} {breed[3]:<10} {breed[4]:<9} {breed[5]:<9} {breed[6]:<15}\n")
        db.close()
        break

def print_dog_energy():
    '''this is a simple function that will print a set of dogs based on the amount of energy the user wants
    By Jess Williams on 5/06/24'''
    energy_amount = input("What energy level would you like?\n1 low energy\n2 medium energy\n3 High energetic\n")
    while energy_amount not in ('1', '2', '3'):
        print("\nplease enter 1, 2, or 3\n")
        energy_amount = input("What energy level would you like?\n1 low energy\n2 medium energy\n3 High energetic\n")

    #connect the database and 
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"SELECT breed_name, energy FROM dog_breeds WHERE energy = {energy_amount} "
    cursor.execute(sql)
    results = cursor.fetchall()
   
    print("\nName ")
    #loop thorugh all of the results
    for breed in results:
        print(f"{breed[0]:<23} ")

def add_a_dog():
    '''this is a simple function to add a new dog into the database
    By Jess WIlliams on 30/05/24'''

    #connect the database and cursor
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
   
    # get all the values for the new dog

    #id
    max_sql = f"SELECT MAX(breed_id) FROM dog_breeds"
    cursor.execute(max_sql)
    results = cursor.fetchall() 
    for breed in results:
        result = (f"{breed[0]:<23}")
    id = int(result)+1
    
    #name
    name = input("Please enter the name of the dog you would like to add?\n")
    #energy
    while True:
        energy_value = input("How much energy does this dog have?\n1 Low Enegy\n2 Medium Energy\n3 High Energy\n")
        if energy_value in ('1','2','3'):
            int(energy_value)
            break
        else:
            print("\nplease enter 1, 2, or 3\n")
    #walkies
    while True:
        walk = input("How long does this dog need to be walked each day?\n1 30 minutes\n2 45 minutes\n3 1 hour\n4 1-2 hours\n5 2 hours +\n")
        if walk in ('1','2','3','4','5'):
            int(walk)
            break
        else:
            print("\nplease enter 1, 2, 3, 4, or 5\n")
    #size
    while True:
        size = input("What is the size of this dog?\n1 Small\n2 Medium\n3 Large\n4 Giant\n")
        if size in ('1','2','3','4'):
            int(size)
            break
        else:
            print("\nplease enter 1, 2, 3, or 4\n")
    #barkness
    while True:
        bark = input("How much does this dog bark?\n1 A little\n2 A Medium Amount\n3 A lot\n")
        if bark in ('1','2','3'):
            int(bark)
            break
        else:
            print("\nplease enter 1, 2, or 3\n")
    #shedness
    while True:
        fur = input("How much does this dog shed?\n1 A little\n2 A Medium Amount\n3 A lot\n")
        if fur in ('1','2','3'):
            int(fur)
            break
        else:
            print("\nplease enter 1, 2, or 3\n")
    #cost
    money = input("What is the cost range?\n")

    sql = f"INSERT INTO dog_breeds (breed_id, breed_name, energy, walkies_id, Size_id, barkness, Shedding, cost) VALUES ({id}, '{name}', {energy_value}, {walk}, {size}, {bark}, {fur}, '{money}');"
    cursor.execute(sql)
    sql2 = f"SELECT dog_breeds.breed_name, dog_breeds.energy, walkies.duration, bigness.size, dog_breeds.barkness, dog_breeds.shedding, dog_breeds.cost FROM dog_breeds JOIN walkies ON dog_breeds.walkies_id = walkies.walkies_id JOIN bigness ON dog_breeds.size_id = bigness.size_id WHERE dog_breeds.breed_name == '{name}';"
    cursor.execute(sql2)
    results = cursor.fetchall()
   
    print("\nHere is the data for the dog you entered")
    print("Name                      Energy   Walk Duration   Size       Barkness  Shedding  Cost Range")
    print(results)
    #loop thorugh all of the results
    for breed in results:
        print(f"{breed[0]:<25} {breed[1]:<8} {breed[2]:<15} {breed[3]:<10} {breed[4]:<9} {breed[5]:<9} {breed[6]:<15}\n")
    
    save_dog = input("Would you like to save this dog to the database? Y or N\n")
    if save_dog.lower() == 'y':
        db.commit()
    db.close()

def print_own_query():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = input("enter an sql query\n")
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    
#main code
while True:
    user_input = input("""What would you like to do? 
    1 List of all the Dog Breeds
    2 Display everything in the database
    3 List the walk needs for each dog breed
    4 List dog breeds that shed a certian amount
    5 List dogs of a specifc size
    6 List dogs with a specific amount of energy
    7 Print all information about one dog
    8 Add a dog to the database
    9 Exit the program
""")
    if user_input == "1":
        print_all_dogbreeds()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "2":
        print_all_data()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "3":
        print_dog_walkies()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "4":
        print_sheddness()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "5":
        print_sized_dogs()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "6":
        print_dog_energy()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "7":
        all_about_one_dog()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "8":
        add_a_dog()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    elif user_input == "9":
        break
    elif user_input == "secret duck":
        print_own_query()
        run_program = input("Would you like to exit the program?\ny or n\n")
        if run_program.lower() == 'y':
            break
    else:
        print("\nThat was not an option")