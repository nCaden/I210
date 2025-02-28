# 11.2 valid zip

# We will use this function in Part 2 as well!
def valid_zip(code):
    return 5 == len(code)
        


# Part 2 - READ ME!!!
# write a function called find_zip() that takes a user-entered string as its parameter.
# First, use the valid_zip() function we wrote to check if it is a valid zip code.
# If it is, determine whether it is in Bloomington (you may need to convert it to an integer).
# Return a message about which of these situations you're in.
def find_zip(zip):
    if valid_zip(zip) == True:
        if (47401 <= int(zip) <= 47408):
            return ("How's the weather in Bloomington")
        else:
            return ("How's the weather in your hometown")
    else:
        return ("Invalid zip code")



# main

# input - get a zip code from the user
zip_code = input("Please enter your zip code: ")

# Part 2
# Call find_zip() on the zip code and receive the result.
# Print a message about the zip code being Bloomington, their home town, or not valid

print(find_zip(zip_code))
