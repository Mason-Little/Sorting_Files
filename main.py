import os
import shutil

Input_Path = "C:\\DATA\\DATA_MAIN"  # Input Directory
Output_Path = "C:\\DATA\\DATA_UPLOAD"  # Output Directory
all_car = ['placeholder']  # Placeholder for all car names because I was too lazy to fix a bug
five_year_rule = 1  # Consent for 5 year rule
Gen_Ticker = 1  # Generation Ticker
temp_year_rule = 1  # Temporary year rule
for dirpath, dirnames, filenames in os.walk(Input_Path):  # Walk through the input directory
    temp_list = []
    print("Current Path: ", dirpath)  # Can Comment out
    print("Directories: ", dirnames)  # Can Comment out
    print("Files: ", filenames)  # Can Comment out
    path_list = dirpath.split("\\")  # Split the path into a list
    path_list = path_list.pop(-1)  # Pop the last element off the list and to get the car name
    print(path_list)  # Can Comment out
    car_name = path_list.split("_")  # Split the car name into a list
    if len(car_name) != 1:
        car_name = car_name[:-1]  # Remove the last element from the list because it is the year and we don't need it
        print(car_name)  # Can Comment out
        for filename in filenames:  # For each file in the directory
            full = os.path.join(dirpath, filename)  # Get the full path of the file
            temp_list.append(full)  # Add the full path to the list to use later
        car_name = '_'.join(car_name)
        print(car_name)
        all_car.append(car_name)  # Add the car name to the list of all cars used to check if the cars are the same
        path = os.path.join(Output_Path, car_name)  # Get the path to the output directory
        if all_car[-2] != all_car[-1]:  # If the last car name is not the same as the current car name make new directory
            try:  # Try to make the directory
                os.mkdir(path)
                Gen_Ticker = 1
                Five_Year_Rule = 1
                for file in temp_list:
                    shutil.copy(file, path)
            except FileExistsError:  # If the directory already exists pass and move on
                pass
        elif five_year_rule == 5:  # If the five year rule is 5 add gen to the end of the directory name
            path = path + f'_New_Gen({Gen_Ticker})'
            try:
                os.mkdir(path)
                for file in temp_list:
                    shutil.copy(file, path)
            except FileExistsError:
                for file in temp_list:
                    shutil.copy(file, path)
                temp_year_rule += 1
                if temp_year_rule == 5:
                    temp_year_rule = 1
                    Gen_Ticker += 1
        else:
            try:
                five_year_rule += 1
                for file in temp_list:
                    shutil.copy(file, path)
            except FileExistsError:
                pass
