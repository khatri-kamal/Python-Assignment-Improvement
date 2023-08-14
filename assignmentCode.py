import matplotlib.pyplot as plt

# There are total of 338 Lines of code including space
# There are 192-200 comments in this program
# There are 8 functions

# SOURCE FOR THE CODE Menu Options:

# SOURCE FOR THE CODE summary : week 7
# SOURCE FOR THE CODE calculate the length check : week 7
# SOURCE FOR THE CODE user input length check : week 7

# ========== MENU OPTIONS =============== #


def menu_options():  # Function for the main menu options
    print("***** SCREWS MENU ******")    # "Andy Dolinski"
    print()                              # Title: "Making a menu in Python"
    print("(1): Show the summary report",    # URL: "https://www.youtube.com/watch?v=63nw00JqHo0"
          "\n(2): Show Just the summary for length",
          "\n(3): Show stock based on length",
          "\n(4): Increase or Decrease stock level",
          "\n(5): Print Bar chart",
          "\n(6): check discount"
          "\n(0): Exit the menu")

# SOURCE FOR THE CODE error handling:
# Author: "Corey Schafer"
# Title: "Python Tutorial: Using Try/Except Blocks for Error Handling"
# URL: "https://www.youtube.com/watch?v=NIWwJbo-9_8"


def menu():
    while True:
        # Creates Infinite loop at the stars
        try:  # Error handling part, Try the code below
            menu_options()
            # Calls the function Menu options to list all the options
            print()    # Creates empty space
            choice = int(input("What would you like to do?: "))
            # Ask yours to input a choice from menu options

            if choice == 1:  # if statement to control the flow chart #
                print()   # Creates empty line
                print(" ==================================== Here is the Menu ========================== \n")
                print("================================= Listing showing screw stock details "
                      "=============================",
                      "\n******************************** STOCK ARE IN BOX OF 50 PER UNIT "
                      "*********************************",
                      "\n| MATERIAL  |  HEAD TYPE  |  LENGTH |  STOCK 50  "
                      "|  STOCK 100  |  STOCK 200  |  COST PER BOX of 50 (Â£) | DISCOUNT")
                screw_summary()  # Calls back function which shows the summary of the text file
                print()  # Creates empty line

            elif choice == 2:  # If user enters 2 than the code below will be executed
                print()    # Creates empty line
                length_stock()  # Calls back the length function which prints all the details about different length.
                print()   # Creates empty line

            elif choice == 3:  # If user enters 3 than the code below will be executed
                print()        # Creates empty space
                search_by_length()  # calls the search length function
                print()       # Creates empty line

            elif choice == 4:
                # If user enter 4 than it will execute the increase_decrease_screws,
                # which lets the user change the stock values
                increase_decrease_screws()   # Call and executes this function

            elif choice == 5:  # if user enter 5 this code will run
                bar_chart()  # calls the bar chart function

            elif choice == 6:  # if user enters 6 this code will run
                discount()   # calls discount and run it

            elif choice == 0:  # If user enters 0 than it will close the program
                print()     # Creates empty space
                print("Thank you for using our service.")  # Prints this message before ending the programs
                exit()  # Exits the program
            else:
                print()     # Creates empty line
                print("Invalid Choice")  # if user input anything beside the options then it will show this message
                print()     # Creates empty line

        except ValueError:  # This code to check if the user enters wrong character type
            print()     # Creates empty line
            print("| ================== ERROR ================== |",
                  # If user does put wrong type of character than it will print this message
                  "\n| ===== Wrong Character, Input a number ===== |",
                  "\n| ================== ERROR ================== |")
            print()     # Creates empty line


# This is the start of reading the file.

Screw_stock_details = []   # Creates empty list to store the text file


with open("data.txt", "r") as file:                         
    # The code above opens the text file in read mode as a file variable    
    for row in file:  # This line will loop through the text
        row = row.replace(' ', '')  # Replaces the extra space in index[7]
        start = 0  # Variable to loop through the number
        string_builder = []  # Empty list to store the values
        if not row.startswith("#"):  # Skips the lines with # on it
            for index in range(len(row)):  # for loop to count the number or line
                if row[index] == "," or index == len(row) - 1:   # this checks if there is comma
                    string_builder.append(row[start:index])     # adds the values from start to finsh line by line
                    start = index + 1       # this adds new line each time it loops through
            Screw_stock_details.append(string_builder)  # this puts the details into the main list


def screw_summary():         # function to hold all the screws summary           # Referenced from week 7
    total_stock = 0    # variable to call back later calculate the total stock
    total_cost = 0     # variable to call back later to calculate the total cost
    for each_item in Screw_stock_details:  # loops through the main list
        print('|', each_item[0], '|', (each_item[1]), '|', each_item[2],
              '|', each_item[3], '|', each_item[4], '|', each_item[5], '|', each_item[6], '|', each_item[7])
        # prints all the values from text file
        stock_50 = int(each_item[3])    # sets the variable to calculate stock 50 unit
        stock_100 = int(each_item[4]) * 2    # sets the variable to calculate stock 100 unit and multiplies by 2
        stock_200 = int(each_item[5]) * 4       # sets the variable to calculate stock 100 unit and multiplies by 4
        total_stock += stock_50 + stock_100 + stock_200     # adds all the variable together
        total_cost += (stock_50 + stock_100 + stock_200) * float(each_item[6])
        # calls back total stock and * index 6 for total cost

    print()
    print("| =================== summary ================= |",
          "\n| ========= The total stock is:", total_stock, "========== |",     # prints total stock
          "\n| == The total value of stock is: £", format(total_cost, '.2f'), "== |",  # prints total stock value
          "\n| =================== summary ================= |")


