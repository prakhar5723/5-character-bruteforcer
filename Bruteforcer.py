import hashlib
import csv
import time
# Created a character list to generate the random word
character_list = ['p', 'a', 's', '4', '!', 'f', 'g',
                  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'b', 'q',
                  'r', 'c', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
                  'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                  'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', 'd',
                  '5', '6', '7', '8', '9', ' ', ':', '.', '?', '@',
                  '$', '-', '=', '[', ']', ';', '\'', '#', "\\", ',',
                  '/', '¬', 'e', '"', '£', '%', '^', '&', '*', '`',
                  '(', ')', '_', '+', '{', '}', '~', '<', '>', '|', '¦',
                  '€', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É',
                  'Í', 'Ó', 'Ú']

Status = "Not Found"    # To get the status of the hash entered
lst = []    # Stores the hashes entered
cracked_lst = []    # Stores the password found
count = len(character_list)  # count of the characters in the character list


def file_input(info):  # Function for file input
    with open("./sha256_hashes.csv", 'r') as file:  # Opening the file
        csvreader = csv.reader(file)
        for column in csvreader:
            lst.extend(column)  # getting the data from the file
    total = len(lst)  # count of the list
    n_list = []  # declaring a list to store just the hashes
    for i in range(2, total, 2):
        n_list.append(lst[i].lower())  # adding hashes to the list
    number = len(n_list)  # count of the hashes we get from the file
    for t in range(0, number):
        print("Decrypting", n_list[t])  # print what is currently being decrypting
        info = decryption(n_list[t], info)  # calling function to decrypt 1 character password
        if info != "Found":  # check if the hash is found
            info = decryption_2_chr(n_list[t], info)  # calling function to decrypt 2 character password
        if info != "Found":  # check if the hash is found
            info = decryption_3_chr(n_list[t], info)  # calling function to decrypt 3 character password
        if info != "Found":  # check if the hash is found
            info = decryption_4_chr(n_list[t], info)  # calling function to decrypt 4 character password
        if info != "Found":  # check if the hash is found
            info = decryption_5_chr(n_list[t], info)  # calling function to decrypt 5 character password
    end = time.time()  # to record the end time of the program
    elapsed = end - start  # calculate the total running time of the program
    minutes = int(elapsed / 60)  # Calculating minutes
    hour = int(minutes / 60)  # Calculating hours
    seconds = elapsed % 60  # Calculating seconds
    print("Elapsed Time: ", hour, "Hours", minutes, "Minutes", " %.2f" % seconds, "Seconds")  # Printing the time
    print("The password(s) entered is/are: ", cracked_lst)  # Printing the list of password


def user_input(info):
    input_count = int(input("Enter the number of input\t"))     # Count of the number of inputs
    for z in range(0, input_count):     # FOR loop for input of the hashes
        password = input("Enter the hash(es) you want to crack \t")     # Variable taking input
        password = password.lower()     # Converting the hash entered into lowercase
        lst.append(password)        # adding the hash into the list
    begin = time.time()     # start recording the time
    for t in range(0, input_count):
        print("Decrypting", lst[t])     # print what is currently being decrypting
        info = decryption(lst[t], info)     # calling function to decrypt 1 character password
        if info != "Found":     # check if the hash is found
            info = decryption_2_chr(lst[t], info)       # calling function to decrypt 2 character password
        if info != "Found":     # check if the hash is found
            info = decryption_3_chr(lst[t], info)       # calling function to decrypt 3 character password
        if info != "Found":     # check if the hash is found
            info = decryption_4_chr(lst[t], info)       # calling function to decrypt 4 character password
        if info != "Found":     # check if the hash is found
            info = decryption_5_chr(lst[t], info)       # calling function to decrypt 5 character password
    end = time.time()       # calculate the total running time of the program
    elapsed = end - begin   # calculate the total running time of the program
    minutes = int(elapsed / 60)     # Calculating minutes
    hour = int(minutes / 60)  # Calculating hours
    seconds = elapsed % 60      # Calculating seconds
    print("Elapsed Time: ", hour, "Hours", minutes, "Minutes", " %.2f" % seconds, "Seconds")  # Printing the time
    print("The password(s) entered is/are: ", cracked_lst)     # Printing the list of password


