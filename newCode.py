## This is the updated code from my assignment, I have used 2d list and dictionaries in comparssion to the old one.
## Also the visual is better as well and few of the things I couldn't do in assignmnet is also here. 


import matplotlib.pyplot as plt

def get_screw_data(file_path):
    screw_data = []

    with open(file_path, "r") as file:
        for row in file:
            row = row.strip()
            if not row.startswith("#"):
                values = row.split(",")
                screw = [
                    values[0],
                    values[1],
                    int(values[2]),
                    int(values[3]),
                    int(values[4]),
                    int(values[5]),
                    float(values[6]),
                    values[7]
                ]
                screw_data.append(screw)

    return screw_data

def print_screw_data(screw_data):
    if not screw_data:
        print("No data to display.")
        return

    # Calculate the maximum width for each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*screw_data)]
    min_column_widths = [len(header) for header in ["Material", "Head Type", "Length", "Box Of 50", "Box Of 100", "Box Of 200", "Price", "Discount"]]
    column_widths = [max(width1, width2) for width1, width2 in zip(column_widths, min_column_widths)]


    # Print the header separator line
    separator_line = "+".join("-" * (width + 2) for width in column_widths)
    print("+" + separator_line + "+")

    # Print the header
    header = ["Material", "Head Type", "Length", "Box Of 50", "Box Of 100", "Box Of 200", "Price", "Discount"]
    header_formatted = " | ".join("{:<{width}}".format(item, width=width) for item, width in zip(header, column_widths))
    print("| " + header_formatted + " |")

    # Print the header separator line again
    print("+" + separator_line + "+")

    # Print each screw's information in rows
    for screw in screw_data:
        row_formatted = " | ".join("{:<{width}}".format(str(item), width=width) for item, width in zip(screw, column_widths))
        print("| " + row_formatted + " |")

    # Print the footer separator line
    print("+" + separator_line + "+")

def print_summary(screw_data):
    if not screw_data:
        print("No data to display.")
        return

    total_stock = sum(
        int(screw[3]) + int(screw[4]) * 2 + int(screw[5]) * 4
        for screw in screw_data
    )
    
    total_value = sum(
        (int(screw[3]) + int(screw[4]) * 2 + int(screw[5]) * 4) * float(screw[6])
        for screw in screw_data
    )

    print("+--------------------------------------------------+")
    print("| Total Combined Stock (All box types): {:>7}    |".format(total_stock))
    print("| Total Values of the Stocks: £{:>18.2f}  |".format(total_value))
    print("+--------------------------------------------------+")

def search_by_length(screw_data):
    # Create a list of available lengths from the screw data
    available_lengths = list(set(screw[2] for screw in screw_data))
    
    # Display the available lengths with corresponding numbers
    print("Available lengths:")
    for idx, length in enumerate(available_lengths, start=1):
        print(idx, "-", length)
    
    while True:
        try:
            # Prompt the user to enter a number corresponding to the desired length
            length_choice = int(input("Enter the number corresponding to the desired length: ")) - 1
            selected_length = available_lengths[length_choice]
            break  # Break out of the loop if valid input is provided
        except (ValueError, IndexError):
            # Handle invalid input and allow the user to retry
            print("Invalid input. Please enter a valid number.")
            continue

    # Find screws with the selected length
    found_screws = [screw for screw in screw_data if screw[2] == selected_length]

    if not found_screws:
        print("No screws found with the specified length.")
        search_again = input("Would you like to search again? (yes/no): ")
        if search_again.lower() == "yes" or search_again.lower() == "y":
            # Recursively call the search_by_length function to retry
            search_by_length(screw_data)
    
    if found_screws:
        print_screw_data(found_screws)

def calculate_total_combined_length(screw_data):
    length_totals = {}

    for screw in screw_data:
        length = screw[2]
        total_length = int(screw[3]) * 1 + int(screw[4]) * 2 + int(screw[5]) * 4

        if length in length_totals:
            length_totals[length] += total_length
        else:
            length_totals[length] = total_length

    print("\nTotal Length Summary:")
    print("+-------------------+----------------------+")
    print("| Length (mm)       | Total Combined Length|")
    print("+-------------------+----------------------+")
    for length, total_length in length_totals.items():
        print("| {:<17} | {:<20} |".format(length, total_length))
    print("+-------------------+----------------------+")

