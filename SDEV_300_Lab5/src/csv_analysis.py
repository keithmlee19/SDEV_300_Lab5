'''Command menu-driven program to perform statistical analysis
on data from two CSV files'''
import sys
import pandas as pd
import matplotlib.pyplot as plt

def analyze_columns(dfr, col):
    '''Calculates summary stats and histogram for given dataframe/column'''
    print("The statistics for this column are:")
    print("Count = ", dfr[col].count())
    # prints mean and stdev to 1 decimal place
    print("Mean = ", f"{dfr[col].mean():.1f}")
    print("Standard Deviation = ", f"{dfr[col].std():.1f}")
    print("Min = ", dfr[col].min())
    print("Max = ", dfr[col].max())
    print("The histogram of this column is now displayed.")
    dfr[col].hist()
    plt.show()

def handle_pop_data():
    '''Handles user input for population data'''
    pop_data = pd.read_csv("PopChange.csv")
    while True:
        try:
            print("You have entered Population Data.")
            print("Select the column you want to analyze:")
            print("a. Pop Apr 1")
            print("b. Pop Jul 1")
            print("c. Change Pop")
            print("d. Exit Column")
            user_input = input()
            if user_input == "a":
                analyze_columns(pop_data, "Pop Apr 1")
            elif user_input == "b":
                analyze_columns(pop_data, "Pop Jul 1")
            elif user_input == "c":
                analyze_columns(pop_data, "Change Pop")
            elif user_input == "d":
                print("You selected to exit the column menu")
                break
            else:
                print("Invalid choice, please enter a letter a-d")
        except ValueError:
            print("Please enter a letter")

def handle_housing_data():
    '''Handles user input for population data'''
    housing_data = pd.read_csv("Housing.csv")
    while True:
        try:
            print("You have entered Housing Data.")
            print("Select the column you want to analyze:")
            print("a. Age")
            print("b. Bedrooms")
            print("c. Built")
            print("d. Rooms")
            print("e. Utility")
            print("f. Exit Column")
            user_input = input()
            if user_input == "a":
                analyze_columns(housing_data, "AGE")
            elif user_input == "b":
                analyze_columns(housing_data, "BEDRMS")
            elif user_input == "c":
                analyze_columns(housing_data, "BUILT")
            elif user_input == "d":
                analyze_columns(housing_data, "ROOMS")
            elif user_input == "e":
                analyze_columns(housing_data, "UTILITY")
            elif user_input == "f":
                print("You selected to exit the column menu")
                break
            else:
                print("Invalid choice, please enter a letter a-f")
        except ValueError:
            print("Please enter a letter")

def main():
    '''Main function to handle initial user input'''
    while True:
        try:
            print("******* Welcome to the Python Data Analysis App *******")
            print("Select the file you want to analyze:")
            print("1. Population Data")
            print("2. Housing Data")
            print("3. Exit the Program\n")
            user_input = int(input())
            if user_input == 1:
                handle_pop_data()
            elif user_input == 2:
                handle_housing_data()
            elif user_input == 3:
                print("******* Thanks for using the Data Analysis App *******")
                sys.exit()
            else:
                print("Invalid choice, please enter a number 1-3\n")
        except ValueError:
            print("Please enter an integer\n")

# execute main function
if __name__ == "__main__":
    main()