def decryption(hashed, info):       # function for 1 character
    for a in range(count):      # for loop for 1st character
        guess = character_list[a]   # taking 1 character from character_list
        guess = guess.encode()      # encoding the generated password
        hash_guess = hashlib.sha256(guess)  # hashing the password
        print(character_list[a])    # printing the guesses
        if hashed == hash_guess.hexdigest():        # comparing the guessed password with the user input
            cracked_lst.append(character_list[a])       # adding the password if matched
            info = "Found"      # updating the status
            return info     # returning the status


def decryption_2_chr(hashed, info):     # function for 2 character
    for b in range(count):      # for loop for 1st character
        if info != "Found":     # checking the status of the hash
            for c in range(count):      # for loop for 2nd character
                guess = character_list[b] + character_list[c]   # generating the 2 character password
                guess = guess.encode()      # encoding the generated password
                hash_guess = hashlib.sha256(guess)      # hashing the generated password
                print(character_list[b] + character_list[c])    # printing the generated guesses
                if hashed == hash_guess.hexdigest():        # comparing the guessed password with the user input
                    cracked_lst.append(character_list[b] + character_list[c])       # adding the password if matched
                    info = "Found"      # updating the status
                    return info     # returning the status


def decryption_3_chr(hashed, info):      # function for 3 character
    for d in range(count):      # for loop for 1st character
        if info != "Found":     # checking the status of the hash
            for e in range(count):      # for loop for 2nd character
                if info != "Found":     # checking the status of the hash
                    for f in range(count):      # for loop for 3rd character
                        guess = character_list[d] + character_list[e] + character_list[f]  # generating the 3 character password
                        guess = guess.encode()      # encoding the generated password
                        hash_guess = hashlib.sha256(guess)      # hashing the generated password
                        print(character_list[d] + character_list[e] + character_list[f])        # printing the generated guesses
                        if hashed == hash_guess.hexdigest():        # comparing the guessed password with the user input
                            cracked_lst.append(character_list[d] + character_list[e] + character_list[f])       # adding the password if matched
                            info = "Found"      # updating the status
                            return info     # returning the status


def decryption_4_chr(hashed, info):     # function for 4 character
    for g in range(count):      # for loop for 1st character
        if info != "Found":     # checking the status of the hash
            for h in range(count):      # for loop for 2nd character
                if info != "Found":     # checking the status of the hash
                    for i in range(count):      # for loop for 3rd character
                        if info != "Found":     # checking the status of the hash
                            for j in range(count):      # for loop for 4th character
                                guess = character_list[g] + character_list[h] + character_list[i] + character_list[j]   # generating the 4 character password
                                guess = guess.encode()      # encoding the generated password
                                hash_guess = hashlib.sha256(guess)      # hashing the generated password
                                print(character_list[g] + character_list[h] + character_list[i] + character_list[j])    # printing the generated guesses
                                if hashed == hash_guess.hexdigest():    # comparing the guessed password with the user input
                                    cracked_lst.append(character_list[g] + character_list[h] + character_list[i]
                                                       + character_list[j])     # adding the password if matched
                                    info = "Found"  # updating the status
                                    return info     # returning the status


def decryption_5_chr(hashed, info):
    for k in range(count):     # for loop for 1st character
        if info != "Found":        # checking the status of the hash
            for l in range(count):       # for loop for 2nd character
                if info != "Found":     # checking the status of the hash
                    for m in range(count):      # for loop for 3rd character
                        if info != "Found":     # checking the status of the hash
                            for n in range(count):      # for loop for 4th character
                                if info != "Found":     # checking the status of the hash
                                    for o in range(count):     # for loop for 5th character
                                        guess = character_list[k] + character_list[l] + character_list[m] + \
                                                character_list[n] + character_list[o]   # generating the 5 character password
                                        guess = guess.encode()      # encoding the generated password
                                        hash_guess = hashlib.sha256(guess)      # hashing the generated password
                                        print(character_list[k] + character_list[l] + character_list[m]
                                              + character_list[n] + character_list[o])# printing the generated guesses
                                        if hashed == hash_guess.hexdigest():    # comparing the guessed password with the user input
                                            cracked_lst.append(character_list[k] + character_list[l] + character_list[m]
                                                               + character_list[n] + character_list[o]) # adding the password if matched
                                            info = "Found"      # updating the status
                                            return info     # returning the status


choice = input("Enter 1 for File Input.\nEnter 2 for User Input.\n")    # taking the user input for the type of input
if choice == "1":       # checking the input if its 1
    start = time.time()     # start recording the time
    file_input(Status)      # calling the file input function
elif choice == "2":     # checking the input if its 2
    user_input(Status)      # calling the user input function
else:   # if it is not a valid input
    print("Enter a valid Choice")