def update_stock_menu(screw_data):
    while True:
        try:
            # Create a list of unique materials, head types, and lengths
            materials = list(set(screw[0] for screw in screw_data))
            head_types = list(set(screw[1] for screw in screw_data))
            lengths = list(set(str(screw[2]) for screw in screw_data))

            # Display the list of materials and prompt the user to choose one
            print("Select a material:")
            for idx, material in enumerate(materials, start=1):
                print(idx, "-", material)

            material_choice = int(input("Enter the number: ")) - 1
            selected_material = materials[material_choice]

            # Display the list of head types and prompt the user to choose one
            print("\nSelect a head type:")
            for idx, head_type in enumerate(head_types, start=1):
                print(idx, "-", head_type)

            head_type_choice = int(input("Enter the number: ")) - 1
            selected_head_type = head_types[head_type_choice]

            # Display the list of lengths and prompt the user to choose one
            print("\nSelect a length:")
            for idx, length in enumerate(lengths, start=1):
                print(idx, "-", length)

            length_choice = int(input("Enter the number: ")) - 1
            selected_length = lengths[length_choice]

            size = input("Enter the size (50/100/200): ")
            change_amount = int(input("Enter the amount to change: "))

            # Find the index of the specified screw
            for screw in screw_data:
                if (screw[0] == selected_material and
                    screw[1] == selected_head_type and
                    str(screw[2]) == selected_length):

                    if size == "50":
                        new_stock_50 = max(0, int(screw[3]) + change_amount)
                        screw[3] = str(new_stock_50)
                    elif size == "100":
                        new_stock_100 = max(0, int(screw[4]) + change_amount)
                        screw[4] = str(new_stock_100)
                    elif size == "200":
                        new_stock_200 = max(0, int(screw[5]) + change_amount)
                        screw[5] = str(new_stock_200)
                    else:
                        print("Invalid size. Please enter 50, 100, or 200.")

                    # Recalculate the total stock for the screw
                    total_stock = new_stock_50 + (int(screw[4]) * 2) + (int(screw[5]) * 4)
                    screw[6] = str(round(total_stock * float(screw[6]), 2))

                    print("Stock level updated successfully.")
                    return

            print("Screw not found. Stock level not updated.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def create_bar_chart(screw_data):
    # Create lists to store data for plotting
    lengths = []
    stock_levels = []

    for screw in screw_data:
        lengths.append(str(screw[2]))  # Convert length to string for categorical data
        stock_level = int(screw[3]) + int(screw[4]) + int(screw[5])  # Combine stock levels
        stock_levels.append(stock_level)

    # Create the bar chart with colors
    colors = ['red', 'blue', 'green']
    plt.bar(lengths, stock_levels, color=colors)
    plt.xlabel('Length (mm)')
    plt.ylabel('Stock Level')
    plt.title('Stock Levels Based on Length')
    plt.show()

def find_largest_stock_category(screw_data):
    largest_stock = 0
    largest_category = None

    for screw in screw_data:
        total_stock = int(screw[3]) + int(screw[4]) * 2 + int(screw[5]) * 4
        if total_stock > largest_stock:
            largest_stock = total_stock
            largest_category = screw[0]

    return largest_category

def check_and_apply_discount(screw_data):
    largest_category = find_largest_stock_category(screw_data)

    for screw in screw_data:
        if screw[0] == largest_category:
            if screw[7].lower() == "yes":
                print(f"The category '{largest_category}' already has a discount.")
                continue

            print(f"The category with the largest stock is '{largest_category}'.")
            
            while True:
                apply_discount = input("Do you want to apply a 10% discount to this category? (yes/no): ")
                
                if apply_discount.lower() in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            if apply_discount.lower() == "yes":
                screw[7] = "yes"
                print(f"Discount applied to '{largest_category}'.")
            else:
                print("Discount not applied.")
                break  # Exit the loop if discount is not applied

def print_menu():
    menu_options = {
        1: "Show the summary report",
        2: "Show Just the summary for length",
        3: "Search stock based on length",
        4: "Increase or Decrease stock level",
        5: "Print Bar chart",
        6: "Check Discount",
        0: "Exit"
    }
    for key, value in menu_options.items():
        print(f"{key} --- {value}")

def main():
    file_path = "data.txt"
    Screw_stock_details = get_screw_data(file_path)

    while True:
        print("===== SCREW MENU ======")
        print_menu()

        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Invalid input. Please enter a number between 0 and 6.')
            continue

        if option == 1:
            print_screw_data(Screw_stock_details)
            print_summary(Screw_stock_details)
        elif option == 2:
            calculate_total_combined_length(Screw_stock_details)
        elif option == 3:
            search_by_length(Screw_stock_details)
        elif option == 4:
            update_stock_menu(Screw_stock_details)
        elif option == 5:
            create_bar_chart(Screw_stock_details)
        elif option == 6:
            check_and_apply_discount(Screw_stock_details)
        elif option == 0:
            print('Thanks for using the program. Exiting...')
            break
        else:
            print('Invalid option. Please enter a number between 0 and 6.')

if __name__ == '__main__':
    main()