def length_stock():
    total20 = 0     # variable to call back later to calculate the total screws in 20mm
    total40 = 0     # variable to call back later to calculate the total cost screws in 40mm
    total60 = 0     # variable to call back later to calculate the total cost screws in 60mm
    while True:     # infinite loop
        for item in Screw_stock_details:    # loops through the main list
            length = int(item[2])
            # variable to call back later to check if 20mm or 40mm or 60mm is in index 2
            if length == 20:   # checking if 20 is in index 2
                total20 += int(item[3]) + int(item[4])*2 + int(item[5])*4
                # adds all the 20mm stock together and creates a variable
            elif length == 40:      # checking if 40 is in index 2
                total40 += int(item[3]) + int(item[4])*2 + int(item[5])*4
                # adds all the 40mm stock together and creates a variable
            elif length == 60:  # checking if 60 is in index 2
                total60 += int(item[3]) + int(item[4])*2 + int(item[5])*4
                # adds all the 60mm stock together and creates a variable

        print("| ============== Length summary ================= |",
              "\n| ======= Total stock in 20mm is:", total20, "=========== |"  # The total stock with 20mm in length
              "\n| ========= Total stock in 40mm is:", total40, "======== |"   # The total stock with 40mm in length
              "\n| ======== Total stock in 60mm is:", total60, " ======== |",  # The total stock with 40mm in length
              "\n| ============== Length summary ================= |")
        break


def search_by_length():  # stored code to check length of screws

    length_search = int(input("Search screws by length: "))      # ask user for length
    search = 0      # variable to call later
    total = 0       # variable to calculate the total amount of stock
    for line in Screw_stock_details:  # loops through main list
        leng = int(line[2])   # set variable for index 2
        if leng == length_search:     # checks if user enter length is in the file
            search = 1              # used to break out of loop
            print(line[::])         # prints of the length is in file
            stock_50 = int(line[3])     # sets the variable to calculate stock 50 unit
            stock_100 = int(line[4]) * 2  # sets the variable to calculate stock 100 unit * 2
            stock_200 = int(line[5]) * 4   # sets the variable to calculate stock 50 unit  * 4
            total += stock_50 + stock_100 + stock_200  # adds all of them together
    if search == 0:     # if user length is not there than this code will execute
        print("We don't sell that")  # prints this line of code
    print(f"| ===== There are total of {total} screws in {length_search} category ====== |")
    # prints the total length enter by user


