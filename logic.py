"""
Author: Thailis Gonzalez
Purpose: This file is intended to contain the program's logic functions, these functions allow you to read, write, 
    and store objects in a CSV file, it also includes utility functions to read auxiliary data useful for 
    users studying archaeology.
"""
import csv

CODE_INDEX = 0
NAME_INDEX = 1
MATERIAL_INDEX = 2
DATED_INDEX = 3
DESCRIPTION_INDEX = 4

#Operation

def read_findings_existing(filename,key_column_index):

    """Reads a CSV file and returns a dictionary of the stored objects, each object is stored using the value of the key column as the key, 
    it also returns an error message if something goes wrong :p"""

    #Initialize the dictionary
    stored_objects = {}

    error_message = None
    
    try: 

        #Operation to open the CSV file provided in read text mode
        with open(filename, "rt", encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")

            try:
                #Skip the header row
                next(csv_reader)

            except StopIteration:

                error_message = f"File {filename} is empty"
                return stored_objects, error_message

            #Add row to dictionary with column key
            for row in csv_reader:

                try:

                    key_value = row[key_column_index]
                    stored_objects[key_value] = row

                except IndexError:
                    
                    error_message = f"There is an invalid data in the row {row}. Please check that the file is correct."
                    return stored_objects, error_message
        
        return stored_objects, error_message
    
    except FileNotFoundError as e:

        error_message = f"File {e.filename} does not exist."
        return stored_objects, error_message
    
    except UnicodeDecodeError:

        error_message = f"File {filename} contains invalid characters. Please check that the file is encoded in UTF-8"
        return stored_objects, error_message

def save_find(filename, code, name, material, dated, description):

    """This function adds a new object record to the CSV file, writes the new row with the given data to the end of the file, 
    returns an error message if something goes wrong, or None if everything it is okey c:"""

    error_message = None
    
    try:
        #Operation to open the CSV file provided in append mode and no extra newlines
        with open(filename, "a", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            #This save the data provided in the corresponding fields in the CSV file
            writer.writerow([code, name, material, dated, description])

        return error_message

    except PermissionError:

        error_message = f"You don't have permission to write to this file {filename}. Please check the file or folder permissions."
        return error_message
    
    except Exception as e:

        error_message = f"An unexpected error has occurred: {e}"
        #print = (error_message)
        return error_message
    
def delete_find(filename, code_to_delete):
    """Deletes a record from the CSV file based on its code, Reads the entire file, deletes the row with the given code, 
    and writes everything back without that row, returns an error if the code doesn't exist or if there are problems :c"""

    error_message = None

    try:

        rows = []
        found = False

        # Read all rows from file
        with open(filename, "rt", encoding="utf-8") as csvfile:
            
            reader = csv.reader(csvfile)
            header = next(reader)
            rows.append(header)

            for row in reader:

                if len(row) > CODE_INDEX and row[CODE_INDEX] == code_to_delete:

                    found = True

                else:

                    rows.append(row)

        if not found:

            error_message = f"Record with code '{code_to_delete}' not found."
            return error_message

        # Rewrite the file without the deleted record
        
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:

            writer = csv.writer(csvfile)
            writer.writerows(rows)

        return error_message

    except FileNotFoundError as e:

        error_message = f"File {e.filename} does not exist."
        return error_message

    except PermissionError:

        error_message = f"You don't have permission to modify the file {filename}."
        return error_message

    except Exception as e:
        error_message = f"An unexpected error has occurred: {e}"
        return error_message

def search_by_field(filename, field_index, search_value):

    """Searches the CSV file for rows where the specified fields contain the search text, returns a list of all rows that partially or fully match :D"""

    #Initialize the list to store the matching rows
    results = []

    try:

        #Operation to open the CSV file provided in read text mode
        with open(filename, "rt", encoding="utf-8") as csvfile:

            csv_reader = csv.reader(csvfile, delimiter=",")

            try:
                #Skip the header row
                next(csv_reader)

            except StopIteration:

                print(f"File {filename} is empty")
                return results

            #Add matching rows to results
            for row in csv_reader:

                try:

                    for index in field_index:

                        #Ensure the row contains the field and the search value matches partially
                        if len(row) > index and search_value.lower() in row[index].lower():
                            results.append(row)
                            break

                except IndexError:

                    print(f"There is invalid data in the row {row}. Please check that the file is correct.")
                    continue
                
    except FileNotFoundError as e:

        print(f"File {e.filename} does not exist.")
        return results
    
    except UnicodeDecodeError:

        print(f"File {filename} contains invalid characters. Please check that the file is encoded in UTF-8")
        return results
    
    return results


def read_alphabet_csv(filename):

    """Reads a CSV file containing Latin and Greek letters, Returns a list of tuples of letters found, if the file is emptyor has errors, returns an empty list D:"""

    #Initialize the list to store the letters in CSV file
    letters = []

    try:
        
        #Operation to open the CSV file provided in read text mode
        with open(filename, "rt", encoding="utf-8") as csvfile:

            reader = csv.reader(csvfile)

            try:
                #Skip the header row
                next(reader)

            except StopIteration:

                print(f"File {filename} is empty")
                return letters

            #Iterate over each row in the CSV file
            for row in reader:

                if len(row) >= 2:
                    letters.append((row[0], row[1]))

        return letters

    except FileNotFoundError as e:

        print(f"File {e.filename} does not exist.")
        return letters

    except UnicodeDecodeError:

        print(f"File {filename} contains invalid characters. Please check that the file is encoded in UTF-8")
        return letters