def increase_decrease_screws():   # function to increase or decrease the stock
    while True:         # infinite loop
        try:            # error handling  try everything below
            screw_type = input("What Material are you looking for?"
                               "\nSteel or Brass: ")  # ask for screw type
            slot_type = input("What Head type are you looking for?\nstar or slot or PyDrive: ")
            # ask for slot type
            len_type = int(input("What length do you wish to use?\n20 40 60: "))
            # ask for length

            for line in Screw_stock_details:   # loops through main list
                if screw_type == line[0] and slot_type == line[1] and len_type == int(line[2]):
                    # checks if users input is in the file if it is code below will run
                    print("| MATERIAL | HEAD TYPE | LENGTH | STOCK 50 "
                          "|STOCK 100 |STOCK 200 | COST | DISCOUNT")     # prints the layout
                    print('|', line[0],   '|', line[1], '|', line[2],
                          '|', line[3], '|', line[4], '|', line[5], '|', line[6], '|', line[7])
                    # prints the line that matches all the users input
                    print()     # prints empty line
            print("(1): Increase the stock\n"   
                  # prints option of increase or decrease 
                  "(2): Decrease the stock")

            for line in Screw_stock_details:    # loops through main list
                if screw_type.lower() == line[0] and \
                        slot_type.lower() == line[1] and len_type == int(line[2]):
                    # checks if users input is in the file if it is code below will run
                    index = Screw_stock_details.index(line)  # crates a variable for index position
                    stock_50 = int(line[3])     # sets the variable to update later for 50 unit
                    stock_100 = int(line[4])     # sets the variable to update later for 100 unit
                    stock_200 = int(line[5])     # sets the variable to update later for 200 unit

                    inc_dec_user = int(input("Enter a number corresponding with your choice: "))
                    # ask user to choose between increase or decrease
                    if inc_dec_user == 1:    # runs the code if user wish to increase the stock
                        increase = int(input("Enter number you wish to increase by: "))
                        # ask for number user wish to increase
                        print()
                        print("(1): 50 Unit" "\n(2): 100 unit" "\n(3): 200 unit")
                        # prints type of units
                        unit_type = int(input("Enter the unit you wish to update: "))
                        # ask which unit to increase
                        if decrease < 0:
                            decrease_stock == 0

                        if unit_type == 1:  # if user chose to update the 50 unit below code will run
                            new_stock = stock_50 + increase  # adds the new amount
                            Screw_stock_details[index][3] = str(new_stock)  # update the new amount to the list

                        elif unit_type == 2:   # if user chose to update the 100 unit below code will run
                            new_stock = stock_100 + increase    # adds the new amount
                            Screw_stock_details[index][4] = str(new_stock)       # update the new amount to the list

                        elif unit_type == 3:    # if user chose to update the 200 unit below code will run
                            new_stock = stock_200 + increase  # adds the new amount
                            Screw_stock_details[index][5] = str(new_stock)  # update the new amount to the list
                        screw_summary()  # calls the screw summary to check if its update

                    elif inc_dec_user == 2:  # runs this code if user chose to decrease the stock
                        decrease = int(input("Enter number you wish to decrease by: "))  # ask for decrease amount
                        print("(1): 50 Unit" "\n(2): 100 unit" "\n(3): 200 unit")       # prints unit option
                        unit_type = int(input("Enter the unit you wish to update: "))   # ask for which unit to decrease
                         
                        if unit_type == 1:
                            # if user chose to decrease 50 unit this code will run
                            decrease_stock = stock_50 - decrease
                            # puts the decrease amount to the variable
                            Screw_stock_details[index][3] = str(decrease_stock)
                            # master list is updated with the decreased value
                        elif unit_type == 2:
                            # if user chose to decrease 100 unit this code will run
                            decrease_stock = stock_100 - decrease
                            # puts the decrease amount to the variable
                            Screw_stock_details[index[4]] = str(decrease_stock)
                            # master list is updated with the decreased value
                        elif unit_type == 3:
                            # if user chose to decrease 200 unit this code will run
                            decrease_stock = stock_200 - decrease
                            # puts the decrease amount to the variable
                            Screw_stock_details[index][5] = str(decrease_stock)
                            # master list is updated with the decreased value
                        screw_summary()  # calls the summary function

                    else:  # if user puts anything beside the options give this will execute
                        print("ATTENTION: "
                              "Please Use the options listed only")  # gives warning

        except ValueError:  # if user put not character type this will execute
            print("Wrong type of value")   # gives error

        retry = input("Try Again? [Y/N]:")  # ask user to if they want to try again
        if retry.lower() == 'y':    # if yes then code loops to the top
            continue                 # loops to top
        elif retry.lower() == 'n':  # if user = n the takes them to menu
            print()
            print("Back to Menu")
            print()
            menu()      # calls menu
        else:
            print("Wrong character type:")
            # if user doesn't pick any of the options the gives them warning

def bar_chart():  # function to hold all the code for bar chart
    total20 = 0
    total40 = 0
    total60 = 0
    while True:  # infinite loop
        for item in Screw_stock_details:
            # loops through the screw stock list
            length = int(item[2])
            # crates variable to store the index value with integer type
            if length == 20:
                # checks if length has 20
                total20 += int(item[3]) + \
                           int(item[4])*2 + int(item[5])*4
                # add all the variable to 20
            elif length == 40:  # checks if length has 40
                total40 += int(item[3]) + int(item[4])*2 + \
                           int(item[5])*4  # add all the variable to 40
            elif length == 60:  # checks if length has 60
                total60 += int(item[3]) + int(item[4])*2 + \
                           int(item[5])*4  # add all the variable to 20
        break

    bar = [total20, total40, total60]
    # store in a list to call back later
    length = ['20mm', '40mm', '60mm']
    plt.bar(length, bar, color=('red', 'purple', 'green'))
    # plots the length and bar with colour red purple and green
    plt.xlabel('  Screw Length  ')  # This prints in x axis
    plt.ylabel('Number of stocks')  # This value in y axis
    plt.title("Screws Graph")  # Title of the graph
    plt.show()   # displays the bar chart


def discount():  # This function is to check which stock has discount
    stock_with_discount = 'yes'  # variable to call back later
    for line in Screw_stock_details:  # loops through the master list

        if stock_with_discount.lower() == line[7]:
            # check if 'yes' is in index 7 and executes the code below

            print("Stock with the discount")
            print()
            print("| MATERIAL | HEAD TYPE | LENGTH | STOCK 50 "
                  "|STOCK 100 |STOCK 200 | COST | DISCOUNT")
            print('|', line[0],   '|', line[1], '|', line[2], '|',
                  line[3], '|', line[4], '|', line[5], '|', line[6], '|', line[7])
            # prints the line that has discount
            print()

            exit_option = input("Would you like to get back to menu? [Y/N]")  # ask user for option to exit
            if exit_option.lower() == 'y':      # if option = y this below code will run
                menu()              # returns to menu

            else:   # else it will loop back to discount function
                print()
                discount()
            # above code will restart the discount

menu()  # calls the menu
